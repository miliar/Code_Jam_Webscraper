#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int INF = 1000000000;

int dp[1 << 10][11][12];
int price[1 << 10][10];

int p;

void alg() {
	memset(price, 0, sizeof(price));
	scanf("%d", &p);
	for (int i = 0; i < (1 << p); ++i) {
		for (int j = 0; j <= p; ++j) {
			for (int k = 0; k <= p + 1; ++k) {
				dp[i][j][k] = INF;
			}
		}
	}
	for (int i = 0; i < (1 << p); ++i) {
		int m;
		scanf("%d", &m);
		while (m >= 0)
			dp[i][p][m--] = 0;
	}
	for (int i = p - 1; i >= 0; --i) {
		for (int j = 0; j < (1 << i); ++j) {
			scanf("%d", &price[j][i]);
		}
	}
	for (int len = p - 1; len >= 0; --len) {
		for (int i = 0; i < (1 << len); ++i) {
			for (int m = 0; m <= p; ++m) {
				dp[i][len][m] = min(dp[i * 2][len + 1][m + 1] + dp[i * 2 + 1][len + 1][m + 1],
									dp[i][len][m]);
				dp[i][len][m] = min(dp[i * 2][len + 1][m] + dp[i * 2 + 1][len + 1][m] + price[i][len],
									dp[i][len][m]);
			}
		}
	}
	int res = INF;
	for (int i = 0;	i <= p; ++i)
		res = min(res, dp[0][0][i]);
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
