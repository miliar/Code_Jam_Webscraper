#include <iostream>
#include <string.h>
#include <stdio.h>
#define MAXN 15
using namespace std;
int dp[2][MAXN];

int main()
{
	int t, n, k, r, i, j, f;
	int sum, num, s, tmp, gold;

	freopen ("C-small.in","r", stdin);
	freopen ("C-small.out","w", stdout);

	cin>>t;
	for (f = 1; f <= t; f++)
	{
		gold = 0;
		cin>>r>>k>>n;
		for (i = 0; i < n; i++)
		{
			scanf("%d", &dp[0][i]);
		}
		for (s = 0; s < r; s++)
		{
			tmp = num = sum = 0;
			for (tmp = 0; tmp < n; tmp++)
			{
				if (sum + dp[s % 2][tmp] <= k)
				{
					sum += dp[s % 2][tmp];
					num++;
				}
				else
				{
					break;
				}
			}
			if (num == 0)
			{
				break;
			}
			gold += sum;
			for (j = tmp; j < n; j++)
			{
				dp[(s + 1) % 2][j - tmp] = dp[s % 2][j];
			}
			for (j = 0; j < tmp; j++)
			{
				dp[(s + 1) % 2][n - tmp + j] = dp[s % 2][j];
			}
		}
		printf("Case #%d: %d\n", f, gold);
	}
	return 0;
}