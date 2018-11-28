#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 10000;
int dp[MAXN];
int d[MAXN], len[MAXN];
int main() {
	int t, n, D;
	bool r;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d", &n);
		r = false;
		memset(dp, -1, sizeof(dp));
		for (int j = 0; j != n; ++j) {
			scanf("%d%d", d + j, len + j);
		}
		scanf("%d", &D);
		dp[0] = d[0];
		for (int j = 0; j != n; ++j) {
			if (dp[j] > 0) {
				if (d[j] + dp[j] >= D) {
					r = true;
					break;
				}
				for (int k = j + 1; k < n; ++k) {
					if (d[j] + dp[j] < d[k]) break;
					dp[k] = max(dp[k], min(d[k] - d[j], len[k]));
				}
			}
		}
		printf("Case #%d: %s\n", i, r?"YES":"NO");
	}
	return 0;
}