#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 110;
int dp[N][N], a[N][2];

int f1(int x) {
	int res = x / 3;
	return (res * 3 == x ? res : res + 1);
}

int f2(int x) {
	if (x < 2) return -1;
	return (x - 2) / 3 + 2;
}

int main() {
	int tt, n, k, p, x;
	scanf("%d", &tt);
	for (int cas = 1; cas <= tt; cas++) {
		scanf("%d%d%d", &n, &k, &p);
		for (int i = 0; i < n; i++) {
			scanf("%d", &x);
			a[i][0] = (f1(x) >= p);
			a[i][1] = (f2(x) >= p);
		}
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i < n; i++)
			for (int j = 0; j <= i; j++) {
				dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a[i][0]);
				dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i][1]);
			}
		printf("Case #%d: %d\n", cas, dp[n][k]);
	}
}
