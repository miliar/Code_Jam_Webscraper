#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

const int maxn = 101;

int d;
int n, m;
int g[ maxn ][ maxn ] = { 0 };
int mark[ maxn ][ maxn ] = { 0 };
char ans[ maxn ][ maxn ] = { 0 };

int val( int x, int y )
{
    return ( 0 <= x && x < n && 0 <= y && y < m ) ? g[ x ][ y ] : 100000;
}

bool update( int nx, int ny, int &dx, int &dy, int &min )
{
    if( min > val( nx, ny ) )
    {
        min = g[ nx ][ ny ];
        dx = nx;
        dy = ny;
        return true;
    }
    return false;
}

int flow( int x, int y )
{
    if( mark[ x ][ y ] )
        return mark[ x ][ y ];

    int min = g[ x ][ y ];
    int dx = x, dy = y;

    update( x - 1, y, dx, dy, min );
    update( x, y - 1, dx, dy, min );
    update( x, y + 1, dx, dy, min );
    update( x + 1, y, dx, dy, min );

    if( dx == x && dy == y )
    {
        mark[ x ][ y ] = x * m + y;
        return mark[ x ][ y ];
    }

    mark[ x ][ y ] = flow( dx, dy );
    return mark[ x ][ y ];
}




void work()
{
    cin >> n >> m;

    for( int k = 0; k < n; k++ )
    for( int j = 0; j < m; j++ )
        cin >> g[ k ][ j ];

    memset( mark, 0, sizeof( mark ) );
    memset( ans, 0, sizeof( ans ) );

    for( int k = 0; k < n; k++ )
    for( int j = 0; j < m; j++ )
    {
        mark[ k ][ j ] = flow( k, j );
    }


    char c = 'a';
    for( int k = 0; k < n; k++ )
    for( int j = 0; j < m; j++ )
    {
        if( ans[ k ][ j ] )
            continue;
        int now = mark[ k ][ j ];
        for( int p = 0; p < n; p++ )
        for( int q = 0; q < m; q++ )
        {
            if( mark[ p ][ q ] == now )
                ans[ p ][ q ] = c;
        }

        c++;
    }
}


int main()
{
    //freopen( "a.in", "r", stdin );
    //freopen( "a.out", "w", stdout );
    cin >> d;
    for( int t = 0; t < d; t++ )
    {
        work();
        printf( "Case #%d:\n", t + 1 );
        for( int k = 0; k < n; k++ )
        {
            for( int j = 0; j < m; j++ )
            {
                printf( "%c", ans[ k ][ j ] );
                if( j == m - 1 )
                    printf( "\n" );
                else
                    printf( " " );
            }
        }
    }

    return 0;
}
