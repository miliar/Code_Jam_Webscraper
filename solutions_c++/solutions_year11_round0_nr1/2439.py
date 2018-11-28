#include <cstdio>
#include <cmath>
#include <algorithm>
#include <fstream>

#define KONJ 42 - 42

using namespace std;

FILE *fin = fopen( "botTrust.in", "r" );
FILE *fout = fopen( "botTrust.txt", "w" );

int T, N;

void solve( int t ){

    fscanf( fin, "%d", &N ); int b_time = 0, b_pos = 1, o_time = 0, o_pos = 1;
    for ( int i = 0; i < N; ++i ){
        char x[2]; int togo; fscanf( fin, "%s %d", x, &togo );
        if ( x[0] == 'O' ){
            o_time += abs( o_pos - togo ) + 1;
            o_time = max( o_time, b_time + 1 );
            o_pos = togo;
        } else {
            b_time += abs( b_pos - togo ) + 1;
            b_time = max( b_time, o_time + 1 );
            b_pos = togo;
        }
    }

    fprintf( fout, "Case #%d: %d\n", t, max( b_time, o_time ) );

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i  ) solve( i + 1 );

    return KONJ;

}
