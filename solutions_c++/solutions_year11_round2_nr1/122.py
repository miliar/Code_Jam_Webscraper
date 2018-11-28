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
	
	REP(q,Q) {
	
		cout << "Case #" << q + 1 << ":\n";
	
		int n;
		
		cin >> n;
	
		vector<string> V(n);
		
		REP(i,n)
			cin >> V[i];
			
		VI pl(n), win(n);
		
		REP(i,n) {
			pl[i] = win[i] = 0;
			REP(j,n) {
				pl[i]++;
				if (V[i][j] == '.')
					pl[i]--;
				else if (V[i][j] == '1')
					win[i]++;
			}
		}
			
		vector<LD> wp(n), owp(n,0), oowp(n,0);
		
		 REP(i,n)
		 	wp[i] = LD(win[i]) / LD(pl[i]);
		 	
		 REP(i,n)  {
		 	REP(j,n)
		 		if (V[i][j] == '1')
		 			owp[i] += LD(win[j]) / LD(pl[j] - 1);
		 		else if (V[i][j] == '0')
		 			owp[i] += LD(win[j] - 1) / LD(pl[j] - 1);
		 	owp[i] /= LD(pl[i]);
		}
		
		REP(i,n) {
			REP(j,n)
				if (V[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= LD(pl[i]);
		}
		
		REP(i,n)
			cout << setprecision(10) <<  0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl; 
	
	}

  	return 0;
}
