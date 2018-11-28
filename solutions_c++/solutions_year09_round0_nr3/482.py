#include <iostream>
#include <string>
using namespace std ;

char a[20] ;
int dp[505][20] ;

void init(){
     char str[] = "welcome to code jam" ; 
     int len = strlen(str) ;
     int i ;
     for( i = 0 ; i < len ; i ++ )
          a[i] = str[i] ;    
}
void solve( char str[] )
{
     int n = strlen(str) ;
     memset( dp , 0 , sizeof(dp) ) ;
     int i , j ;
     for( i = 0 ; i < n ; i ++ )
     {
          if( str[i] == 'w' )
              dp[i][0] += 1 ;
          if( i != 0 )
          {
              for( j = 18 ; j >= 0 ; j -- )
              {
                   if( dp[i-1][j] )
                   {
                       if( j + 1 <= 18 && str[i] == a[j+1] )
                       {
                           dp[i][j+1] += dp[i-1][j] ;
                           while( dp[i][j+1] >= 10000 )
                                  dp[i][j+1] -= 10000 ;
                       }
                       dp[i][j] += dp[i-1][j] ;
                       while( dp[i][j] >= 10000 )
                              dp[i][j] -= 10000 ;
                   }
              }
          }
     }
}
int main(){
    freopen("C-large.in", "r",stdin) ;
    freopen("C-large.out","w",stdout) ;
    int n ;
    init();
    while( scanf("%d" , &n ) == 1 )
    {
           int i , k ;
           char str[505] ;
		   getchar();
           for( i = 0 ; i < n ; i ++ )
           {
                gets(str) ;
                solve( str ) ;
                k = strlen(str) ;
                printf("Case #%d: %04d\n" , i + 1 , dp[k-1][18] ) ;
           }
    }
    return 0 ;
}
