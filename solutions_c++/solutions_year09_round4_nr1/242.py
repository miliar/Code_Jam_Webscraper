#include <algorithm>
#include <vector>
#include <string>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 42;

int n;

char grid[ MAXN ][ MAXN ];
int row[ MAXN ];

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%d", &n );

        for( int i = 0; i < n; ++i ) {
            scanf( "%s", grid[i] );
            row[i] = 0;

            for( int j = 0; j < n; ++j )
                if( grid[i][j] == '1' )
                    row[i] = j;
        }

        int cnt = 0;

        for( int i = 0; i < n; ++i ) {
            int uzmi = -1;

            for( int j = i; j < n; ++j )
                if( row[j] <= i ) {
                    uzmi = j;
                    break;
                }

            cnt += ( uzmi - i );

            for( int j = uzmi; j >= i; --j )
                row[j] = row[j-1];
        }

        printf( "Case #%d: %d\n", t+1, cnt );
    }

    return 0;
}

