#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

#define MIN( a, b ) ( a < b ? a : b )

int main()
{
    int t, tc = 0;
    scanf( "%d", &t );
    while( tc++ < t )
    {
        int row, col;
        scanf( "%d%d\n", &row, &col );
        char M[ row ][ col ], c;
        for( int i = 0, s = col/4; i < row; ++i, getchar() )
            for( int j = 0; j < s; ++j )
            {
                c = getchar();
                if( c <= '9' )
                    c -= '0';
                else
                    c = 10 + ( c - 'A' );
                for( int h = 3; h >= 0; --h )
                {
                    M[ i ][ ( j * 4 ) + h ] = ( '0' + ( c%2 ) );
                    c /= 2;
                }
            }
        /*for( int i = 0; i < row; ++i, putchar( '\n' ) )
            for( int j = 0; j < col; ++j )
                putchar( M[ i ][ j ] );*/
        int R[ MIN( row, col ) ], total = 0;
        for( int n = MIN( row, col ) - 1; n >= 0; --n )
            R[ n ] = 0;
        for( int n = MIN( row, col ); n > 0; --n )
            for( int i = 0; i + n <= row; ++i )
                for( int j = 0; j + n <= col; ++j )
                {
                    bool st = true;
                    for( int k = 0; st && k < n; ++k )
                        for( int l = 0; st && l < n; ++l )
                        {
                            if( M[ i + k ][ j + l ] == -1 )
                                st = false;
                            else if( k + 1 < n && M[ i + k ][ j + l ] == M[ i + k + 1 ][ j + l ] )
                                st = false;
                            else if( l + 1 < n && M[ i + k ][ j + l ] == M[ i + k ][ j + l + 1 ] )
                                st = false;
                        }
                    if( st )
                    {
                        for( int k = 0; st && k < n; ++k )
                            for( int l = 0; st && l < n; ++l )
                                M[ i + k ][ j + l ] = -1;
                        if( R[ n - 1] == 0 )
                            ++total;
                        ++R[ n - 1 ];
                    }
                }
        printf( "Case #%d: %d\n", tc, total );
        for( int n = MIN( row, col ) - 1; n >= 0; --n )
            if( R[ n ] > 0 )
                printf( "%d %d\n", n + 1, R[ n ] );
    }
    return 0;
}
