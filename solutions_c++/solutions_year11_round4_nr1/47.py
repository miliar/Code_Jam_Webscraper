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

const double EPS = 1e-10;

const int INF = 1000000000;

const int NMAX = 1000;

struct walkway {
	double len, w;
};
bool operator <(const walkway& w1, const walkway& w2) {
	return w1.w < w2.w;
}

walkway W[5*NMAX];

void testcase() {
	int X, S, R, _t, N;
	scanf("%d%d%d%d%d", &X, &S, &R, &_t, &N);
	int totlen = 0;
	REP(i, N) {
		int B, E, w;
		scanf("%d%d%d", &B, &E, &w);
		W[i].len = E-B;
		W[i].w = w+S;
		totlen += E-B;
	}
	if (totlen != X) {
		W[N].len = X-totlen;
		W[N++].w = S;
	}
	
	sort(W, W+N);

	double res = 0, t = _t;
	R -= S;
	for (int ind = 0; ind < N; ) {
//printf("ind=%d len=%lf v=%lf res=%lf\n", ind, W[ind].len, W[ind].w, res);
		if (t > EPS) {
			double tprim = 1.0 * W[ind].len / (W[ind].w + R);
			if (tprim >= t) {
				res += t;
				W[ind].len -= t * (W[ind].w+R);
				t = 0;
			} else {
				res += tprim;
				t -= tprim;
				++ind;
				continue;
			}
		}
		res += W[ind].len / W[ind].w;
		++ind;
	}
	printf("%.7lf\n", res);
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
