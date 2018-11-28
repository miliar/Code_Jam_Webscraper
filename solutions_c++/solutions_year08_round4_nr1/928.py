#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

struct Node
{
	int G;
	int C;
};

Node node[10001];
int leaf[10001];
int dp[10001][2];
int M, V;

int min(int x,int y)
{
    return x<y?x:y;
}

int min(int a,int b,int c)
{
	return min(a,b<c?b:c);
}

void dfs(int x)
{
	if (x>(M-1)/2)
	{
		dp[x][leaf[x]]=0;
		dp[x][1-leaf[x]]=20000;
	}
	else
	{
		dfs(x*2);
        dfs(x*2+1);
		if (node[x].C==0)
		{
			if (node[x].G==1)
			{
				dp[x][0]=min(dp[x*2][0]+dp[x*2+1][0],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0]);
				dp[x][1]=dp[x*2][1]+dp[x*2+1][1];
			}
			else
			{
				dp[x][1]=min(dp[x*2][1]+dp[x*2+1][1],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0]);
				dp[x][0]=dp[x*2][0]+dp[x*2+1][0];
			}
		}
		else
		{
			if (node[x].G==1)
			{
				dp[x][0]=min(min(dp[x*2][0]+dp[x*2+1][0],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0]),dp[x*2][0]+dp[x*2+1][0]+1);
				dp[x][1]=min(dp[x*2][1]+dp[x*2+1][1],min(dp[x*2][1]+dp[x*2+1][1],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0])+1);
			}
			else
			{
				dp[x][1]=min(min(dp[x*2][1]+dp[x*2+1][1],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0]),dp[x*2][1]+dp[x*2+1][1]+1);
				dp[x][0]=min(dp[x*2][0]+dp[x*2+1][0],min(dp[x*2][0]+dp[x*2+1][0],dp[x*2][0]+dp[x*2+1][1],dp[x*2][1]+dp[x*2+1][0])+1);
			}	
		}
	}
}

int main()
{
	int t,ct=0;
	scanf("%d", &t);
	while (t--)
	{
		memset(dp,0,sizeof(dp));
		scanf("%d%d",&M,&V);
		for (int i=1;i<=(M-1)/2;i++)
			scanf("%d%d",&node[i].G,&node[i].C);
		for (int i=(M-1)/2+1;i<=M;i++)
			scanf("%d",&leaf[i]);
		dfs(1);
		if (dp[1][V]>=20000)
			printf("Case #%d: IMPOSSIBLE\n",++ct);
		else
			printf("Case #%d: %d\n",++ct,dp[1][V]);
	}
	return 0;
}
