#include <stdio.h>
#include <algorithm>

using namespace std;

const int H = 100003;

int c[501][501];
int dp[501][501];

int dfs (int a, int b)
{
	if (dp[a][b] != -1) return dp[a][b];
	if (b == 1)
		return 1;

	int ans = 0;
	for (int i = 1; i < b; i ++)
		if (a - b - 1 >= b - i - 1)
			ans = (ans + dfs(b,i) * (long long) c[a-b-1][b-i-1]) % H;
	return (dp[a][b] = ans);
}

int main ()
{
	freopen ("c-large.in", "r", stdin);
	freopen ("c-large.out", "w", stdout);

	for (int i = 0; i <= 500; i ++)
	{
		c[i][0] = c[i][i] = 1;
		for (int j = 1; j < i; j ++)
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % H;
		for (int j = 0; j <= 500; j ++)
			dp[i][j] = -1;
	}

	int ct, tt, n;

	tt = 0;
	for (scanf("%d", &ct); ct > 0; ct --)
	{
		scanf ("%d", &n);
		int ans = 0;
		for (int i = 1; i < n; i ++)
			ans = (ans + dfs(n,i)) % H;
		printf ("Case #%d: %d\n", ++ tt, ans);
	}

	return 0;
}