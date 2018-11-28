#include <cstdio>

int abs(int x) {
	return x < 0 ? -x : x;
}

int T, a, b, m, n, d[100], dp[101][256], ans;

int f(int x) {
	if (x < 0) x = -x;
	if (x == 0) return 0;
	if (m == 0) return 1 << 25;
	return (x - 1)/m*b;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d%d%d", &a, &b, &m, &n);
		for (int i = 0; i < n; ++i) scanf("%d", d + i);
		for (int i = 0; i < 256; ++i) dp[0][i] = 0;
		for (int i = 1; i <= n; ++i)
			for (int j = 0; j < 256; ++j) {
				dp[i][j] = dp[i - 1][j] + a;
				for (int k = 0; k < 256; ++k)
					if (abs(d[i - 1] - k) + dp[i - 1][k] + f(k - j) < dp[i][j])
						dp[i][j] = abs(d[i - 1] - k) + dp[i - 1][k] + f(k - j);
			}
		ans = 1 << 30;
		for (int i = 0; i < 256; ++i) if (dp[n][i] < ans) ans = dp[n][i];
		printf("%d\n", ans);
	}
	return 0;
}
