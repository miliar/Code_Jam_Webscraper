#include<stdio.h>
#include<string.h>
int S, Q ;
char Engine[128][128];
int query[1024];
int ans[1024][128];
int res;
int findIndex( char*p)
{
	int i;
	for( i = 0 ; i < S ; i ++)
	{
		if( !strcmp(p,Engine[i]))
			return i;
	}
	return -1;
}
void init()
{
	scanf("%d",&S);
	char buffer[128];
	int i;
	gets(buffer);
	for( i = 0 ; i < S ; i ++ )
	{
		gets(Engine[i]);
	}
	scanf("%d",&Q);
	gets(buffer);
	for( i = 0 ; i < Q ; i ++)
	{
		gets(buffer);
		query[ i ] = findIndex( buffer ); 
	}
}
void run()
{
	if( Q == 0 )
	{
		res = 0 ;
		return ;
	}
	memset( ans, 0 , sizeof(ans) );
	int i,j;
	const int INF = 0x1fffffff;
	ans[0][query[ 0 ]] = INF ;
	for(i = 1 ; i < Q ; i ++ )
	{
		for( j = 0 ; j < S ; j ++)
		{
			if( j == query[i] )
				ans[i][j] = INF;
			else
			{
				int k;
				ans[i][j] = INF;
				for( k = 0 ; k < S ; k ++ )
				{
					if( ans[i-1][k] == INF)
						continue;
					if( k == j )
					{
						ans[i][j] = ans[i][j] < ans[i-1][k] ? ans[i][j] : ans[i-1][k];
					}
					else
					{
						ans[i][j] = ans[i][j] < ans[i-1][k] + 1 ? ans[i][j] : ans[i-1][k] + 1;
					}
				}
			}
		}
	}
	
	res = ans[Q-1][0];
	for( i = 1 ; i < S ; i ++ )
	{
		res = res < ans[Q-1][i] ? res : ans[Q-1][i];
	}
	
}
int main ()
{
#ifdef _DEBUG
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int nCase;
	scanf("%d",&nCase);
	int cnt = 0 ;
	while ( nCase -- )
	{
		cnt ++ ;
		init();
		run();
		printf("Case #%d: %d\n",cnt,res);
	}
	return 0;
}