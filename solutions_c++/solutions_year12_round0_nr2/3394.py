#include <cstdio>
#include <algorithm>
using namespace std;

int t, n, s, p;
int c, sc;
int ti, y;

int main(){

    FILE* out = fopen( "output.txt", "w" );

    scanf( "%d", &t );

    for( int a = 1; a <= t; a++ ){
        scanf( "%d%d%d", &n, &s, &p );

        //printf( "%d %d %d", n, s, p );

        y = 0;

        c = max( 2 * ( p - 1 ), 0 ) + p;
        sc = max( 2 * ( p - 2 ), 0 ) + p;

        for( int b = 0; b < n; b++ ){
            scanf( "%d", &ti );

            if( ti >= c ){
                y++;
                continue;
            }

            if( ti >= sc && s > 0 ){
                y++;
                s--;
                continue;
            }
        }

        if( a != 1 ) fprintf( out, "\n" );
        fprintf( out, "Case #%d: %d", a, y );

//        printf( "\n" );

    }

}
