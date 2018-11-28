#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 1008

typedef long long llint;

int r, k, n;
int group[ MAXN ];
int next[ MAXN ];
int sz[ MAXN ];

int bio[ MAXN ];

void run( int test ){
  memset( sz, 0, sizeof sz );
  memset( next, -1, sizeof next );
  
  printf( "Case #%d: ", test );
  scanf( "%d%d%d", &r, &k, &n );
  for( int i = 0; i < n; ++i )
    scanf( "%d", &group[i] );
  
  if( n == 1 ){
    if( group[0] <= k ) printf( "%lld\n", (llint) group[0] * r );
    else printf( "0\n" );
    return;
  }

  for( int i = 0; i < n; ++i ){
    int sum = group[i];
    if( sum > k ){ next[i] = i; continue; }
    for( int j = ( i+1 ) % n; j != i; j = ( j+1 ) % n ){
      sum += group[j];
      if( sum > k ){ sz[i] = sum-group[j]; next[i] = j; break; }
    }
    if( next[i] == -1 ){ next[i] = i; for( int j = 0; j < n; ++j ) sz[i] += group[j]; }
  }
  
  memset( bio, 0, sizeof bio );
  int sad = 0; llint ret = 0;
  while( r > 0 ){
    if( bio[sad] == 1 ) break;
    bio[sad] = 1;
    --r;
    ret += sz[sad];
    sad = next[sad];
  }

  assert( ret >= 0 );

  // ODREDIM CIKLUS
  int cycsz = 0, poc = sad;
  llint cycval = 0;
  do{
    cycval += sz[sad];
    cycsz++;
    sad = next[sad];
  }while( sad != poc );

  ret += cycval * ( r / cycsz );
  r %= cycsz;

  for( int i = poc; r; --r ){
    ret += sz[i];
    i = next[i];
  }

  printf( "%lld\n", ret );
}

int main(){
  int T; scanf( "%d", &T );
  for( int i = 1; i <= T; ++i ) run( i );
  return 0;
}
