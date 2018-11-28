#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    int t, n, caso = 0;
    int P; // games played
    int W; // games won
    char M[ 110 ][ 110 ];
    double WP[ 110 ];
    double OWP[ 110 ];
    double OOWP[ 110 ];
    char tc;
    scanf( "%d", &t );
    while( caso++ < t )
    {
        scanf( "%d", &n );
        for( int i = 0; i < n; ++i )
        {
            P = W = 0;
            for( int j = 0; j < n; )
                if( ( tc = getchar() ) == '.' || tc == '1' || tc == '0' )
                {
                    M[ i ][ j++ ] = tc;
                    P += tc != '.' ? 1 : 0;
                    W += tc == '1' ? 1 : 0;
                }
            WP[ i ] = (double)W / (double)P;
        }
        for( int i = 0; i < n; ++i )
        {
            OWP[ i ] = 0.0;
            int tpa = 0;
            for( int j = 0; j < n; ++j )
                if( M[ i ][ j ] != '.' )
                {
                    int gp = 0, gw = 0; // fake win perc of team j
                    for( int k = 0; k < n; ++k )
                        if( k != i && k != j && M[ j ][ k ] != '.' ) // j vs k
                        {
                            ++gp;
                            gw += ( M[ j ][ k ] == '1' ? 1 : 0 );
                        }
                    OWP[ i ] += gw / (double)gp;
                    ++tpa;
                }
            OWP[ i ] /= (double)tpa;
        }
        for( int i = 0; i < n; ++i )
        {
            OOWP[ i ] = 0.0;
            int tpa = 0;
            for( int j = 0; j < n; ++j )
                if( j != i && M[ i ][ j ] != '.' )
                {
                    OOWP[ i ] += OWP[ j ];
                    ++tpa;
                }
            OOWP[ i ] /= (double)tpa;
        }
        printf( "Case #%d:\n", caso );
        for( int i = 0; i < n; ++i )
            printf( "%.8lf\n", ( 0.25 * WP[ i ] ) + ( 0.25 * OOWP[ i ] ) + ( 0.5 * OWP[ i ] ) );
    }
    return 0;
}
