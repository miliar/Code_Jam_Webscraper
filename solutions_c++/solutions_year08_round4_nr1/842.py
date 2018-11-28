#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 10000 + 10;

int m, v;
int canchange[MAXN];
int type[MAXN];
int dp[MAXN][2];

int better(int a, int b)
{
	if (a < 0) return b;
	if (b < 0) return a;
	return min(a, b);
}

void run(int t)
{
	scanf("%d %d", &m, &v);
	int half = m / 2;
	int left = m - half;
	int i;
	for (i = 0; i < half; ++i) {
		scanf("%d %d", type + i, canchange + i);
	}
	memset(dp, -1, sizeof(dp));
	for (; i < m; ++i) {
		scanf("%d", type + i);
		dp[i][type[i]] = 0;
	}
	for (int i = left - 1; i >= 0; --i) {
		int l = (i + 1) * 2 - 1, r = (i + 1) * 2;
		if (type[i] == 1) {
			if (dp[l][0] != -1 && dp[r][0] != -1) {
				dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][0]);
			}
			if (dp[l][1] != -1 && dp[r][0] != -1) {
				dp[i][0] = better(dp[i][0], dp[l][1] + dp[r][0]);
			}
			if (dp[l][0] != -1 && dp[r][1] != -1) {
				dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][1]);
			}
			if (dp[l][1] != -1 && dp[r][1] != -1) {
				dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][1]);
			}
		}
		else {
			if (dp[l][0] != -1 && dp[r][0] != -1) {
				dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][0]);
			}
			if (dp[l][1] != -1 && dp[r][0] != -1) {
				dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][0]);
			}
			if (dp[l][0] != -1 && dp[r][1] != -1) {
				dp[i][1] = better(dp[i][1], dp[l][0] + dp[r][1]);
			}
			if (dp[l][1] != -1 && dp[r][1] != -1) {
				dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][1]);
			}
		}
		if (canchange[i]) {
			if (type[i] == 1) {
				if (dp[l][0] != -1 && dp[r][0] != -1) {
					dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][0] + 1);
				}
				if (dp[l][1] != -1 && dp[r][0] != -1) {
					dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][0] + 1);
				}
				if (dp[l][0] != -1 && dp[r][1] != -1) {
					dp[i][1] = better(dp[i][1], dp[l][0] + dp[r][1] + 1);
				}
				if (dp[l][1] != -1 && dp[r][1] != -1) {
					dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][1] + 1);
				}
			}
			else {
				if (dp[l][0] != -1 && dp[r][0] != -1) {
					dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][0] + 1);
				}
				if (dp[l][1] != -1 && dp[r][0] != -1) {
					dp[i][0] = better(dp[i][0], dp[l][1] + dp[r][0] + 1);
				}
				if (dp[l][0] != -1 && dp[r][1] != -1) {
					dp[i][0] = better(dp[i][0], dp[l][0] + dp[r][1] + 1);
				}
				if (dp[l][1] != -1 && dp[r][1] != -1) {
					dp[i][1] = better(dp[i][1], dp[l][1] + dp[r][1] + 1);
				}
			}
		}
	}
	printf("Case #%d: ", t);
	if (dp[0][v] == -1) {
		puts("IMPOSSIBLE");
	}
	else {
		printf("%d\n", dp[0][v]);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		run(i);
	}
	return 0;
}