#include <iostream>
#include <string>
#include <map>
using namespace std ;

map<string , int>a ;
int dp[1005][105] ;

int main(){
	int test ;
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen("A-large.out" , "w" , stdout ) ;
	cin >> test ;
	int t =  1 ;
	while( test -- )
	{
		int s , q ;
		cin >> s ;
		string str ;
		int n = 0 ;
		getchar() ;
		int i , j , k ;
		for( i = 0 ; i < s;  i ++ )
		{
			getline( cin , str ) ;
			a[str] = n ++ ;
		}
		
		cin >> q ;
		for( i = 1 ; i <= q ; i ++ )
			for( j = 0 ; j < n ; j++ )
				dp[i][j] = 1005 ;
		int temp ;
		getchar() ;
		for( i = 1 ; i <= q ; i ++ )
		{
			getline( cin , str ) ;
			temp = a[str] ;
			for( j = 0 ; j < n;  j ++ )
			{
				if( j != temp )
					dp[i][j] = min( dp[i-1][j] , dp[i][j] ) ;
				else
				{
					for( k = 0 ; k < n ; k ++ )
					{
						if( k == j )
							continue ;
						else
							dp[i][k] = min( dp[i-1][j] + 1 , dp[i][k] ) ;
					}
				}
			}
		}

		int Min = -1 ;
		for( i = 0 ;i < n; i ++ )
			if( dp[q][i] < Min || Min == -1 )
				Min = dp[q][i] ;
		printf("Case #%d: %d\n" , t++ , Min ) ;
	}
	return 0 ;
}