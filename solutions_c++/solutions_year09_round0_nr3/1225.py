#include <stdio.h>
#include <string.h>

char const HELL[] = "welcome to code jam";
int const MAXLEN = 600;

int main()
{
//    freopen( "in.txt", "rt", stdin );
    int testCount;
    scanf( "%d\n", &testCount );
    for( int test = 1; test <= testCount; ++ test )
    {
        char str[ MAXLEN + 1 ];
        gets( str );
        int len = strlen( str );
        int src_len = strlen( HELL );
        int D[ sizeof( HELL )][ MAXLEN ];
        for( int i = 0; i != len; ++ i)
        {
            D[ 0 ][ i ] = i > 0 ? D[ 0 ][ i - 1] : 0;
            if( str[ i ] == HELL[ 0 ] ) ++ D[ 0 ][ i ];
        }
        for( int i = 1; i != src_len; ++ i )
        {
            D[ i ][ 0 ] = 0;
            for( int j = 1; j != len; ++ j )
            {
                int t = D[ i ][ j - 1 ];
                if( str[ j ] == HELL[ i ] ) t = ( t + D[ i - 1 ][ j - 1 ] ) % 10000;
                D[ i ][ j ] = t;
            }
        }

        int count = D[ src_len - 1 ][ len - 1 ];

        printf( "Case #%d: %04d\n", test, count );
    }
    return 0;
}