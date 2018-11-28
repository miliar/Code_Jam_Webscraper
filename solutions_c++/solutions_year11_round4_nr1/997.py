// Some algorithmic problem solution by Artem Khizha [DNU2] (also known as metar)

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

const int MAXN = 1e6 + 1;

int main() {
	int tnum;
	int v[MAXN];
	cin >> tnum;
	REP(ti,tnum) {
		//cerr << ti+1 << endl;
		ld ans = 0.0;
		int x, s, r, n;
		ld t;
		cin >> x >> s >> r >> t >> n;
		for (int i = 0; i < x; ++i)
			v[i] = 0;
		REP(i,n) {
			int a, b, c;
			cin >> a >> b >> c;
			for (int j = a; j < b; ++j)
				v[j] = c;
		}
		sort(v, v+x);
		for (int i = 0; i < x; ++i) {
			if (t > 0) {
				if ((r+v[i])*t >= 1) {
					ans += 1.0/(r+v[i]);
					t -= 1.0/(r+v[i]);
				} else {
					ans += (1.0-(r+v[i])*t)/(s+v[i]);
					ans += t;
					t = 0;
				}
			} else {
				ans += 1.0/(s+v[i]);
			}
		}
		printf("Case #%d: %.6Lf\n", 1+ti, ans);
	}
	return 0;
}