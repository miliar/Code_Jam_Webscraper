#include <cstdio>
#include <fstream>

#define KONJ 42 - 42

FILE *fin = fopen( "googleDancingIn.txt", "r" );
FILE *fout = fopen( "googleDancingOut.txt", "w" );

using namespace std;

int T, N, S, K;

void solve( int t ){
     
     fscanf( fin, "%d%d%d", &N, &S, &K );
     
     int sol = 0;
     for ( int i = 0; i < N; ++i ){
         
         int x; fscanf( fin, "%d", &x );
         int _maks;
         
         if ( x % 3 == 0 ) _maks = x / 3;
         if ( x % 3 == 1 ) _maks = ( ( x - 1 ) / 3 ) + 1;
         if ( x % 3 == 2 ) _maks = ( x + 1 ) / 3;
         
         printf( "%d ", _maks );
         
         if ( _maks >= K ) ++sol;
         if ( x % 3 != 1 && _maks == K - 1 && x != 0 && S > 0 ){ ++sol; --S; }
         
     }
     printf( "\n" );
     
     fprintf( fout, "Case #%d: %d\n", t, sol );
     
}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );

    return KONJ;

}
