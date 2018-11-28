#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cctype>
using namespace std;

//int zauzetR[512];
//int zauzetC[512];
int R, C;
int koliko[512];

int tabla[32][32];
int bio[32][32];

int main( void ) {

  int test; scanf( "%d", &test );
  
  for( int cs = 1; cs <= test; ++cs ) {
      scanf( "%d%d", &R, &C );
      
      for( int i = 0; i < R; ++i ) {
          char buff[100]; scanf( "%s", buff );
          int mask = 0;
          for( int j = 0; buff[j]; ++j ) {
            mask = mask * 16;
            if( isdigit( buff[j] ) ) mask += buff[j] - '0';
            else		     mask += buff[j] - 'A' + 10;
          }
          for( int j = C-1; j >= 0; --j ) tabla[i][C-1-j] = ( mask >> j ) & 1;
      }
   
//      for( int i = 0; i < R; ++i, puts( "" ) ) 
//        for( int j = 0; j < C; ++j )
//          printf( "%c", tabla[i][j] ? '.' : 'X' );     


      memset( bio, 0, sizeof bio );
      memset( koliko, 0, sizeof koliko );
         
      for( int velicina = min( R, C ); velicina >= 1; --velicina ) {
        for( int r = 0; r < R; ++r ) 
          for( int c = 0; c < C; ++c ) {
            int prvo   = tabla[r][c];
            int drugo  = 1-prvo;
            int prvomask = 0;
            int drugomask = 0;
            int ok     = 1;
            
            if( r + velicina > R ) continue;
            if( c + velicina > C ) continue;
            
            for( int plus = 0; plus < velicina; ++plus )  {
//              int dokler = r + plus;
//              int dokles = s + plus;
              
              prvomask = prvomask * 2 + prvo;
              drugomask = drugomask * 2 + drugo;
              
              int redmask = 0;
              for( int i = c; i <= c+plus; ++i ) {
                if( bio[r+plus][i] ) ok = 0;
                redmask = redmask * 2 + tabla[r+plus][i];
//                if( r == 0 && c == 13 ) printf( ":: %x %d\n", redmask, velicina );
              }
              
              int colmask = 0;
              for( int i = r; i <= r+plus; ++i ) {
                if( bio[i][c+plus] ) ok = 0;
                colmask = colmask * 2 + tabla[i][c+plus];
              }
              
//              if( r == 0 && c == 13 ) 
//                printf( "%x %x %x\n", prvomask, redmask, colmask );
                            
              if( prvomask != redmask || prvomask != colmask ) {
//                printf( "%x %x %x\n", prvomask, redmask, colmask );
                ok = 0;
              }
              if( !ok ) break;
              swap( prvomask, drugomask );
              
            }
            
            if( ok ) {
              // oznaci sve koristeno
              for( int i = r; i < r + velicina; ++i ) 
                for( int j = c; j < c + velicina; ++j ) 
                  bio[i][j] = 1;
              ++koliko[velicina];
            }
          }
      }
      
      int br = 0;
      for( int i = 32; i >= 1; --i )
        if( koliko[i] ) ++br;
        
      printf( "Case #%d: %d\n", cs, br );
      for( int i = 32; i >= 1; --i )
        if( koliko[i] ) printf( "%d %d\n", i, koliko[i] );
  }

return 0;
}