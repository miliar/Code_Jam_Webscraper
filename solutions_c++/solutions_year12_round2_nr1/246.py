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

const LD EPS = 1e-9;

int main() {
  	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);

	int T;
	
	cin >> T;

	REP(q,T) {
		cout << "Case #" << q + 1 << ":";

		int n;

		cin >> n;

		VI V(n);

		REP(i,n)
		    cin >> V[i];

		int X = 0;

		REP(i,n)
		    X += V[i];

		REP(j,n) {

		    LD left = 0, right = 1;

		    REP(v,100) {
			LD s = (left + right) / 2;
			LD score = LD(V[j]) + LD(X) * s;
			LD sm = 0;
			REP(i,n)
			    if (i != j)
				sm += max((score - LD(V[i])) / LD(X), 0.0);
			if (sm < 1.0 - s)
			    left = s;
			else
			    right = s;
		    }

		    cout << setprecision(10) << " " << left * 100;
		}

		cout << endl;

	}


  	return 0;
}	
