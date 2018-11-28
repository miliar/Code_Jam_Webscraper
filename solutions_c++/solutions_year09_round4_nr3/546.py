#include <stdio.h>
#include <string.h>

const int M = 110;
bool canmatch[M][M];

int q[M][M];
int qin[M];
int n,m;
int flag[M];
int min;

void search( int cur, int from)
{
	int i,j;
	if( from == 0 )
	{
		for( i = 1; i <= n; i++ )
		{
			if( flag[i] == 1 )
				continue;
			for( j = 1; j <=n; j ++ )
			{
				if( flag[j] == 1 )
					continue;
				if( canmatch[j][i] == 1 )
					break;
			}
			if( j == n+1) 
				break;
		}
		if( i == n + 1 )
		{
			if( cur < min )
			{
				min = cur;
			}
			return;
		}
		else
		{
			flag[i] = 1;
			search(cur, i);
			flag[i] = 0;
		}
	}
	else
	{
		int sb = 1;
		for( i = 1; i <= n; i ++ )
		{
			if( flag[i] == 1 )
				continue;
			if( canmatch[from][i] == 1 )
			{
				sb = 0;
				flag[i] = 1;
				search( cur, i);
				flag[i] = 0;
			}
		}
		if( sb == 1 )
		{
			search(cur+1, 0);
		}
	}
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("31.out","w", stdout);
	int T;
	int ca;
	scanf("%d", &T);
	
	int i,j,k;
	for( ca = 1; ca <= T; ca ++ )
	{
		min =  9999;
		scanf("%d%d", &n, &m);
		for( i = 1 ; i<= n; i ++ )
		{
			for( j = 1; j <= m; j ++ )
			{
				scanf("%d", &q[i][j]);
			}
		}
		for( i = 1; i <= n; i ++ )
		{
			for( j = 1; j <= n; j ++ )
			{
				for( k = 1; k <= m; k ++ )
				{
					if( q[i][k] >= q[j][k])
						break;
				}
				if( k == m + 1 )
				{
					canmatch[i][j] = 1;
				}
				else
				{
					canmatch[i][j] = 0;
				}
			}
			
		}
		for( i = 1; i<=n; i ++ )
		{
			flag[i] = 0;
		}
		search( 0, 0);
		printf("Case #%d: %d\n", ca, min);
	}
	return 0;
}