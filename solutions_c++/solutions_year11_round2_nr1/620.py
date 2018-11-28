#include <cstdio>
#include <cstring>
#include <fstream>

#define KONJ 42 - 42

using namespace std;

FILE *fin = fopen( "A.in", "r" );
FILE *fout = fopen( "A.out", "w" );

int T, N;
double WP[105], OWP[105], OOWP[105];
int win[105], game[105];
char grid[105][105];

void solve( int t ){

    fprintf( fout, "Case #%d:\n", t );
    memset( WP, 0, sizeof WP );
    memset( OWP, 0, sizeof OWP );
    memset( OOWP, 0, sizeof OOWP );

    fscanf( fin, "%d", &N );
    for ( int i = 0; i < N; ++i ){
        fscanf( fin, "%s", grid[i] ); int _game = 0, _win = 0;
        for ( int j = 0; j < N; ++j ){
            if ( grid[i][j] != '.' ){ ++_game; }
            if ( grid[i][j] == '1' ){ ++_win; }
        }
        win[i] = _win; game[i] = _game;
        WP[i] = ( double ) _win / (double)_game;
    }

    for ( int i = 0; i < N; ++i ){
        int _game = 0; double nes = 0;
        for ( int j = 0; j < N; ++j ){
            if ( grid[i][j] != '.' ){ ++_game; nes += (double) ( win[j] - ( grid[j][i] == '1' ) ) / ( game[j] - 1 ); }
        }
        OWP[i] = ( double ) nes / (double)_game;
        //printf( "%lf\n", OWP[i] );
    }

    for ( int i = 0; i < N; ++i ){
        int _game = 0; double nes = 0;
        for ( int j = 0; j < N; ++j ){
            if ( grid[i][j] != '.' ){ ++_game; nes += OWP[j]; }
        }
        OOWP[i] = ( double ) nes / (double)_game;
        fprintf( fout, "%.10lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] );
    }

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ){ solve( i + 1 ); }

    return KONJ;

}
