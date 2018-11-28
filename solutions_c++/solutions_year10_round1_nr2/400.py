#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int INF = 100000005;

int N, D, I, M;
int s[105];
int dp[256][256]={};
int cnt[256];

inline int Abs( int a ) {
    return a >= 0 ? a : -a;
}

inline int Min( int a, int b ) {
    return a < b ? a : b;
}

inline int Cost( int a, int b ) {
    if ( a == b ) return 0;
    else return ( ( Abs( a - b ) - 1 ) / M ) * I;
}

int main() {
    int t, casN, i, j, k, a, sum, ans;
    
    scanf("%d", &t);
    
    for ( casN=1; casN<=t; casN++ ) {
        
        scanf("%d%d%d%d", &D, &I, &M, &N);
        
        if ( M == 0 ) {
            
            for ( i=0; i<256; i++ ) {
                cnt[i] = 0;
            }
            for ( i=1; i<=N; i++ ) {
                scanf("%d", &s[i] );
                cnt[ s[i] ]++;
            }
            ans = INF;
            for ( j=0; j<256; j++ ) {
                sum = 0;
                for ( i=0; i<256; i++ ) {
                    sum += cnt[i] * Min( D, Abs( i - j ) );
                }
                if ( sum < ans ) ans = sum;
            }
            
        } else {
            
            for ( i=1; i<=N; i++ ) {
                scanf("%d", &s[i] );
                for ( j=0; j<256; j++ ) {
                    dp[i][j] = INF;
                }
            }
            
            for ( i=1; i<=N; i++ ) {
                for ( k=0; k<256; k++ ) {
                    for ( j=0; j<i; j++ ) {
                        for ( a=0; a<256; a++ ) {
                            dp[i][k] = Min( dp[i][k], dp[j][a] + Abs( k - s[i] ) + Cost( a, k ) + D * ( i-j - 1 ) );
                        }
                    }
                }
            }
            
            ans = D * N;
            for ( i=0; i<256; i++ ) {
                ans = Min( ans, dp[N][i] );
            }
            
        }
        
        printf("Case #%d: %d\n", casN, ans);
        
    }

    //system("Pause");
    return 0;
}
