#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 0x3f3f3f3f;

int D, I, m, n;
int a[105];
int dp[105][260];

int run() {
	for (int i = 0; i < 256; i++) {
		dp[0][i] = min(abs(a[0] - i), D);
	}
	for (int i = 0; i < 256; i++) {
		if (m == 0) {
			continue;
		}
		for (int j = i + 1; j < 256; j++) {
			int t = (j - i - 1) / m + 1;
			dp[0][j] = min(dp[0][j], dp[0][i] + t * I);
			dp[0][j] = min(dp[0][j], dp[0][i] + t * m);
		}
		for (int j = i - 1; j >= 0; j--) {
			int t = (i - j - 1) / m + 1;
			dp[0][j] = min(dp[0][j], dp[0][i] + t * I);
			dp[0][j] = min(dp[0][j], dp[0][i] + t * m);
		}
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < 256; j++) {
			for (int k = j - m; k <= j + m; k++) {
				if (k < 0 || k >= 256) {
					continue;
				}
				dp[i][j] = min(dp[i][j], dp[i - 1][k]);
			}
			dp[i][j] += abs(a[i] - j);
		}
		for (int j = 0; j < 256; j++) {
			if (m == 0) {
				continue;
			}
			for (int k = j + 1; k < 256; k++) {
				int t = (k - j - 1) / m + 1;
				dp[i][k] = min(dp[i][k], dp[i][j] + t * I);
				dp[i][k] = min(dp[i][k], dp[i][j] + t * m);
			}
			for (int k = j - 1; k >= 0; k--) {
				int t = (j - k - 1) / m + 1;
				dp[i][k] = min(dp[i][k], dp[i][j] + t * I);
				dp[i][k] = min(dp[i][k], dp[i][j] + t * m);
			}
		}
		for (int j = 0; j < 256; j++) {
			dp[i][j] = min(dp[i][j], dp[i - 1][j] + D);
		}
	}
/*	for (int i = 0; i < 3; i++) {
		for (int j = 0; j <= 50; j++) {
			printf("%3d ", dp[i][j]);
		}
		printf("\n");
	}*/
	int ret = INF;
	for (int i = 0; i < 256; i++) {
		ret = min(ret, dp[n - 1][i]);
	}
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d%d%d", &D, &I, &m, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", a + i);
		}
		memset(dp, 0x3f, sizeof(dp));
		printf("Case #%d: %d\n", cas, run());
	}
	return 0;
}
