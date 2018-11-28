#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef double LD;

const int DBG = 0, INF = int(1e9);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

int main() {
  	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);
	
	int Q;
	
	cin >> Q;
	
	REP(q,Q) {cerr << q << endl;
	
		cout << "Case #" << q + 1 << ": ";
		
		int c,d;
		
		cin >> c >> d;
		
		vector<PII> V(c);
		
		REP(i,c) 
			cin >> V[i].ST >> V[i].ND;
			
		LD sm = 0;
		
		REP(i,c)
			sm += V[i].ND;
			
		LD left = 0, right = LD(d) * sm;
		
		LD eps = 0.00025;
		
		while (left < right - eps) {
		
			LD t = (left + right) / 2;
			
			vector<PII> W = V;
			
			LD last = W[0].ST - t; W[0].ND--;
			
			int k = 0;
			
			bool ok = true;
			
			while (k < c) 
				if (W[k].ND == 0)
					++k;
				else {
					if (W[k].ST <= last + d) {
						if (W[k].ST + t < last + d) {
							ok = false;
							break;
						}
						last = last + d;
						W[k].ND--;
					}
					else {
						last = max(last + d,W[k].ST - t);
						W[k].ND--;
					}
				}
				
			if (ok)
				right = t;
			else
				left = t;
		}
		
		LD res = (left + right) / 2;
		
		res *= 10;
		
		res = round(res);
		
		res /= 10;
		
		cout << setprecision(7) << res << endl;
	}

  	return 0;
}
