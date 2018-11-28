#include <cstdio>
#include <algorithm>
#include <fstream>

#define KONJ 42 - 42
#define inf 1000000000

using namespace std;

FILE *fin = fopen( "candy.in", "r" );
FILE *fout = fopen ( "candy.txt", "w" );

int T, N;

void solve( int t ){

    fscanf( fin, "%d", &N );
    int mini = inf, tmp, _sum = 0, sum = 0;

    for ( int i = 0; i < N; ++i ){
        fscanf( fin, "%d", &tmp );
        _sum ^= tmp; mini = min( mini, tmp ); sum += tmp;
    }

    if ( _sum != 0 ){ fprintf( fout, "Case #%d: NO\n", t ); return; }
    fprintf( fout, "Case #%d: %d\n", t, sum - mini );

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );

    return KONJ;

}
