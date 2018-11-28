#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int ntest = 0, test = 0;
inline void init();
inline void run();
inline void stop() {
	ntest = test - 1;
}

int main() {
#ifdef LOCAL
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	init();
	while (++test <= ntest) {
		run();
	}
	return 0;
}

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define FIT(it, v) for (typeof((v).begin())it = (v).begin(); it != (v).end(); it++)

#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SORT(v) sort(ALL(v))
#define GSORT(v) sort(ALL(v), greater<typeof(*(v).begin())>())
#define UNIQUE(v) SORT(v); (v).resize(unique(ALL(v)) - (v).begin())

#define PB push_back
#define MP make_pair
#define F first
#define S second

typedef long long ll;
typedef pair<int, int> pii;

const int INF = (int) 1E9 + 5;
const double EPS = 1E-11;
const ll MOD = (ll) 1E9 + 7;

const int dx[] = { -1, 0, 0, 1 };
const int dy[] = { 0, -1, 1, 0 };

const int MAXN = 105;

int n, s, p, a[MAXN];

inline void init() {
	scanf("%d\n", &ntest);
}

inline int ceilDiv3(int a) {
	return a / 3 + (a % 3 != 0);
}

inline void run() {
	scanf("%d%d%d", &n, &s, &p);
	REP(i, n) {
		scanf("%d", &a[i]);
	}

	sort(a, a + n, greater<int>());

	int cnt = 0;
	REP(i, n) {
		if (ceilDiv3(a[i]) >= p) {
			cnt++;
		} else if (s > 0 && a[i] >= 2) {
			s--;
			if ((a[i] - 2) / 3 + 2 >= p) {
				cnt++;
			}
		}
	}
	printf("Case #%d: %d\n", test, cnt);
}
