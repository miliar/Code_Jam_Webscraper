#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAX = 110;

const int dx[4] = { -1, 0, 0, 1 };
const int dy[4] = { 0, -1, 1, 0 };

int R, S;
int grid[ MAX ][ MAX ];

int dset[ MAX*MAX ];
char boja[ MAX*MAX ];

int find( int x )
{
    if( x == dset[x] ) return x;
    return dset[x] = find( dset[x] );
}

void merge( int a, int b )
{
    a = find( a ); b = find( b );
    if( a != b ) dset[a] = b;
}

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%d %d", &R, &S );

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j )
                scanf( "%d", &grid[i][j] );

        for( int i = 0; i < R*S; ++i ) {
            dset[i] = i;
            boja[i] = 0;
        }

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j ) {
                int mini = grid[i][j];

                for( int dc = 0; dc < 4; ++dc ) {
                    int x = i + dx[ dc ];
                    int y = j + dy[ dc ];

                    if( x < 0 || x >= R ) continue;
                    if( y < 0 || y >= S ) continue;

                    if( grid[x][y] < mini ) mini = grid[x][y];
                }

                if( mini == grid[i][j] ) continue;

                for( int dc = 0; dc < 4; ++dc ) {
                    int x = i + dx[ dc ];
                    int y = j + dy[ dc ];

                    if( x < 0 || x >= R ) continue;
                    if( y < 0 || y >= S ) continue;

                    if( grid[x][y] == mini ) {
                        merge( x*S+y, i*S+j );
                        break;
                    }
                }
            }

        printf( "Case #%d:\n", t+1 );
        char curr = 'a';

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j ) {
                int x = find( i*S+j );
                if( boja[x] == 0 ) boja[x] = curr++;
                printf( "%c%c", boja[x], j+1 < S ? ' ' : '\n' );
            }
    }

    return 0;
}

