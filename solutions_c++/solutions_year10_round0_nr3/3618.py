//---------------------------------------------------------------------------
#include <stdio.h>

using namespace std;

long int R, K, N, T;
long int i, t, j, count, next;
long int money;
long int k, front;

long int G[ 2000 ];
//---------------------------------------------------------------------------
int main( void )
{
    FILE *in  = fopen( "prob2.in", "r" );
    FILE *out = fopen( "prob2.out", "w" );

    fscanf( in, "%ld", &T );

    for( t=1; t<=T; t++ )
    {
        fscanf( in, "%ld %ld %ld", &R, &K, &N );
        money = 0;

        for( i=0; i<N; i++ )
            fscanf( in, "%ld", &G[i] );

        asm nop;

        i = 0; count = 0;

        for( j=0; j<R; j++ )
        {
            count = 0;
            for( k=K; k>=0; )
            {
                if( k < G[i] ) break;
                if( count == N ) break;

                k -= G[i];
                money += G[i];
                if( ++i >= N ) i = 0;

                count++;
            }
        }

        fprintf( out, "Case #%d: %ld\n", t, money );
    }

    fclose( in );
    fclose( out );

    return 0;
}
//---------------------------------------------------------------------------
