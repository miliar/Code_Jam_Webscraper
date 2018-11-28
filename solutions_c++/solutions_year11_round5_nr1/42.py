#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define FOR(i, a, b) for (int i = (a), _n = (b); i <= _n; ++i)
#define FORD(i, a, b) for (int i = (a), _n = (b); i >= _n; --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int PMAX = 400;

const int INF = 1000000000;

struct point {
	int x, y;
};

const int NMAX = 100;

point up[NMAX], down[NMAX];

inline long double cmp_area(long double x1, long double x2, const point& p1, const point& p2) {
	long double y[2];
	REP(i, 2) {
		long double x = i==0 ? x1 : x2, coeff = (x-p1.x) / (p2.x-p1.x);
		y[i] = (1.0-coeff)*p1.y + coeff*p2.y;
	}
	return 0.5*(y[0]+y[1])*(x2-x1);
}

void testcase() {
	int W, L, U, G;
	scanf("%d%d%d%d", &W, &L, &U, &G);
	REP(i, L) scanf("%d%d", &down[i].x, &down[i].y);
	REP(i, U) scanf("%d%d", &up[i].x, &up[i].y);
	
	long double area = 0;
	REP(i, U-1) area += cmp_area(up[i].x, up[i+1].x, up[i], up[i+1]);
	REP(i, L-1) area -= cmp_area(down[i].x, down[i+1].x, down[i], down[i+1]);
	
	REP(ii, G-1) {
		const long double seek = area / G * (ii+1);
		long double left = 0, right = W;
		REP(iter, 200) {
			long double mid = 0.5*(left+right);
			
			long double cmp = 0;
			REP(i, U-1) {
				if (up[i].x > mid) break;
				long double a = up[i].x, b = up[i+1].x;
				b = min(b, mid);
				cmp += cmp_area(a, b, up[i], up[i+1]);
			}
			REP(i, L-1) {
				if (down[i].x > mid) break;
				long double a = down[i].x, b = down[i+1].x;
				b = min(b, mid);
				cmp -= cmp_area(a, b, down[i], down[i+1]);
			}
			
			if (cmp > seek) right = mid;
			else left = mid;
		}
		printf("%.8lf\n", (double)left);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d:\n", i);
		testcase();
	}
}
