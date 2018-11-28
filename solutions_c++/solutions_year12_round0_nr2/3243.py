#include <iostream>
#include <cstring>

using namespace std;

int ABS ( int x ){
    return ( x < 0 ) ? -x : x;
}

int ok ( int t1, int t2, int t3 ){
    if ( t1 < 0 || t2 < 0 || t3 < 0 ) return 0;
    if ( t1 > 10 || t2 > 10 || t3 > 10 ) return 0;
    if ( ABS ( t1 - t2 ) > 2 || ABS ( t1 - t3 ) > 2 || ABS ( t2 - t3 ) > 2 ) return 0;
    return 1;
}

int special( int t1, int t2, int t3 ){
    return ABS( t1 - t2 ) == 2 || ABS ( t1 - t3 ) == 2 || ABS ( t2 - t3 ) == 2;
}
void solve( int cs ){
    int N, S, a[128], dp[128][128], P;
    memset ( dp, -1, sizeof ( dp ) );

    cin >> N >> S >> P;

    for ( int i = 0; i < N; ++i )
        cin >> a[i];

    dp[0][0] = 0;

    for ( int i = 0; i < N; ++i )
        for ( int j = 0; j <= S; ++j )
            if ( dp[i][j] != -1 ){
            //    cout << i << " " << j << endl;
                for ( int p1 = 0; p1 <= 10; ++p1 )
                    for ( int p2 = 0; p2 <= 10; ++p2 ){
                        int p3 = a[i] - p1 - p2;

                        if ( !ok ( p1, p2, p3 ) )
                            continue;

                        int mx = max ( p1, max ( p2, p3 ) );

                        if ( special ( p1, p2, p3 ) )
                            dp[i + 1][j + 1] = max ( dp[i][j] + ( mx >= P ), dp[i + 1][j] );
                        else
                            dp[i + 1][j] = max ( dp[i][j] + ( mx >= P ), dp[i + 1][j] );
                    }
            }
    cout << "Case #" << cs << ": " << dp[N][S] << endl;
}

int main(){
    int tests;

    cin >> tests;

    for ( int i = 1; i <= tests; ++i )
        solve(i);
}
