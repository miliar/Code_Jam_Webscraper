#include <cstdio>
#include <cstring>
#include <fstream>
#include <cmath>

#define KONJ 42 - 42
#define eps 0.00000001

using namespace std;

FILE *fin = fopen( "B.in", "r" );
FILE *fout = fopen( "B.out", "w" );

struct vendor{
    int q, pos;
} niz[220];

int T, C, D;

bool greedy( double val ){

    double start = niz[0].pos - val;
    for ( int i = 0; i < C; ++i ){
        for ( int j = 0; j < niz[i].q ; ++j ){
            if ( i == 0 && j == niz[i].q - 1 ) continue;
            start += D; if ( start < niz[i].pos ){ start = max( start, niz[i].pos - val ); continue; }
            if ( abs( start - niz[i].pos ) > val ) return false;
        }
    }

    return true;

}

double binary( double lo, double hi ){

    double ret = 0;

    while( fabs( lo - hi ) > eps ){
        double mid = ( lo + hi ) / 2;
        if ( greedy( mid ) ){ hi = ret = mid; } else { lo = mid; }
    }

    return ret;

}

void solve( int t ){

    fscanf( fin, "%d%d", &C, &D );
    for ( int i = 0; i < C; ++i ){
        fscanf( fin, "%d%d", &niz[i].pos, &niz[i].q );
    }

    //printf( "%d\n", greedy( 0 ) );
    fprintf( fout, "Case #%d: %.10lf\n", t, binary( 0, (double) 100000000 ) );

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );

    return KONJ;

}
