#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int dp[3000][12];
int price[3000];
int a[3000];
const int inf = 1000000000;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d", &n);
		int start = 1;
		for (int i = 0; i < n; ++i)
			start *= 2;
		int end = start * 2;
		for (int i = start; i < end; ++i)
			scanf("%d", &a[i]);
		int tmp = start >> 1;
		while (tmp) {
			int tt = tmp * 2;
			for (int i = tmp; i < tt; ++i)
				scanf("%d", &price[i]);
			tmp >>= 1;
		}
		for (int i = 0; i < 3000; ++i)
			for (int j = 0; j < 12; ++j)
				dp[i][j] = inf;
		for (int i = start; i < end; ++i) {
			dp[i][n - a[i]] = 0;
		}
		for (int i = start - 1; i >= 1; --i) {
			int sub1 = i * 2;
			int sub2 = sub1 + 1;
			for (int j = 0; j <= n; ++j) {
				for (int k = 0; k <= n; ++k) {
					dp[i][max(j, k)] = min(dp[i][max(j, k)], dp[sub1][j] + dp[sub2][k]);
					if (j || k)
						dp[i][max(j, k) - 1] = min(dp[i][max(j, k) - 1], dp[sub1][j] + dp[sub2][k] + price[i]);
				}
			}
		}
		printf("Case #%d: %d\n", t, dp[1][0]);
	}
	return 0;
}