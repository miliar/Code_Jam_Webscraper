#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <deque>
#include <string>
#define MAXX 20008

using namespace std;

int ans[MAXX], dp[2][MAXX];
int m, v;
struct Node
{
	bool an , ccge;
};
Node N[MAXX];

void DFS(int now)
{
	int l1, l2, r1, r2;
	if(now * 2 > m)
	{
		dp[ans[now]][now] = 0 ;
		dp[1-ans[now]][now] = -1;
		return ;
	}
	DFS(2*now);
	DFS(2*now+1);
	dp[0][now] = dp[1][now] = INT_MAX;
	l1 = dp[0][2*now];
	l2 = dp[1][2*now];
	r1 = dp[0][2*now+1];
	r2 = dp[1][2*now+1] ;
	if(N[now].an == 1)
	{
		if(l1 != -1 && r1 != -1)
		{
			if(dp[0][now] > l1 + r1)
				dp[0][now] = l1 + r1 ;
		}
		if(l1 != -1 && r2 != -1)
		{
			if(dp[0][now] > l1 + r2)
				dp[0][now] = l1 + r2 ;
		}
		if(l2 != -1 && r1 != -1)
		{
			if(dp[0][now] > l2 + r1)
				dp[0][now] = l2 + r1 ;
		}
		if( l2 != -1 && r2 != -1)
		{
			if(dp[1][now] > l2 + r2)
				dp[1][now] = l2 + r2 ;
		}
	}
	else
	{
		if(l1 != -1 && r1 != -1)
		{
			if(dp[0][now] > l1 + r1)
				dp[0][now] = l1 + r1 ;
		}
		if(l1 != -1 && r2 != -1)
		{
			if(dp[1][now] > l1 + r2)
				dp[1][now] = l1 + r2 ;
		}
		if(l2 != -1 && r1 != -1)
		{
			if(dp[1][now] > l2 + r1)
				dp[1][now] = l2 + r1 ;
		}
		if( l2 != -1 && r2 != -1)
		{
			if(dp[1][now] > l2 + r2)
				dp[1][now] = l2 + r2 ;
		}
	}
	if(N[now].ccge == 1)
	{
		if(N[now].an == 1)
		{
			if(l1 != -1 && r1 != -1)
			{
				if(dp[0][now] > l1 + r1 + 1)
					dp[0][now] = l1 + r1 + 1;
			}
			if(l1 != -1 && r2 != -1)
			{
				if(dp[1][now] > l1 + r2 + 1)
					dp[1][now] = l1 + r2 + 1;
			}
			if(l2 != -1 && r1 != -1)
			{
				if(dp[1][now] > l2 + r1 + 1)
					dp[1][now] = l2 + r1 + 1;
			}
			if( l2 != -1 && r2 != -1)
			{
				if(dp[1][now] > l2 + r2 + 1)
					dp[1][now] = l2 + r2 + 1;
			}
		}
		else
		{
			if(l1 != -1 && r1 != -1)
			{
				if(dp[0][now] > l1 + r1 + 1)
					dp[0][now] = l1 + r1 +1;
			}
			if(l1 != -1 && r2 != -1)
			{
				if(dp[0][now] > l1 + r2 + 1)
					dp[0][now] = l1 + r2 + 1;
			}
			if(l2 != -1 && r1 != -1)
			{
				if(dp[0][now] > l2 + r1 + 1)
					dp[0][now] = l2 + r1+ 1 ;
			}
			if( l2 != -1 && r2 != -1)
			{
				if(dp[1][now] > l2 + r2 + 1)
					dp[1][now] = l2 + r2 + 1;
			}
		}
	}
	if(dp[0][now] == INT_MAX) dp[0][now] = -1;
	if(dp[1][now] == INT_MAX) dp[1][now] = -1;
}
int main(void)
{
	int T, i, j, t = 1, v1, v2;
	//freopen("A-l1rge.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&T);
	while( T -- )
	{
		memset(ans, -1, sizeof(ans));
		scanf("%d%d", &m ,&v);
		for(i = 1; i <= (m - 1)/2 ; i ++)
		{
			scanf("%d%d",&v1, &v2);
			if(v1 == 1) N[i].an = 1;
			else N[i].an = 0;
			if(v2 == 1) N[i].ccge = 1;
			else N[i].ccge = 0;
		}
		for(i = (m - 1) /2 + 1 ; i <= m ; i ++)
			scanf("%d",&ans[i]);
		DFS(1);
		printf("Case #%d: ",t ++);
		if(dp[v][1] == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",dp[v][1]);
	}
	return 0;
}