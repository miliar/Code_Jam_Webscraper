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
	
		int n;
		
		cin >> n;
		
		vector<PII> V;
		
		REP(i,n) {
			string s;
			int a;
			cin >> s >> a;
			V.PB(MP( (s == "B"),a ));
		}
		
		PII a[2]; // last action, ST - position, ND - time
		
		a[0] = a[1] = MP(1,0);
		
		int t = 0;
		
		REP(i,n) {
			int r = V[i].ST, p = V[i].ND;
			
			t = max(t, a[r].ND + abs(p - a[r].ST)) + 1;
			
			a[r].ST = p;
			a[r].ND = t;
		}
		
		cout << "Case #" << q + 1 << ": " << t << endl;
	}
	

  return 0;
}
