#include <cstdio>

#define MAX 55

bool player_wins( char M[ MAX ][ MAX ], char p, int n, int k );
void rotar( char M[ MAX ][ MAX ], int n );

int main()
{
    int t, c = 0, k, n;
    bool red, blue;
    char M[ MAX ][ MAX ];
    scanf( "%d", &t );
    while( c++ < t )
    {
        printf( "Case #%d: ", c );
        scanf( "%d%d\n", &n, &k );
        red = blue = false;
        for( int i = 0; i < n; ++i, getchar() )
            for( int j = 0; j < n; ++j )
                M[ i ][ j ] = getchar();
        rotar( M, n );
        red = player_wins( M, 'R', n, k );
        blue = player_wins( M, 'B', n, k );
        if( !red && !blue )
            printf( "Neither\n" );
        else if( !red )
            printf( "Blue\n" );
        else if( !blue )
            printf( "Red\n" );
        else
            printf( "Both\n" );
    }
    return 0;
}

bool rows( char M[ MAX ][ MAX ], int n, int k, char p )
{
    int c = 0;
    for( int i = 0; i < n; ++i, c = 0 )
        for( int j = 0; j < n; ++j )
        {
            if( M[ i ][ j ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
    return false;
}

bool cols( char M[ MAX ][ MAX ], int n, int k, char p )
{
    int c = 0;
    for( int i = 0; i < n; ++i, c = 0 )
        for( int j = 0; j < n; ++j )
        {
            if( M[ j ][ i ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
    return false;
}

bool diag_a( char M[ MAX ][ MAX ], int n, int k, char p )
{
    int c = 0;
    for( int i = 0; i < n; ++i, c = 0 ) /* revisa fila i, columna 0 en diagonal */
        for( int x = i, y = 0; x < n && y < n; ++x, ++y )
        {
            if( M[ x ][ y ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
    c = 0;
    for( int i = 1; i < n; ++i, c = 0 ) /* revisa fila 0, columna i */
        for( int x = 0, y = i; x < n && y < n; ++x, ++y )
        {
            if( M[ x ][ y ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
    return false;
}

bool diag_b( char M[ MAX ][ MAX ], int n, int k, char p )
{
    int c = 0;
    for( int i = 0; i < n; ++i, c = 0 ) /* revisa fila i, columna 0 en diagonal */
        for( int x = i, y = 0; x >= 0 && y < n; --x, ++y )
        {
            if( M[ x ][ y ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
        c = 0;
    for( int i = 1; i < n; ++i ) /* revisa fila n-1, columna i */
        for( int x = n - 1, y = i; x >= 0 && y < n; --x, ++y )
        {
            if( M[ x ][ y ] == p )
                ++c;
            else
                c = 0;
            if( c >= k )
                return true;
        }
        return false;
}

void print( char M[ MAX ][ MAX ], int n )
{
    putchar( '\n' );
    for( int i = 0; i < n; ++i, putchar( '\n' ) )
        for( int j = 0; j < n; ++j )
            putchar( M[ i ][ j ] );
}

void take_down( char M[ MAX ][ MAX ], int n, int x, int y )
{
    while( x + 1 < n && M[ x + 1 ][ y ] == '.' )
    {
        M[ x + 1 ][ y ] = M[ x ][ y ];
        M[ x ][ y ] = '.';
        ++x;
    }
}

/*
        ( 0, 0 ) -> top left corner
        ( n, n ) -> bottom right corner
        ( n, 0 ) -> bottom left corner
        ( 0, n ) -> top right corner
*/
void gravity( char M[ MAX ][ MAX ], int n )
{
    for( int i = n - 1; i >= 0; --i )
        for( int j = 0; j < n; ++j )
            if( M[ i ][ j ] != '.' )
                take_down( M, n, i, j );
}

void rotar( char M[ MAX ][ MAX ], int n )
{
    char T[ MAX ][ MAX ];
    gravity( M, n );
    for( int j = 0; j < n; ++j )
        for( int i = n - 1, x = 0; i >= 0; --i, ++x )
            T[ j ][ x ] = M[ i ][ j ];
    for( int i = 0; i < n; ++i )
        for( int j = 0; j < n; ++j )
            M[ i ][ j ] = T[ i ][ j ];
    gravity( M, n );
}

bool player_wins( char M[ MAX ][ MAX ], char p, int n, int k )
{
    return rows( M, n, k, p ) || cols( M, n, k, p ) || diag_a( M, n, k, p ) || diag_b( M, n, k, p );
}
