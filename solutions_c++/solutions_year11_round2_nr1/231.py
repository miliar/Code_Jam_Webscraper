#include <cstdio>

using namespace std;

    char a[128][128];

    double wp[128], owp[128], oowp[128];

    int N;
    double brall[128];
void solve(){

    scanf ( "%d", &N );

    for ( int i = 0; i < N; ++i )
            scanf ( "%s", a[i] );

    for ( int i = 0; i < N; ++i )
        wp[i] = owp[i] = oowp[i] = brall[i] = 0;


    for ( int i = 0; i < N; ++i ){
        double  brwin = 0;

        for ( int j = 0; j < N; ++j ){
            if ( a[i][j] != '.' ) ++brall[i];
            if ( a[i][j] == '1' ) ++brwin;
        }

        wp[i] = brwin / brall[i];
    }


    for ( int i = 0; i < N; ++i ){
        for ( int j = 0; j < N; ++j )
            if ( a[i][j] != '.' ){

                if ( a[i][j] == '0' )
                    owp[i] += ( ( wp[j] * brall[j] - 1 ) / ( brall[j] - 1 ) );
                else
                    owp[i] += ( wp[j] * brall[j] / ( brall[j] - 1 ) );
            }
        owp[i] /= brall[i];
    }



    for ( int i = 0; i < N; ++i ){
        for ( int j = 0; j < N; ++j )
            if ( a[i][j] != '.' )
                oowp[i] += owp[j];
        oowp[i] /= brall[i];
    }

    for ( int j = 0; j < N; ++j )
        printf ( "%.6f\n", wp[j] / 4. + owp[j] / 2 + oowp[j] / 4 );

}

int main(){
    int tests;
    scanf ( "%d", &tests );
    int br = 0;

    while ( tests -- ){
        ++br;
        printf ( "Case #%d:\n", br );
        solve();
    }
}
