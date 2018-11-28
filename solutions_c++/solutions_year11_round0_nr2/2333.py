#include <cstdio>
#include <cstring>
#include <fstream>

#define KONJ 42 - 42

using namespace std;

FILE *fin = fopen( "Magicka.in", "r" );
FILE *fout = fopen( "Magicka.txt", "w" );

int T, N;
bool opposed[30][30];
int combine[30][30];

void solve( int t ){

    memset( opposed, false, sizeof opposed );
    memset( combine, -1, sizeof combine );

    fscanf( fin, "%d", &N );
    for ( int i = 0; i < N; ++i ){
        char x[5]; fscanf( fin, "%s", x ); // printf( "%s\n", x );
        combine[ x[0] - 'A' ][ x[1] - 'A' ] = combine[ x[1] - 'A' ][ x[0] - 'A' ] = x[2];
    }

    fscanf( fin, "%d", &N );
    for ( int i = 0; i < N; ++i ){
        char x[5]; fscanf( fin, "%s", x );
        opposed[ x[0] - 'A' ][ x[1] - 'A' ] = opposed[ x[1] - 'A' ][ x[0] - 'A' ] = true;
    }

    char s[105], sol[105];
    fscanf( fin, "%d%s", &N, s );

    int cnt = 0;
    for ( int i = 0; i < N; ++i ){

        if ( cnt == 0 ){ sol[cnt++] = s[i]; continue; }
        if ( combine[ sol[ cnt - 1 ] - 'A' ][ s[i] - 'A' ] != -1 ){ sol[cnt - 1] = combine[ sol[ cnt - 1 ] - 'A' ][ s[i] - 'A' ]; continue; }

        for ( int j = 0; j < cnt; ++j ){
            if ( opposed[ sol[j] - 'A' ][ s[i] - 'A' ] ){ cnt = 0; break; }
        } if ( cnt == 0 ) continue;

        sol[cnt++] = s[i];
    }

    fprintf( fout, "Case #%d: [", t );
    for ( int i = 0; i < cnt - 1; ++i ){ fprintf( fout, "%c, ", sol[i] ); }
    if ( cnt != 0 ) fprintf( fout, "%c", sol[cnt - 1] );
    fprintf( fout, "]\n" );

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );

    return KONJ;

}
