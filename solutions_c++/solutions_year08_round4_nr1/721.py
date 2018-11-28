#include <map>
#include <set>
#include <list>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

const int MAXM = 10000 , INF = 0x3f3f3f3f ;

int canchange[ MAXM ], isand[ MAXM ], leaf[ MAXM ], dp[ MAXM ] [ 2 ] ;
int val[ MAXM ];
int m,v;

void recurr ( int curr )
{
    dp[ curr ][ val[ curr ] ] = 0;
    if( leaf[ curr ] )
     return ;
    recurr( 2*curr );
    recurr( (2*curr) + 1 );


        if( val[curr] )
        {
            if( isand[ curr ] || canchange[ curr ] )
            {
                dp[ curr ][ 0 ] = min( dp[2*curr][1] + dp[(2*curr)+1][0]+!isand[curr], dp[curr][0]);
                dp[ curr ][ 0 ] = min( dp[2*curr][0] + dp[(2*curr)+1][1]+!isand[curr], dp[curr][0]);
                dp[ curr ][ 0 ] = min( dp[2*curr][0] + dp[(2*curr)+1][0]+!isand[curr], dp[curr][0]);
            }
            if( !isand[ curr ] || canchange[ curr ] )
            {
                dp[ curr ][ 0 ] = min( dp[2*curr][0] + dp[(2*curr)+1][0]+isand[curr], dp[curr][0]);
            }
        }
        else
        {
            if( isand[ curr ] || canchange[ curr ] )
            {
                dp[ curr ][ 1 ] = min( dp[2*curr][1] + dp[(2*curr)+1][1]+!isand[curr], dp[curr][1]);
            }
            if( !isand[ curr ] || canchange[ curr ] )
            {
                dp[ curr ][ 1 ] = min( dp[2*curr][1] + dp[(2*curr)+1][0]+isand[curr], dp[curr][1]);
                dp[ curr ][ 1 ] = min( dp[2*curr][0] + dp[(2*curr)+1][1]+isand[curr], dp[curr][1]);
                dp[ curr ][ 1 ] = min( dp[2*curr][1] + dp[(2*curr)+1][1]+isand[curr], dp[curr][1]);
            }
        }

    return ;
}

int set_val( int curr )
{
    if( leaf[ curr ] ) return val[ curr ];
    if(isand[ curr ])
     val[ curr ] = set_val( 2*curr ) & set_val( 2*curr + 1 );
    else
     val[ curr ] = set_val( 2*curr ) | set_val( 2*curr + 1 );
    return val[ curr ];
}

int main()
{
    int n;
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    scanf( "%d", &n );

    for( int cas = 1 ; cas <= n ; cas ++)
    {
        scanf ( "%d %d", &m , &v );
        memset( leaf, 0, sizeof leaf );
        memset( dp, 0x3f, sizeof dp );
        memset( isand, 0, sizeof isand );
        memset( canchange , 0, sizeof canchange );

        for(int i = 1;i <= (m-1)/2; i ++)
        {
            int a , c ;
            scanf ( "%d %d", &a, &c );
            isand[ i ] = a ;
            canchange[ i ] = c;
        }

        for(int i = ((m-1)/2) +1;i <= m; i ++)
        {
            int temp;
            leaf [ i ] = 1 ;
            scanf ( "%d", &temp );
            val[ i ] = temp;
        }

        set_val( 1 );
        recurr( 1 );

        printf( "Case #%d: ", cas);
        if( dp[1][v] >= INF )
         printf( "IMPOSSIBLE\n");
        else
         printf( "%d\n", dp[1][v] );
    }

    return 0;
}
