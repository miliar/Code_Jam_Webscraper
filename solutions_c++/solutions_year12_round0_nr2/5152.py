#define FILEIO

#define INPUT "in"
#define OUTPUT "out"

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <vector>
#include <cassert>

#define mp make_pair
#define pb push_back
#define foreach(i,T) for(__typeof(T.begin()) i = T.begin(); i != T.end(); ++i)

using namespace std;

namespace Solve {
	const int MAXN = 202;

	int t, n, s, p;

	inline int Cal(int s, int d) {
		int ret = 0;
		if (s % 3 == 0) ret = s / 3;
		if (s - d > 0 && (s - d) % 3 == 0) ret = max((s + 2 * d) / 3, ret);
		if ((s + d) % 3 == 0) ret = max((s + d) / 3, ret);
		if (s % 3 == 0 && d == 2 && s != 0)
			ret = max(ret, s / 3 + 1);
		return ret;
	}

	inline void solve(void) {
		int T; scanf("%d", &T);
		for (int i = 1; i <= T; i++) {
			printf("Case #%d: ", i);
			scanf("%d%d%d", &n, &s, &p);
			fprintf(stderr, "%d %d %d\n", n, s, p);
			int ret = 0;
			for (int j = 1; j <= n; j++) {
				scanf("%d", &t);
				if (Cal(t, 1) >= p)
					ret++;
				else if (s && Cal(t, 2) >= p)
					s--, ret++;
			}
			printf("%d\n", ret);
		}
	}
}

int main(void) {
	#ifdef FILEIO
		freopen(INPUT, "r", stdin);
		freopen(OUTPUT, "w", stdout);
	#endif
	Solve::solve();
	return 0;
}
