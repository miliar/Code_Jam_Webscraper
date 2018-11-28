#include <iostream>
#include <string.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define REV(a)  ((a) < 0 ? (-(a)) : (a))
#define MAXN 105
#define INF 99999999
using namespace std;

int dp[MAXN][257][257];
int ori[MAXN];
int del, ins, m, n;
int inc (int internal);

int main()
{
	int t, f, i, j, k;
	int tmp1, tmp2, tmp3, tmp, min;
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	cin>>t;
	for (f = 1; f <= t; f++)
	{
		memset (dp, 0, sizeof dp);
		memset (ori, 0, sizeof ori);
		cin>>del>>ins>>m>>n;
		for (i = 0; i < n; i++)
		{
			cin>>ori[i];
		}
		dp[0][256][256] = del;
		for (i = 0; i <= 255; i++)
		{
			tmp1 = REV (ori[0] - i);
			dp[0][256][i] = tmp1;
		}
		for (i = 0; i <= 255; i++)
		{
			for (j = 0; j <= 256; j++)
			{
				dp[0][i][j] = INF;
			}
		}
		for (i = 1; i < n; i++)
		{
			for (j = 0; j <= 256; j++)
			{
				min = INF;
				for (k = 0; k <= 256; k++)
				{
					min = MIN(min, dp[i - 1][k][j]);
				} //got min
				if (j == 256)
				{
					dp[i][256][256] = min + del;
					for (k = 0; k <= 255; k++)
					{
						tmp1 = REV (ori[i] - k);
						dp[i][256][k] = tmp1 + min;
					}
					continue;
				}
				dp[i][j][256] = INF;
				for (k = 0; k <= 255; k++)
				{
					dp[i][j][k] = INF;
					tmp1 = inc (REV (j - k)) + REV(ori[i] - k);
					tmp2 = INF;
					if (k == j)
					{
						tmp2 = del;
					}
					tmp3 = inc (REV (j - k)) + ins + del;
					tmp = MIN(INF, tmp1);
					tmp = MIN(tmp, tmp2);
					tmp = MIN(tmp, tmp3);
					dp[i][j][k] = tmp + min;
				}
			}
		}
		min = INF;
		for (i = 0; i <= 256; i++)
		{
			for (j = 0; j <= 256; j++)
			{
				min = MIN(min, dp[n - 1][i][j]);
			}
		}
		printf("Case #%d: %d\n",f, min);
	}
	return 0;
}

int inc (int internal)
{
	int res = 0;
	if (internal > m)
	{
		if (m != 0)
			res = (internal - 1) / m * ins;
		else
			res = INF;
	}
	return res;
}