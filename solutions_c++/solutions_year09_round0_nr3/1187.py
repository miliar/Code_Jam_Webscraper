#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXN = 505,MOD=10000;
const char code[] = "welcome to code jam";

char input[MAXN];
int dp[MAXN][50];
int n , m ;

int main()
{
	freopen("data.txt", "r", stdin );
	freopen("C.out", "w", stdout );
	int t ;
	gets(input);
	sscanf (input, "%d", &t );
	int cas;

	for(cas=1;cas<=t;cas++)
	{
		gets(input);
		n = strlen(input);
		m = strlen(code);
		memset(dp,0,sizeof dp);
		dp[n][m]=1;
		int i , j ;

		for( i = n - 1 ; i >= 0 ; i -- )
		{
			for( j = m ; j >= 0 ; j -- )
			{
				if( code[ j ] == input[ i ] )
					dp[ i ][ j ] = (dp[ i ][ j ] + dp[ i + 1 ] [ j + 1 ])%MOD;
				dp[ i ][ j ] = (dp[i+1][j]+dp[i][j])%MOD;
			}
		}

		printf("Case #%d: ",cas);
		char res [ 10 ];
		sprintf( res, "%d", dp[ 0 ][ 0 ] );
		for( i = 0;i < 4-strlen(res);i++)
			putchar('0');
		printf(res);
		putchar('\n');
	}

	return 0;
}