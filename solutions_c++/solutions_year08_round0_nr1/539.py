#include<stdio.h>
#include<string.h>

char query[1010][110];
char engine[1010][110];
int dp[1010][1010];
char temp[110];


int main()
{
	freopen( "temp.txt", "r", stdin);
	freopen( "out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int casenum = 0;
	while( T -- )
	{
		casenum ++;
		int i, j, k;
		int n, q;
		scanf("%d", &n);
		gets( temp );
		for( i=0; i<n; i++ )
			gets( engine[i] );
		scanf("%d", &q);
		gets( temp );
		for( i=0; i<q; i++ )
			gets( query[i] );
		for( i=0; i<=q; i++ )
			for( j=0; j<= n; j++)
				dp[i][j] = -1;
		for( i=0; i<q; i++ )
		{
			for( j=0; j<n; j++ )
			{
				if( strcmp( query[i], engine[j] ) == 0 )
					continue;
				int cur = -1;
				int now;
				for( k=0; k<n; k++ )
				{
					if( i == 0 )
					{
						dp[i][j] = 0;
						break;
					}
					else
					{
						if( dp[i-1][k] == -1 )
							continue;
						if( j == k )
							now = dp[i-1][k];
						else
							now = dp[i-1][k] + 1;
						if( cur == -1 || now < cur )
							cur = now;
					}
				}
				if( cur != -1 )
					dp[i][j] = cur;
			}
		}
		int re = -1;
		for( i=0; i<n; i++ )
		{
			if( dp[q-1][i] >= 0 )
			{
				if( re == -1 || dp[q-1][i] < re )
					re = dp[q-1][i];
			}
		}
		if( q == 0 )
			re = 0;
		printf("Case #%d: %d\n", casenum, re);
	}
	return 0;
}