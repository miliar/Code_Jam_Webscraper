#include <vector>
#include <algorithm>
using namespace std;

#include <stdio.h>

int m;
int v;
int g[22222];
int c[22222];
int val[22222];
int dp[2][22222];

const int INF = 999999;

int Min(int a, int b)
{
	return a<b?a:b;
}

void Read()
{
	int i;

	scanf("%d%d", &m, &v);

	for (i=1; i<=(m-1)/2; i++)
		scanf("%d%d", &g[i], &c[i]);

	for (; i<=m; i++)
		scanf("%d", &val[i]);
}

int DoIt(int dig, int idx)
{
	if(idx > m)
		return INF;

	if(dp[dig][idx] != -1)
		return dp[dig][idx];

	int minVal = INF;
	int l0 = DoIt(0, idx*2);
	int r0 = DoIt(0, idx*2+1);
	int l1 = DoIt(1, idx*2);
	int r1 = DoIt(1, idx*2+1);

	//AND
	if(g[idx] == 1)
	{
		if (dig == 0)
		{
			minVal = Min(minVal, l0+r0);
			minVal = Min(minVal, l0+r1);
			minVal = Min(minVal, l1+r0);
		}
		else
		{
			minVal = Min(minVal, l1+r1);
			if(c[idx] == 1)
			{
				minVal = Min(minVal, l0+r1+1);
				minVal = Min(minVal, l1+r0+1);
			}
		}
	}
	//OR
	else
	{
		if (dig == 1)
		{
			minVal = Min(minVal, l0+r1);
			minVal = Min(minVal, l1+r0);
			minVal = Min(minVal, l1+r1);
		}
		else
		{
			minVal = Min(minVal, l0+r0);
			if(c[idx] == 1)
			{
				minVal = Min(minVal, l0+r1+1);
				minVal = Min(minVal, l1+r0+1);
			}
		}

	}

	dp[dig][idx] = minVal;

	return dp[dig][idx];
}

void Solve()
{
	int i;

	for (i=1; i<=(m-1)/2; i++)
		dp[0][i] = dp[1][i] = -1;
	for (; i<=m*2; i++)
	{
		dp[0][i] = dp[1][i] = INF;
		dp[val[i]][i] = 0;
	}

	int ans = DoIt(v, 1);

//	for (i=1; i<=m; i++)
//		printf("%d %d\n", dp[0][i], dp[1][i]);


	if(ans >= INF)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);

	int t;
	int n;

	scanf("%d", &n);
	for (t=1; t<=n; t++)
	{
		Read();		
		printf("Case #%d: ", t);
		Solve();
	}

	return 0;
}

