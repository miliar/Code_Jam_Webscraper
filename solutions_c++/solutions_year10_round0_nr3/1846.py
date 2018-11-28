#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int MAXN = 1010;

int R, N; // jedino R nije long long

long long k;
long long A[ 2*MAXN ];

long long Lova[ 2*MAXN ];
int End[ 2*MAXN ];

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        scanf( "%d %lld %d", &R, &k, &N );
        printf( "Case #%d: ", counter + 1 );

        long long suma_svih = 0;

        for( int i = 0; i < N; ++i ) {
            scanf( "%lld", A + i );
            A[ i+N ] = A[i];
            suma_svih += A[i];
        }

        if( suma_svih <= k ) {
            printf( "%lld\n", suma_svih * R );
        }
        else {
            for( int start = 0; start < N; ++start ) {
                long long tmp = 0;

                int i; for( i = start; i < 2*N; ++i )
                    if( ( tmp += A[i] ) > k )
                        break;

                End[start] = i;
                Lova[start] = tmp - A[i];
            }

            long long ret = 0;
            int start = 0;

            for( int i = 0; i < R; ++i ) {
                ret += Lova[start];
                if( ( start = End[start] ) >= N ) start -= N;
            }

            printf( "%lld\n", ret );
        }

        fprintf( stderr, "Rijesio sam %d / %d\n", counter+1, T );
    }

    return (0-0);
}
