#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int maxn = 501;
const int la = 19;

char s[ maxn ] = { 0 };
char a[ la + 1 ] = "welcome to code jam";
int f[ la + 1 ][ maxn ] = { 0 };

void work()
{
    int l = 0;
    memset( f, 0, sizeof( f ) );
    memset( s, 0, sizeof( s ) );
    scanf( "%c", &s[ l ] );
    while( s[ l ] != '\n' )
    {
        l++;
        scanf( "%c", &s[ l ] );
    }

    for( int j = 0; j < l; j++ )
        f[ 0 ][ j ] = ( s[ j ] == a[ 0 ] );

    for( int k = 1; k < la; k++ )
    for( int j = 0; j < l; j++ )
    {
        if( a[ k ] != s[ j ] )
            continue;
        for( int x = 0; x < j; x++ )
        {
            if( s[ x ] == a[ k - 1 ] )
            {
                f[ k ][ j ] += ( f[ k - 1 ][ x ] ) % 10000;
                f[ k ][ j ] %= 10000;
            }

        }
    }

    /*for( int k = 0; k < la; k++ )
    {
        for( int j = 0; j < l; j++ )
        {
            printf( "f[%d][%d]=%d ", k, j, f[ k ][ j ] );
        }
        printf( "\n" );
    }*/

    int ans = 0;
    for( int j = 0; j < l; j++ )
    {
        ans += f[ la - 1 ][ j ];
        ans %= 10000;
    }

    ans %= 10000;

    if( ans < 10 )
        printf( "000%d\n", ans );
    else if( ans < 100 )
        printf( "00%d\n", ans );
    else if( ans < 1000 )
        printf( "0%d\n", ans );
    else
        printf( "%d\n", ans );
}

int main()
{
    //freopen( "a.in", "r", stdin );
    //freopen( "a.out", "w", stdout );

    int d;
    cin >> d;
    char c;
    scanf( "%c", &c );
    for( int k = 0; k < d; k++ )
    {
        printf( "Case #%d: ", k + 1 );
        work();
    }

    return 0;
}
