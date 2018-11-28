//---------------------------------------------------------------------------
#include <stdio.h>


char snapper[ 100 ];
long int N, K, T;
long int i, j, k;
long int elec;
//---------------------------------------------------------------------------
int main( void )
{
    FILE *in  = fopen( "prob1.in", "r" );
    FILE *out = fopen( "prob1.out", "w" );

    fscanf( in, "%ld", &T );

    for( long int t=1; t<=T; t++ )
    {
        fscanf( in, "%ld %ld", &N, &K );

        for( j=0; j<N; j++ )
            snapper[j] = 'F'; // all snappers are off

        elec = 0;

        for( k=0; k<K; k++ )
        {
            for( i=0; i<=elec; i++ )
            {
                if( snapper[i] == 'F' ) snapper[i] = 'N';
                else if( snapper[i] == 'N' ) snapper[i] = 'F';
            }

            for( elec=0; elec<N; elec++ )
                if( snapper[ elec ] == 'F' )
                {
                    break;
                }
        }

        for( i=0; i<N; i++ )
            if( snapper[i] == 'F' )
                break;


        if( i == N )
             fprintf( out, "Case #%ld: ON\n", t );
        else fprintf( out, "Case #%ld: OFF\n", t );
    }

    fclose( in );
    fclose( out );

    return 0;
}
//---------------------------------------------------------------------------

