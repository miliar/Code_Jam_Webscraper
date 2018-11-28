#include <cassert>
#include <cstdio>
#include <cstring>


int main( void ) {

  int test; scanf( "%d", &test );
  
  
  for( int cs = 1; cs <= test; ++cs ) { 
    
      int R, k, N;
      int g[1000];
      int bio[1000];
      int koliko[1000];
      int next[1000];

      memset( bio, 0, sizeof bio );
      memset( next, -1, sizeof next );
      
      scanf( "%d%d%d", &R, &k, &N );
      for( int i = 0; i < N; ++i ) scanf( "%d", g+i );
      
      
      int pt = 0, rijesio_ciklus = 0, zarada = 0;
      
      while( R > 0 ) {
        
          if( bio[pt] && !rijesio_ciklus && R >= 1000 ) {
            
            //printf( "%d %d %d %d %d\n", R, tajm, diff, app[pt], koliko[pt] );
            int cijena_ciklusa = 0;
            int duljina_ciklusa = 0;
            
            int slj = next[pt];
            do {
              cijena_ciklusa += koliko[slj];
              slj = next[slj];
              ++duljina_ciklusa;
            } while( next[slj] != pt );
            
            //assert( duljina_ciklusa == diff );
            zarada += R/duljina_ciklusa*cijena_ciklusa;
            R %= duljina_ciklusa;
            
            rijesio_ciklus = 1;
          } else {
            
            int board = 0;
            int ja = pt;
            
            bio[ja] = 1;
            
            for( int i = 0; i < N && board + g[pt] <= k; ++i ) {
              board += g[pt++];
              pt %= N;
            }
            
            next[ja] = pt;
            koliko[ja] = board;
            zarada += board;
            --R;
          }
        
      }

      printf( "Case #%d: %d\n", cs, zarada );
  
  }


return 0;

}