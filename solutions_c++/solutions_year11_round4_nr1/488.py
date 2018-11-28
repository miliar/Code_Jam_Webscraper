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
	
	int T;
	
	cin >> T;
	
	REP(q,T) {
	
		cout << "Case #" << q + 1 << ": ";
	
		LD x,S,R,t,n;
		
		cin >> x >> S >> R >> t >> n;
		
		vector<pair<int,PII> > V(n);
		
		REP(i,n)
			cin >> V[i].ND.ST >> V[i].ND.ND >> V[i].ST;
			
		LD res = 0;
		
		LD len = 0;
		
		FORE(it,V)
			len += it->ND.ND - it->ND.ST; //cout << x - len << " " ;
			
		V.PB(MP(0,MP(0,x - len)));
		
		sort(ALL(V));
		
		//reverse(ALL(V));
			
		FORE(it,V) {
		
			LD d = it->ND.ND - it->ND.ST, w = it->ST;
			
			bool done = false;
			
			if (t != 0) {
			
				if ( d > (R + w) * t) {
					res += t;
					d -= (R + w) * t;
					t = 0;
				}
				else {
					t -= d / (R + w);
					res += d / (R + w);
					done = true;
				}
			}
			
			if (!done)
				res += d / (S + w);
		}
	
		cout << setprecision(10) << res << endl;
	
	}

  	return 0;
}
