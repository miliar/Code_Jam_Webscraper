#include <stdio.h>
#include <string.h>

const int INF = 20000;
char engine[105][105];
int  dp[1005][105];
int main ()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int i, j, k;
	int t;
	int T;
	int s, q;
	char query[105];
	scanf("%d",&T);
	for ( t=1; t<=T; t++ )
	{
		scanf("%d", &s );		
		gets( engine[0] );
		for ( i=0; i<s; i++ )
			gets( engine[i] );
		scanf("%d", &q );
		if ( q==0 )
		{
			printf("Case #%d: 0\n", t );
			continue;
		}
		gets( query );gets( query );
		for ( i=0; i<s; i++ )
		{
			if ( strcmp( query, engine[i] )==0 )
				dp[0][i] = INF;
			else
				dp[0][i] = 0;
		}
		for ( i=1; i<q; i++ )
		{
			gets( query );
			for ( j=0; j<s; j++ )
			{
				if ( strcmp( query, engine[j])==0  )
					dp[i][j] = INF;
				else
				{
					int min = INF;
					for ( k=0; k<s; k++ )
					{
						if ( j==k )
						{
							if ( dp[i-1][k]<min )
								min = dp[i-1][k];
						}
						else
						{
							if ( dp[i-1][k]+1<min )
								min = dp[i-1][k]+1;
						}
					}
					dp[i][j] = min;
				}
			}
		}
		int min = INF;
		for ( i=0; i<s; i++ )
		{
			if ( dp[q-1][i]<min )
				min = dp[q-1][i];
		}
		printf("Case #%d: %d\n", t, min );
	}
	return 0;
}