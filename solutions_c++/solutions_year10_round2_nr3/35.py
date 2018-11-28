#include <cstdio>

typedef long long LL;

const int MD = 100003;

int bn[505][505];
int dp[505][505];

int main() {
	for (int n = 0; n <= 500; ++n) {
		bn[n][0] = 1;
		for (int k = 1; k <= n; ++k) {
			bn[n][k] = (bn[n - 1][k - 1] + bn[n - 1][k]) % MD;
		}
	}
	for (int i = 2; i <= 500; ++i) {
		dp[i][1] = 1;
		for (int j = 2; j <= i - 1; ++j) {
			dp[i][j] = 0;
			for (int s = 1; s <= j - 1; ++s) {
				dp[i][j] = (dp[i][j] + (LL(dp[j][s]) * bn[i - j - 1][j - s - 1])) % MD;
			}
		}
	}
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		int n;
		scanf("%d", &n);
		int res = 0;
		for (int j = 1; j <= n - 1; ++j)
			res = (res + dp[n][j]) % MD;
		printf("Case #%d: %d\n", i, res);
	}
}
