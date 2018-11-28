#include <cstdio>
#include <cstring>

using namespace std;

int m[1 << 10];
int a[520][520];
int dp[600][600][12];

inline int max(int a, int b) {
	if (a > b) {
		return a;
	} else {
		return b;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n, N;
		scanf("%d", &n);
		N = 1 << n;
		for (int i = 0; i < N; i++) {
			scanf("%d", &m[i]);
			m[i] = n - m[i];
		}
		for (int i = 1; i <= n; i++) {
			int t = N >> i;
			for (int j = 0; j < t; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		int res = 0x3f3f3f3f;
		memset(dp, 0x3f, sizeof(dp));
		for (int i = 0; i < N / 2; i++) {
			int t = max(m[i * 2], m[i * 2 + 1]);
			dp[1][i][t] = 0;
			if (t > 0) {
				dp[1][i][t - 1] = a[1][i];
			}
		}
		for (int i = 2; i <= n; i++) {
			int t = N >> i;
			for (int j = 0; j < t; j++) {
				for (int k = 0; k <= n; k++) {
					for (int l = 0; l <= n; l++) {
						int tt = dp[i - 1][j * 2][k] + dp[i - 1][j * 2 + 1][l];
						if (tt < dp[i][j][max(k, l)]) {
							dp[i][j][max(k, l)] = tt;
						}
						tt += a[i][j];
						if (tt < dp[i][j][max(k, l) - 1]) {
							dp[i][j][max(k, l) - 1] = tt;
						}
					}
				}
			}
		}
		res = dp[n][0][0];
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
