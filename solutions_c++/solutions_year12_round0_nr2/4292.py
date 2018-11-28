#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int BR[2][50];

bool comp( const int &a, const int &b ) {
    if ( BR[0][a] == BR[0][b] ) return a < b;
    return BR[0][a] < BR[0][b];
}

int main() {

    memset( BR, -1, sizeof(BR) );
    for( int i=0; i<=10; i++ ) {
        for( int j=i; j<=10; j++ ) {
            for( int k=j; k<=10; k++ ) {

                int d1 = max( i, j ) - min( i, j );
                int d2 = max( i, k ) - min( i, k );
                int d3 = max( j, k ) - min( j, k );

                int dall = max( d1, max(d2, d3) );

                if ( dall > 2 ) continue;
                if ( dall <= 1 ) dall = 0;
                else dall = 1;


                int nm = max( i, max( j, k ) );

                BR[dall][ i + j + k ] = max( BR[dall][ i + j + k ], nm );

            }
        }
    }

    int ntc, T[120];
    scanf("%d", &ntc);
    
    for( int TC=1; TC<=ntc; TC++ ) {
        int S, P, N;
        
        scanf("%d %d %d", &N, &S, &P);

        for( int i=0; i<N; i++ ) scanf("%d", &T[i]);

        sort( T, T+N, comp );

        int ans = 0;
        for( int i=N-1; i>=0; i-- ) {
            if ( BR[0][T[i]] >= P ) {
                ans++;
            } else {
                if ( S > 0 && ( BR[0][T[i]] < BR[1][T[i]] ) ) {
                    if ( BR[1][T[i]] >= P ) {
                        ans++;
                        S--;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", TC, ans);
    }
    return 0;
}
