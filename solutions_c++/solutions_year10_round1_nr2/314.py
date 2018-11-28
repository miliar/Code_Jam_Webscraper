#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int max_n = 105;
const int oo = 1000000000;

int d, p, m, n, a[max_n], dp[max_n][256];

int change(int x, int y) {
	if (m == 0 && x != y)
		return oo;
	int ret = 0;
	while (abs(x - y) > m) {
		ret += p;
		if (x < y) {
			x += m;
		}
		else {
			y += m;
		}
	}
	return ret;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testID = 1;testID <= test;testID++) {
		scanf("%d %d %d %d", &d, &p, &m, &n);
		for (int i = 0;i < n;i++)
			scanf("%d", &a[i]);
		for (int i = 0;i < n;i++) {
			for (int j = 0;j < 256;j++) {
				dp[i][j] = oo;
			}
		}
		for (int i = 0;i < 256;i++)
			dp[0][i] = abs(a[0] - i);
		for (int i = 1;i < n;i++) {
			for (int k = 0;k < 256;k++) {
				for (int j = 0;j < i;j++) {
					for (int l = 0;l < 256;l++) {
						dp[i][k] = min(dp[i][k], dp[j][l] + change(k, l) + (i - j - 1) * d + abs(k - a[i]));
					}
				}
			}
		}
		int ans = n * d;
		for (int i = 0;i < n;i++) {
			for (int j = 0;j < 256;j++) {
				ans = min(ans, dp[i][j] + (n - i - 1) * d);
			}
		}
		printf("Case #%d: %d\n", testID, ans);
	}
	return 0;
}
