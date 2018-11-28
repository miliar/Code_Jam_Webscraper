#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int D[1 << 14], L[1 << 14], N, F;
int dp[1 << 14];

void scan(){
    scanf ( "%d", &N );

    for ( int i = 0; i < N; ++i )
        scanf ( "%d%d", D + i, L + i );

    scanf ( "%d", &F );
}

inline int MIN ( int t1,int t2 ){
    return ( t1 < t2 ) ? t1 : t2;
}
int dist ( int idx1, int idx2 ){
    if ( idx2 == -1 )
        return -1e9;

    int ll = MIN ( D[idx2] - D[idx1], L[idx2] );

    return D[idx2] + ll;
}

void print ( int cs, string res ){
    cout << "Case #" << cs << ": " << res << endl;
}

long long dist ( long long x1, long long y1, long long x2, long long y2 ){
    return ( x2 - x1 ) * ( x2 - x1 ) + ( y2 - y1 ) * ( y2 - y1 );
}
void solve ( int cs ){
    int idx = 0, curL = D[0];
    dp[0] = curL;
    int ok = 0;
    for ( int i = 0; i < N; ++i ){
        for ( int j = i + 1; j < N; ++j )
            if ( D[j] - D[i] <= dp[i] ){
                dp[j] = max ( dp[j], dist ( i, j ) - D[j] );

            }
        if ( D[i] + dp[i] >= F ){
            ok = 1;
        }
//cout << D[i] << " " << dp[i] << endl;
    }

    if ( ok )
        print ( cs, "YES" );
    else
        print ( cs, "NO" );
    memset ( dp, 0, sizeof ( dp ) );

}
int main(){
    int tests;

    cin >> tests;

    for ( int i = 1; i <= tests; ++i ){
        scan();
        solve ( i );
    }
}
