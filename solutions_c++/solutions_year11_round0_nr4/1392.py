#include <cstdio>
#include <cstring>

using namespace std;

int a[1024], N;
char used[1024];


int f ( int x ){
    int br = 0;

    while ( !used[ x ] ){
     //   printf ( "%d ", x );
        used[ x ] = 1;
        x = a[x];
       // printf ( "%d ", x );
        ++br;
    }
   // printf ( "\n" );

    return br;
}
void solve(){
    memset ( used, 0, sizeof ( used ) );

    scanf ( "%d", &N );

    for ( int i = 1; i <= N; ++i )
        scanf ( "%d", a + i );

    double prob = 0;

    for ( int i = 1; i <= N; ++i )
        if ( !used[i] ){
            double cnt = f ( i );
            if ( cnt > 1.2 )
                prob += cnt;

         //   printf ( "%.5f\n", cnt );
        }
    printf ( "%.6f\n", prob );
}

int main(){
    int tests;

    scanf ( "%d", &tests );

    for ( int i = 0; i < tests; ++i ){
        printf ( "Case #%d: ", i + 1 );
        solve();
    }

}
