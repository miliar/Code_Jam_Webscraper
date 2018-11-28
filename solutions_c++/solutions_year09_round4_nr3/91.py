#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int MAXN = 500;

int n, k;
int V[ MAXN ][ 30 ];

vector< int > E[ MAXN ];

int dad[ MAXN ];
int bio[ MAXN ];

int match( int x ) {
    if( bio[x] ) return false;

    bio[x] = true;

    for( vector< int >::iterator it = E[x].begin(); it != E[x].end(); ++it )
        if( dad[ *it ] == -1 || match( dad[ *it ] ) ) {
            dad[ *it ] = x;
            return true;
        }

    return false;
}

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        int n, k; scanf( "%d %d", &n, &k );

        for( int i = 0; i < n; ++i )
            E[i].clear();

        for( int i = 0; i < n; ++i ) 
            for( int j = 0; j < k; ++j )
                scanf( "%d", V[i] + j );

        for( int i = 0; i < n; ++i )
            for( int j = 0; j < n; ++j ) {
                if( i == j ) continue;
                int ok = true;

                for( int x = 0; x < k; ++x ) {
                    if( V[i][x] <= V[j][x] )
                        ok = false;
                }

                if( ok == true ) 
                    E[j].push_back( i );
            }
        
        int flow = 0;
        memset( dad, -1, sizeof dad );
        
        for( int i = 0; i < n; ++i ) {
            memset( bio, 0, sizeof bio );
            flow += match( i );
        }

        printf( "Case #%d: %d\n", counter + 1, n - flow );
    }

    return (0-0);
}
