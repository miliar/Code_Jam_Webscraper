#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int N , d[ 11111 ] , l[ 11111 ] , D , VAL[ 11111 ];

int main(){
  freopen( "f.out" , "w" , stdout );
  FILE *in = fopen( "A-large (2).in" , "r" );
  int T;
  fscanf( in , "%d" ,&T );
  for( int kase = 1 ; kase <= T ; kase++ ){
    fscanf( in , "%d" ,&N );
    for( int q = 0 ; q < N ; q++ ){
      fscanf( in , "%d%d" ,&d[ q ] ,&l[ q ] );
    }
    memset( VAL , 0 , sizeof VAL );
    VAL[ 0 ] = d[ 0 ];
    fscanf( in , "%d" ,&D );
    
    for( int q = 0 ; q < N ; q++ ){
      for( int w = q + 1 ; w < N ; w++ ){
	if( d[ w ] - d[ q ] > VAL[ q ] ) break;
	VAL[ w ] = max( VAL[ w ] , min( l[ w ] , d[ w ] - d[ q ] ) );
      }
    }
    
    bool Can = 0;
    for( int q = 0 ; q < N ; q++ ){
      if( D - d[ q ] <= VAL[ q ] ){
	Can = 1;
	break;
      }
    }
    
    printf( "Case #%d: %s\n" ,kase ,Can ? "YES" : "NO" );
  }
  
  return 0;
}
