#include<stdio.h>
#include<algorithm>

using namespace std;


int T, N, S, P;

int data[ 103 ];


inline int _max( int a, int b )
{
        if( a < b ) return b;
        return a;
}

int main( )
{
        scanf( "%d", &T );
        for( int i = 1; i <= T; i ++ )
        {
                scanf( "%d", &N );
                scanf( "%d", &S );
                scanf( "%d", &P );
                for( int j = 1; j <= N; j ++ )
                        scanf( "%d", &data[ j ] );

                sort( data + 1, data + N + 1 );

                int res = 0;

                for( int j = N; j >= 1; j -- )
                {
                        // like case (p, p-1, p-1)
                        if( P + _max( 0, P - 1 ) * 2 <= data[ j ] )
                                res ++;
                        else if( S > 0 )
                        {
                                // like case (p, p-2, p-2)
                                if( P + _max( 0, P - 2 ) * 2 <= data[ j ] )
                                {
                                        res ++;
                                        S --;
                                }
                        }
                }

                printf( "Case #%d: %d\n", i, res );
        }
        return 0;
}

