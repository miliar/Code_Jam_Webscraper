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
	        cout << "Case #" << q + 1 << ":" << endl;

		int n;
		cin >> n;
		VI V(n);
		REP(i,n)
		    cin >> V[i];

		map<int,int> M;

		bool found = false;

		FOR(msk,1, (1 << n) - 1) {
		    LL sm = 0;
		    REP(i,20)
			if (msk & (1 << i))
			    sm += V[i];
		    
		    if (M[sm] != 0) {
			int msk2 = M[sm];
			REP(i,20)
			    if (msk2 & (1 << i))
				cout << V[i] << " ";
			cout << endl;
			REP(i,20)
			    if (msk & (1 << i))
				cout << V[i] << " ";
			cout << endl;
			found = true;
			break;
		    }
		    M[sm] = msk;
		}

		if (!found)
		    cout << "Impossible\n";

	}


  	return 0;
}	
