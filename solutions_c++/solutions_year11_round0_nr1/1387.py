#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdio>

using namespace std;


int ABS ( int x ){
    return ( x < 0 ) ? (-x) : x;
}
void solve(){
    int N;

    pair <char, int> a[128];

    cin >> N;

    for ( int i = 0; i < N; ++i )
        cin >> a[i].first >> a[i].second;

    int dp[128];

    memset ( dp, 0, sizeof ( dp ) );

    int x[256];
    int t[256];

    x[ 'O' ] = x[ 'B' ] = 1;
    t[ 'O' ] = t[ 'B' ] = 0;

    t[ a[0].first ] = x[ a[0].first ] = dp[0] = a[0].second;

    for ( int i = 1; i < N; ++i ){
        t[ a[i].first ] = dp[i] = max ( dp[i - 1], t[ a[i].first ] + ABS ( a[i].second - x[ a[i].first ] ) ) + 1;
        x[ a[i].first ] = a[i].second;

    //    cout << x[ 'O' ] << " " << t[ 'O' ] << " " << x[ 'B' ] << " " << t[ 'B' ] << endl;
    }

    cout <<  dp[N - 1] << endl;
}

int main(){
    int tests;

    scanf ( "%d", &tests );

    for ( int i = 0; i < tests; ++i ){
        printf ( "Case #%d: ", i + 1 );
        solve();
    }
}
