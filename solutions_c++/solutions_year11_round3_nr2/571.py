#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
using namespace std;

__int64 L, t, N, C, dis[1005], dp[1005][5];

__int64 go()
{
	memset(dp, 0, sizeof(dp));
	for(__int64 i = 1; i <= N; i++)
	{
		dp[i][0] = dp[i - 1][0] + dis[(i - 1) % C] * 2;	
	}
	

	/*
	for(__int64 i = 0; i <= N; i++)
	{
		printf("%#d %I64d %I64d\n", i, dp[i][0], dp[i][1]);
	}
	*/

	for(__int64 i = 1; i <= N; i++)  for(__int64 j = 1; j <= L; j++)
	{
		dp[i][j] = dp[i - 1][j] + dis[(i - 1) % C] * 2;
		
		__int64 left = t - dp[i - 1][j - 1];
		
		if(left <= 0)	//½¨ºÃÁË
		{
			dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dis[(i - 1) % C]);
		}
		else
		{
			if(left >= dis[(i - 1) % C] * 2)  continue;

			dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + left + (dis[(i - 1) % C] - left / 2));
		}
	}

	__int64 res = -1;
	for(__int64 i = 0; i <= L; i++)
	{
		if(res == -1 || dp[N][i] < res)
			res = dp[N][i];
	}

	/*
	for(__int64 i = 0; i <= N; i++)
	{
		printf("%#d %I64d %I64d\n", i, dp[i][0], dp[i][1]);
	}
	*/

	return res;
}

int main()
{
	freopen("d:\\Desktop\\GCJ\\B-small-attempt0 (1).in", "r", stdin);
	freopen("d:\\Desktop\\GCJ\\B-small-attempt0 (1).out", "w", stdout);
	__int64 T, c = 0;
	scanf("%I64d", &T);
	while(T--)
	{
		printf("Case #%I64d: ", ++c);
		scanf("%I64d%I64d%I64d%I64d", &L, &t, &N, &C);
		for(__int64 i = 0; i < C; i++)
			scanf("%I64d", &dis[i]);
		printf("%I64d\n", go());
	}
}