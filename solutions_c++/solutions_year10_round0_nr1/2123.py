#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 32

int n, k;
int state[ MAXN ];

int period( int x ){
  if( x == 0 ) return 1;
  memset( state, 0, sizeof state );
  int ret = 0;
  for( ret = 0; ; ++ret ){
    for( int i = 0; i < x; ++i ){
      state[i] ^= 1;
      if( state[i] == 1 ) break;
    }
    
    int dalje = 0;
    for( int i = 0; i < x; ++i )
      if( state[i] == 0 ) dalje = 1;
    if( dalje ) continue;
    break;
  }
  return ret+2;
}

void run( int x ){
  printf( "Case #%d: ", x ); 
  scanf( "%d%d", &n, &k );

  int n1 = ( n+1 ) >> 1;
  int n2 = n-n1;

  int p1 = period( n1 );
  int p2 = period( n2 );

  int pu = p1 * p2;
  if( k % pu != pu-1 ) printf( "OFF\n" );
  else printf( "ON\n" );
}

int main(){
  int T; scanf( "%d", &T );
  for( int i = 1; i <= T; ++i ) run( i );
  return 0;
}
