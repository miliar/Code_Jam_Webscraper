#include <iostream>
#include <string>
using namespace std ; 
const int MOD = 10000 ;
char pat[] = "welcome to code jam" ;
char str[600] ;
int dp[600][30] ;
int len , m ;

int main()
{
	freopen("C-small-attempt2.in" , "r" , stdin) ;
	freopen("C-small-attempt2.out" , "w" , stdout) ;
	int n ; 
	int T  = 0 ;
	int i , j ;
	m = strlen(pat) ;
	while(1 == scanf("%d" ,&n))
	{
		T = 0 ;
		getchar() ;
		while(n--)
		{
			T++ ;
			gets(str) ;
			len = strlen(str) ;
			memset(dp , -1 , sizeof(dp)) ;
			bool flag = false ;
			for(i = 0 ; i < len ; i++)
			{
				if( str[i] == 'w' )
				{
					if( !flag )
						dp[i][0] = 1 ;
					else dp[i][0] = dp[i-1][0] + 1 ;
					flag = true ;

					if( dp[i][0] >= MOD )
						dp[i][0] %= MOD ;
					if(i > 0)
					{
						for(j = 1 ; j < m ; j++)
							dp[i][j] = dp[i-1][j] ;
					}
					continue ;
				}
				else if( !flag ) continue ;
				dp[i][0] = dp[i-1][0] ;
				if( dp[i][0] >= MOD )
						dp[i][0] %= MOD ;
				for(j = 1 ; j < m ; j++)
				{
					if( str[i] == pat[j] )
					{
						if( dp[i-1][j-1] != -1 )
						{
							if( dp[i-1][j] == -1 )
								dp[i][j] = dp[i-1][j-1] ;
							else 
								dp[i][j] = dp[i-1][j] + dp[i-1][j-1] ;
						}
					}
					else dp[i][j] = dp[i-1][j] ;
					if( dp[i][j] >= MOD)
						dp[i][j] %= MOD ;
				}
			}
			printf("Case #%d: " ,T ) ;
			if( dp[len-1][m-1] == -1)
				printf("0000\n") ;
			else if(dp[len-1][m-1]/10 == 0)
				printf("000%d\n" , dp[len-1][m-1]) ;
			else if(dp[len-1][m-1]/100 == 0)
				printf("00%d\n" , dp[len-1][m-1]) ;
			else if(dp[len-1][m-1]/1000 == 0)
				printf("0%d\n" , dp[len-1][m-1]) ;
			else printf("%d\n" , dp[len-1][m-1]) ;

		}
	}
	return 0 ;
}