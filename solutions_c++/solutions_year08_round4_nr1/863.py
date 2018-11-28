#include <stdio.h>
#include <limits>

#define min(a, b) ((a) < (b) ? (a) : (b))

const double inf = std::numeric_limits<double>::infinity();

int m, v;

double dp[11000][2];
int g[11000], c[11000];
int inter;

void solve()
{
	scanf("%d%d", &m, &v);
	inter = (m - 1) / 2;
	int i;
	for (i = 1; i <= inter; ++i)
		scanf("%d %d", g + i, c + i);
	for (; i <= m; ++i)
		scanf("%d", g + i);
	for (int i = inter + 1; i <= m; ++i) {
		dp[i][g[i]] = 0;
		dp[i][1 - g[i]] = inf;
	}
	for (int i = inter; i > 0; --i) {
		dp[i][0] = dp[i][1] = inf;
		if (g[i]) {
			dp[i][0] = min(dp[i * 2][0] + dp[i * 2 + 1][1], dp[i * 2][1] + dp[i * 2 + 1][0]);
			dp[i][0] = min(dp[i][0], dp[i * 2][0] + dp[i * 2 + 1][0]);
			dp[i][1] = dp[i * 2][1] + dp[i * 2 + 1][1];
		} else {
			dp[i][0] = dp[i * 2][0] + dp[i * 2 + 1][0];
			dp[i][1] = min(dp[i * 2][0] + dp[i * 2 + 1][1], dp[i * 2][1] + dp[i * 2 + 1][0]);
			dp[i][1] = min(dp[i][1], dp[i * 2][1] + dp[i * 2 + 1][1]);
		}
		if (c[i]) {
			if (!g[i]) {
			dp[i][0] = min(dp[i][0], min(dp[i * 2][0] + dp[i * 2 + 1][1] + 1, dp[i * 2][1] + dp[i * 2 + 1][0] + 1));
			dp[i][0] = min(dp[i][0], dp[i * 2][0] + dp[i * 2 + 1][0] + 1);
			dp[i][1] = min(dp[i][1], dp[i * 2][1] + dp[i * 2 + 1][1]);
			} else {
				dp[i][0] = min(dp[i][0], dp[i * 2][0] + dp[i * 2 + 1][0]);
				dp[i][1] = min(dp[i][1], 1 + min(dp[i * 2][0] + dp[i * 2 + 1][1], dp[i * 2][1] + dp[i * 2 + 1][0]));
				dp[i][1] = min(dp[i][1], 1 + dp[i * 2][1] + dp[i * 2 + 1][1]);
			}
		}
	}
	printf(dp[1][v] == inf ? "IMPOSSIBLE\n" : "%.0llf\n", dp[1][v]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n; scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
}