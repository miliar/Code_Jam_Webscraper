#include <stdio.h>
#include <string.h>
int dp[111][111] ;
char m[111][111] ;

int main()
{
	freopen ( "D-small-attempt1.in" , "r" , stdin ) ;
	freopen ( "D-small-attempt1.out" , "w" , stdout ) ;
	int tn , h , w , r , x , y , i , j , prob = 0 ;
	for ( scanf ( "%d" , &tn ) ; tn -- ; )
	{
		memset ( dp , 0 , sizeof(dp ) ) ;
		memset ( m , 0 , sizeof(m ) ) ;
		scanf ( "%d%d%d" , &h , &w , &r ) ;
		for ( i = 0 ; i < r ; i ++ )
		{
			scanf ( "%d%d" , &x , &y ) ;
			m[x][y] = 1 ;
		}
		dp[1][1] = 1 ;
		for ( i = 1 ; i <= h ; i ++ )
			for ( j = 1 ; j <= w ; j ++ ) if ( !m[i][j] && dp[i][j] ) 
			{
				if ( i + 2 <= h && j + 1 <= w && !m[i+2][j+1])
					dp[i+2][j+1] = (dp[i+2][j+1]+dp[i][j])%10007 ;
				if ( i + 1 <= h && j + 2 <= w && !m[i+1][j+2] )
					dp[i+1][j+2] = (dp[i+1][j+2]+dp[i][j])%10007 ;
			}
		printf ( "Case #%d: %d\n" , ++prob , dp[h][w] ) ;
	}
	return 0 ;
}