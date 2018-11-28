#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

#define maxn 1000100
#define maxm 30002
#define inf 1<<29
#define Max( a , b ) ((a) > (b)) ? a : b
#define Min( a , b ) ((a) < (b)) ? a : b

int n , q , dp[1001][102] , list[1002];
char s[102][102];

int fd( char *x )
{
    int i;
    for( i = 1;i <= n;i++ )
         if( strcmp( s[i] , x ) == 0 ) return i;
    return n+1;
}

void solve()
{
     int i , j , k , a;
     char in[102];
     scanf("%d" , &n );
     getchar();
     for( i = 1;i <= n;i++ )
          gets( s[i] );
     scanf("%d" , &q );getchar();
     for( i = 1;i <= q;i++ )
     {
          gets( in );
          list[i] = fd( in );
     }
     if( n == 0 || q == 0 ) {
         printf("0\n");return;
     }
     memset( dp , -1 , sizeof( dp ) );
     for( i = 1;i <= n;i++ )
          if( i != list[1] ) dp[1][i] = 0;
          else dp[1][i] = inf;
     for( i = 2;i <= q;i++ )
     {
          for( j = 1;j <= n;j++ )
          {
               dp[i][j] = inf;
               if( j == list[i] ) continue;
               for( k = 1;k <= n;k++ ) {
                    a = dp[i-1][k] + (k != j );
                    dp[i][j] = Min( dp[i][j] , a );
               }
          }
     }
     for( a = dp[q][1] , i = 2;i <= n;i++ )
          a = Min( a , dp[q][i] );
     printf("%d\n" , a );
     
}

int main()
{
    int cas , i;
    scanf("%d" , &cas);
    for( i = 1;i <= cas;i++ )
    {
         printf("Case #%d: " , i );
         solve();
    }
    
    
    return 0;
}
