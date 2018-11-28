#include <cstdio>
#include <cstring>
#include <fstream>

#define KONJ 42 - 42

FILE *fin = fopen( "googleSpeakIn.txt", "r" );
FILE *fout = fopen( "googleSpeakOut.txt", "w" );

using namespace std;

int T;

char s[110];
char key[] = "ynficwlbkuomxsevzpdrjgthaq";

int find( char c ){
    for ( int i = 0; i < 26; ++i ){
        if ( key[i] == c ) return i;
    }
}

void solve( int t ){

     if ( t == 1 ) fgets( s, 101, fin );
     
     fprintf( fout, "Case #%d: ", t );
     fgets( s, 110, fin ); int len = strlen( s );
     
     printf( "%d %s\n", len, s );
     
     for ( int i = 0; i < len - 1; ++i ){
         //printf( "%c", s[i] ); 
         if ( s[i] == ' ' ) fprintf( fout, " " ); else fprintf( fout, "%c", 'a' + find( s[i] ) );
     }
     
     fprintf( fout, "\n" );   

}

int main( void ){

    fscanf( fin, "%d", &T );
    for ( int i = 0; i < T; ++i ) solve( i + 1 );
    
    return KONJ;

}
