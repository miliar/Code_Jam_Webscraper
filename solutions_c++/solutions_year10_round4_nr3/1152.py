#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define MAX 1000

using namespace std;

void fill( bool M[ MAX ][ MAX ], int, int, int, int );
bool second( bool M[ MAX ][ MAX ], bool R[ MAX ][ MAX ] );
void print( bool M[ MAX ][ MAX ] );

int main()
{
    int t, casos = 0, k, x, y, xf, yf;
    scanf( "%d", &t );
    while( casos++ < t )
    {
        scanf( "%d", &k );
        bool M[ MAX ][ MAX ], R[ MAX ][ MAX ];
        for( int i = 0; i < MAX; ++i )
            for( int j = 0; j < MAX; ++j )
                M[ i ][ j ] = R[ i ][ j ] = false;
        for( int i = 0; i < k; ++i )
        {
            scanf( "%d%d%d%d", &x, &y, &xf, &yf );
            fill( M, x, y, xf, yf );
        }
        int s = 1;
        while( second( M, R ) )
            ++s;
        printf( "Case #%d: %d\n", casos, s );
    }
    return 0;
}

bool second( bool M[ MAX ][ MAX ], bool R[ MAX ][ MAX ] )
{
    bool ans = false;
    for( int i = 1; i < MAX; ++i )
        for( int j = 1; j < MAX; ++j )
        {
            if( M[ i ][ j ] )
                R[ i ][ j ] = ( M[ i - 1 ][ j ] || M[ i ][ j - 1 ] );
            else
                R[ i ][ j ] = ( M[ i - 1 ][ j ] && M[ i ][ j - 1 ] );
            ans = ans || R[ i ][ j ];
        }
    if( !ans )
        return false;
    for( int i = 0; i < MAX; ++i )
        for( int j = 0; j < MAX; ++j )
            M[ i ][ j ] = R[ i ][ j ];
    return true;
}

void fill( bool M[ MAX ][ MAX ], int x, int y, int xf, int yf )
{
    int offset = 100;
    y += offset, yf += offset, xf += offset, x += offset;
    for( int i = y; i <= yf; ++i )
        for( int j = x; j <= xf; ++j )
            M[ i ][ j ] = true;
}

void print( bool M[ MAX ][ MAX ] )
{
    for( int i = 0; i < MAX; ++i, putchar( '\n' ) )
        for( int j = 0; j < MAX; ++j )
            putchar( M[ i ][ j ] ? '1':'0' );
    printf( "-\n" );
}
