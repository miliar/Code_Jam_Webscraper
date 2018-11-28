#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

const int MaxN = 10002;
const int INF = 30000;

int n, k, v;

int dp[ MaxN ][ 2 ];
int g[ MaxN ], c[ MaxN ];

int rek( int x, int y )
{
    if( dp[x][y] != -1 ) return dp[x][y];
    int k = INF;
    if( g[x] == 1 )
    {
        if( y == 1 ) k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 1 ) ); else
        {
            k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 0 ) );
            k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 1 ) );
            k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 0 ) );
        }
        if( c[x] == 1 )
        {
            if( !y ) k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 0 ) + 1 ); else
            {
                k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 1 ) + 1 );
                k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 1 ) + 1 );
                k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 0 ) + 1 );  
            }
        }
    } else
    {
            if( !y ) k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 0 ) ); else
            {
                k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 1 ) );
                k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 1 ) );
                k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 0 ) );
            }
            if( c[x] == 1 )
            {
                if( y == 1 ) k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 1 ) + 1 ); else
                {
                    k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 0 ) + 1 );
                    k = min( k, rek( x * 2, 0 ) + rek( x * 2 + 1, 1 ) + 1 );
                    k = min( k, rek( x * 2, 1 ) + rek( x * 2 + 1, 0 ) + 1 );
                }
            }
    }
    return dp[x][y] = k;
}                          
            
         
int main( void )
{
    int t;
    ifstream in( "A-large.in" );
    ofstream out( "A.out" );
    in >> t;
  //  cout << t;
    for( int R = 1; R <= t; ++R )
    {
         memset( dp, -1, sizeof( dp ) );
         in >> n >> v;
         for( int i = 1; i <= ( n - 1 ) / 2; ++i )
              in >> g[i] >> c[i];
         for( int i = ( n + 1 ) / 2; i <= n; ++i )
         {
              int r;
              in >> r;
              dp[i][r] = 0;
              dp[i][!r] = INF;
         }
         int ret = rek( 1, v );
         out << "Case #" << R << ": ";
         if( ret >= INF ) out << "IMPOSSIBLE" << endl; else
         out << ret << endl;
    }
 //   for(;;);
    return 0;
}
