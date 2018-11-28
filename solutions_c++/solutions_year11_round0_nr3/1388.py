#include <cstdio>
#include <algorithm>

using namespace std;

void solve(){
    int N;

    int a[1024];

    scanf ( "%d", &N );

    int x = 0;

    for ( int i = 0; i < N; ++i ){
        scanf ( "%d", a + i );
        x ^= a[i];
    }

    if ( x ){
        printf ( "NO\n" );
        return;
    }

    sort ( a, a + N );

    int sum = 0;

    for ( int i = 1; i < N; ++i )
        sum += a[i];

    printf ( "%d\n", sum );
}
int main(){
    int tests;

    scanf ( "%d", &tests );

    for ( int i = 0; i < tests; ++i ){
        printf ( "Case #%d: ", i + 1 );
        solve();
    }
}
