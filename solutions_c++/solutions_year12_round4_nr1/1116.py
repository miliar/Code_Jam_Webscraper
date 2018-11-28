#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 10010;

int cas, n, d[MAXN], l[MAXN], dp[MAXN], D;

int main() {
	scanf("%d", &cas);
	for (int ca = 1; ca <= cas; ++ca) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &D);
		memset(dp, -1, sizeof(dp));
		dp[0] = min(d[0], l[0]);
		for (int i = 0; i < n; ++i) {
			if (dp[i] > 0) {
				for (int j = i + 1; j < n; ++j) {
					if (dp[i] >= d[j] - d[i])
						dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
				}
			}
		}
		bool ok = false;
		for (int i = 0; i < n; ++i) {
			if (d[i] + dp[i] >= D)
				ok = true;
		}
		printf("Case #%d: %s\n", ca, ok ? "YES" : "NO");
	}
	return 0;
}

