#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[52][52];

int x[51];
int v[51];

void alg() {
	int n, K, b, t;
	scanf("%d %d %d %d", &n, &K, &b, &t);
	for (int i = 1; i <= n; ++i)
		scanf("%d", &x[i]);
	for (int i = 1; i <= n; ++i)
		scanf("%d", &v[i]);
	for (int i = 1; i <= n; ++i)
		dp[n + 1][i] = n * n + 1;
	dp[n + 1][0] = 0;
	int res = n * n + 1;
	if (K == 0)
		res = 0;
	for (int i = n; i >= 1; --i) {
		dp[i][0] = 0;
		for (int k = 1; k <= n; ++k) {
			dp[i][k] = n * n + 1;
			if ((b - x[i]) > t * v[i])
				continue;
			if (k > n + 1 - i)
				continue;
			for (int j = i + 1; j <= n + 1; ++j) {
				dp[i][k] = min(dp[i][k], dp[j][k - 1] + (n + 1 - i) - k);
			}
			if (k >= K)
				res = min(res, dp[i][k]);
		}
	}
	if (res > n * n)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", res);
}

int main() {
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		printf("Case #%d: ", i);
		alg();
	}
}
