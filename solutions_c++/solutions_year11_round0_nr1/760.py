#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

int main() {
	int tn;
	cin >> tn;
	REP(ti,tn) {
		int n;
		int ot = 0, bt = 0, tt = 0;
		int op = 1, bp = 1;
		cin >> n;
		REP(i,n) {
			char c;
			int  p;
			cin >> c >> p;
			if (c == 'O') {
				int cost = abs(p-op)+1;
				ot += cost;
				op = p;		
				tt = (ot <= tt)? tt+1 : ot;
				ot = tt;
			} else if (c == 'B') {
				int cost = abs(p-bp)+1;
				bt += cost;
				bp = p;				
				tt = (bt <= tt)? tt+1 : bt;
				bt = tt;
			}
			//printf("%d %d\n", ot, bt);
		}
		printf("Case #%d: %d\n", ti+1, tt);
	}
	return 0;
}

