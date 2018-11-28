#include <stdio.h>

int n;
int data[1024];
int price[10][512];
int dp[10][512][11];

int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t, ct = 0;

	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d", &n);
		for (int i = 0; i < (1 << n); i ++)
			scanf ("%d", data + i);

		for (int i = 0; i < n; i ++)
			for (int j = 0; j < (1 << (n - 1 - i)); j ++)
				scanf ("%d", price[i] + j);

#define modify(a,b) ((a)=((a)<(b)?(a):(b)))
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < (1 << (n - 1 - i)); j ++)
				for (int k = n; k >= 0; k --)
				{
					if (i == 0)
					{
						dp[i][j][k] = 1000000000;
						if (k + 1 <= n)
							modify(dp[i][j][k],dp[i][j][k + 1]);
						if (k == (data[j * 2] < data[j * 2 + 1]? data[j * 2] : data[j * 2 + 1]))
							modify(dp[i][j][k],price[i][j]);
						if (k < (data[j * 2] < data[j * 2 + 1]? data[j * 2] : data[j * 2 + 1]))
							modify(dp[i][j][k],0);
					}
					else
					{
						dp[i][j][k] = 1000000000;
						if (k + 1 <= n)
							modify(dp[i][j][k],dp[i][j][k + 1]);
						modify(dp[i][j][k], dp[i-1][j*2][k] + dp[i-1][j*2+1][k] + price[i][j]);
						if (k + 1 <= n)
							modify(dp[i][j][k], dp[i-1][j*2][k + 1] + dp[i-1][j*2+1][k + 1]);
					}
				}

		printf ("Case #%d: %d\n", ++ct, dp[n - 1][0][0]);
	}

	return 0;
}