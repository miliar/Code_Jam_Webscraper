#include <iostream>
#include <cstdio>

using namespace std;

char a [ 200 ] [ 200 ];
int gamesPlayed [ 200 ], gamesWon [ 200 ];
double wp [ 200 ], owp [ 200 ], oowp [ 200 ], rpi [ 200 ];

int main(){
    freopen ( "input.txt", "rt", stdin );
    freopen ( "output.txt", "wt", stdout );
    int n, t, i, j, k;
    cin >> t;
    for ( k = 1; k <= t; ++ k ){
        cin >> n;
        for ( i = 0; i < n; ++ i ){
            for ( j = 0; j < n; ++ j ){
                cin >> a [ i ] [ j ];
            }
        }
        for ( i = 0; i < n; ++ i ){
            gamesPlayed [ i ] = gamesWon [ i ] = wp [ i ] = owp [ i ] = oowp [ i ] = rpi [ i ] = 0;
        }
        for ( i = 0; i < n; ++ i )
            for ( j = 0; j < n; ++ j ){
                if ( a [ i ] [ j ] == '1' ){
                    gamesWon [ i ] ++;
                }
                if ( a [ i ] [ j ] == '1' || a [ i ] [ j ] == '0' ){
                    gamesPlayed [ i ] ++;
                }
                else if ( a [ i ] [ j ] == '.' ){

                }
                else cout << "Error!!!";
            }
        for ( i = 0; i < n; ++ i )
            wp [ i ] = (double)gamesWon [ i ] / (double)gamesPlayed [ i ];
        for ( i = 0; i < n; ++ i ){
            for ( j = 0; j < n; ++ j ){
                if ( a [ i ] [ j ] != '.' && j != i ){
                    owp [ i ] += ( ( double ) ( gamesWon [ j ] - ( a [ i ] [ j ] == '0' ? 1 : 0 ) )
                    / ( double ) ( gamesPlayed [ j ] - 1 ) );
                }
            }
            owp [ i ] /= (double) gamesPlayed [ i ];
        }
        for ( i = 0; i < n; ++ i ){
            for ( j = 0; j < n; ++ j ){
                if ( a [ i ] [ j ] != '.'  && i != j ){
                    oowp [ i ] += owp [ j ];
                }
            }
            oowp [ i ] /= (double) gamesPlayed [ i ];
        }
        for ( i = 0; i < n; ++ i ){
            rpi [ i ] = wp [ i ] / 4.0 + owp [ i ] / 2.0 + oowp [ i ] / 4.0;
        }
        printf ( "Case #%d:\n", k );
        for ( i = 0; i < n; ++ i )
            printf ( "%.9lf\n", rpi [ i ] );
    }
    return 0;
}
