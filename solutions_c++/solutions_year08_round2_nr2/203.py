#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>

#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <functional>

#include <cmath>
#include <cstring>
#include <ctime>
using namespace std;
const int NULA = 0;

struct union_find {
private:
  struct node { int parent, height; };
  vector< node > V;

public:
  union_find( void ) : V( vector< node >() ) {}
  union_find( int size ) : V( vector< node >( size ) ) {}

  void MakeSet( int x ) {
    if( (int)V.size() <= x ) V.resize( x + 1 );
    V[x].parent = x;
    V[x].height = 0;
  }

  int Find( int x ) {
    if( V[x].parent == x ) return x;
    return V[x].parent = Find( V[x].parent );
  }

  bool Union( int x, int y ) {
    int xRoot = Find( x );
    int yRoot = Find( y );
    if( xRoot == yRoot ) 
      return 0;
    
    if( V[ xRoot ].height > V[ yRoot ].height ) V[ yRoot ].parent = xRoot;
    else if( V[ xRoot ].height < V[ yRoot ].height ) V[ xRoot ].parent = yRoot;
    else { V[ yRoot ].parent = xRoot; ++V[ xRoot ].height; }
    
    return 1;
  }
  
  int count( int start, int end ) {
    int ret = 0;
    for( int i = start; i <= end; ++i ) 
      if( V[ i ].parent == i )
        ++ret;
    return ret;
  }
};

vector< int > prime;
inline void sito( int granica ) {
  int i, j;
  static char *polje;
  polje = (char*) malloc( granica + 1 );
  memset( polje, 0, ( granica + 1 ) * sizeof( char ) );

  prime.clear();
  prime.reserve( granica / 10 );
  prime.push_back( 2 );

  for( i = 3; i < granica; i += 2 ) {
    if( polje[ i ] ) continue;
    for( j = 2; i * j < granica; ++j )
      polje[ i * j ] = 1;
    prime.push_back( i );
  }
} 

int A, B, C, P;
union_find U;

inline int greatest_prime_factor( int x ) {
  vector< int >::iterator start = lower_bound( prime.begin(), prime.end(), x );
  for( ; start+1 != prime.begin(); --start ) 
    if( x % *start == 0 )
      return *start;
  return 1;
}

int main( void ) {
  scanf ( "%d", &C );
  sito( 10000 );

  for( int c = 0; c < C; ++c ) {
    int ret = -1;
    scanf( "%d%d%d", &A, &B, &P );
    U = union_find( B );
    for( int i = 1; i <= B; ++i )
      U.MakeSet( i );

    for( int i = A; i <= B; ++i )
      for( int j = i+1; j <= B; ++j )
        if( greatest_prime_factor( __gcd( i, j ) ) >= P )
          U.Union( i, j );
    
    ret = U.count( A, B ); 
    printf( "Case #%d: %d\n", c + 1, ret );
  }

  return NULA;
}
