#include<stdio.h>

struct
{
	int flag;
	int val;
	int change;
	int op;
}node[10010];

int dp[10010][2];

void changeand( int i , int flag )
{
	int temp;
	if( dp[i+i][0] != -1 && dp[i+i+1][0] != -1 )
	{
		temp = dp[i+i][0] + dp[i+i+1][0] + flag;
		if( temp < dp[i][0] || dp[i][0] == -1 )
			dp[i][0] = temp;
	}
	if( dp[i+i][1] != -1 && dp[i+i+1][0] != -1 )
	{
		temp = dp[i+i][1] + dp[i+i+1][0] + flag;
		if( temp < dp[i][0] || dp[i][0] == -1 )
			dp[i][0] = temp;
	}
	if( dp[i+i][0] != -1 && dp[i+i+1][1] != -1 )
	{
		temp = dp[i+i][0] + dp[i+i+1][1] + flag;
		if( temp < dp[i][0] || dp[i][0] == -1 )
			dp[i][0] = temp;
	}
	if( dp[i+i][1] != -1 && dp[i+i+1][1] != -1 )
	{
		temp = dp[i+i][1] + dp[i+i+1][1] + flag;
		if( temp < dp[i][1] || dp[i][1] == -1 )
			dp[i][1] = temp;
	}
}

void changeor( int i , int flag )
{
	int temp;
	if( dp[i+i][0] != -1 && dp[i+i+1][0] != -1 )
	{
		temp = dp[i+i][0] + dp[i+i+1][0] + flag;
		if( temp < dp[i][0] || dp[i][0] == -1 )
			dp[i][0] = temp;
	}
	if( dp[i+i][1] != -1 && dp[i+i+1][0] != -1 )
	{
		temp = dp[i+i][1] + dp[i+i+1][0] + flag;
		if( temp < dp[i][1] || dp[i][1] == -1 )
			dp[i][1] = temp;
	}
	if( dp[i+i][0] != -1 && dp[i+i+1][1] != -1 )
	{
		temp = dp[i+i][0] + dp[i+i+1][1] + flag;
		if( temp < dp[i][1] || dp[i][1] == -1 )
			dp[i][1] = temp;
	}
	if( dp[i+i][1] != -1 && dp[i+i+1][1] != -1 )
	{
		temp = dp[i+i][1] + dp[i+i+1][1] + flag;
		if( temp < dp[i][1] || dp[i][1] == -1 )
			dp[i][1] = temp;
	}
}

int main()
{
	freopen( "in.txt", "r", stdin);
	freopen("out.txt","w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca=1; ca<=T; ca++ )
	{
		int m;
		int v;
		scanf("%d%d", &m, &v);
		int i;
		for( i=1; i<=(m-1)/2; i++ )
		{
			scanf("%d%d", &node[i].op, &node[i].change);
			node[i].flag = 0;
		}
		for( ; i<=m; i++ )
		{
			scanf("%d", &node[i].val);
			node[i].flag = 1;
		}
		for( i=0; i<=m; i++ )
		{
			dp[i][0] = -1;
			dp[i][1] = -1;
		}
		for( i=m; i>0; i-- )
		{
			if( node[i].flag == 1)
			{
				if( node[i].val == 1 )
				{
					dp[i][0] = -1;
					dp[i][1] = 0;
				}
				else
				{
					dp[i][0] = 0;
					dp[i][1] = -1;
				}
			}
			else
			{
				int temp;
				if( node[i].op == 1 )
				{
					changeand( i , 0);
					if( node[i].change == 1 )
					{
						changeor( i, 1);
					}
				}
				else
				{
					changeor( i, 0);
					if( node[i].change == 1 )
					{
						changeand( i, 1);
					}
				}
			}
		}
		if( dp[1][v] == -1 )
		{
			printf("Case #%d: IMPOSSIBLE\n", ca);
		}
		else
		{
			printf("Case #%d: %d\n", ca, dp[1][v]);
		}
	}
	return 0;
}