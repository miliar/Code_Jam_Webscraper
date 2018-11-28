#include <cstdio>

int t, a, b;
int num, y;
int n[7];
int d;

int pow[7] = { 1, 10, 100, 1000, 10000, 100000, 1000000 };

int main(){

    FILE* out = fopen( "output.txt", "w" );

    scanf( "%d", &t );

    for( int c = 0; c < t; c++ ){
        scanf( "%d%d", &a, &b );

        y = 0;

        for( d = 1; d < 8; d++ ){
            if( a / pow[d] == 0 ) break;
        }

        for( int x = a; x < b; x++ ){
            for( int z = 0; z < d; z++ ){
                n[z] = ( x / pow[z] ) % 10;
            }

            for( int z = 1; z < d; z++ ){
                num = 0;

                for( int e = 0; e < d; e++ ){
                    num += n[( e + z ) % d] * pow[e];
                }

                if( num > x && num <= b ){
                    y++;
                }
            }
        }

        if( c != 0 ) fprintf( out, "\n" );
        fprintf( out, "Case #%d: %d", c+1, y );
    }
}
