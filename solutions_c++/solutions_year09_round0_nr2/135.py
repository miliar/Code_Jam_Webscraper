#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int dx[ 4 ] = { -1, 0, 0, 1 };
const int dy[ 4 ] = { 0, -1, 1, 0 };

int R, S;
int grid[ 110 ][ 110 ];
int kamox[ 110 ][ 110 ];
int kamoy[ 110 ][ 110 ];

inline bool valid( int x, int y ) { if( x < 0 || y < 0 || x >= R || y >= S ) return false; return true; }

char output[ 110 ][ 110 ];

char calc( int x, int y ) {
    if( output[x][y] != 0 ) return output[x][y];
    if( kamox[x][y] == -1 ) return 0;
    return output[x][y] = calc( kamox[x][y], kamoy[x][y] );
}

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        scanf( "%d %d", &R, &S );

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j )
                scanf( "%d", grid[i] + j );

        memset( kamox, -1, sizeof kamox );
        memset( kamoy, -1, sizeof kamoy );

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j ) {
                int where = -1;
                int val = 1000000000;

                for( int pc = 0; pc < 4; ++pc ) {
                    int ni = i + dx[ pc ];
                    int nj = j + dy[ pc ];
                    if( !valid( ni, nj ) ) continue;
                    if( grid[ni][nj] >= grid[i][j] ) continue;
                    if( val > grid[ni][nj] ) {
                        val = grid[ni][nj];
                        where = pc;
                    }
                }

                if( where != -1 ) {
                    int ni = i + dx[ where ];
                    int nj = j + dy[ where ];
                    kamox[i][j] = ni;
                    kamoy[i][j] = nj;
                }
            }

        char next = 'a';
        memset( output, 0, sizeof output );
        printf( "Case #%d:\n", counter + 1 );

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j ) {
                char c = calc( i, j );
                if( c != 0 ) output[i][j] = c;
                else {
                    int x = i, y = j;

                    while( x != -1 ) {
                        output[x][y] = next;
                        int old_x = x;
                        x = kamox[x][y];
                        y = kamoy[old_x][y];
                    }

                    ++next;
                }

                putchar( output[i][j] );
                putchar( j+1 == S ? '\n' : ' ' );
            }
    }

    return (0-0);
}
