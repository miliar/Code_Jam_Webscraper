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

char S[ 1002 ];
char S2[ 1002 ];
int n, k, l;
int A[ 20 ];

inline int koliko( void ) {
  for( int i = 0; i < l; i += k )
    for( int j = 0; j < k; ++j )
      S2[ i + A[ j ] ] = S[ i + j ];
  
  int ret = 1;

  for( int i = 1; i < l; ++i )
    if( S2[ i ] != S2[ i - 1 ] )
      ++ret;

  return ret;
}

int main( void ) {
  scanf( "%d", &n ); 
  
  for( int i = 0; i < n; ++i ) {
    printf( "Case #%d: ", i + 1 );
    scanf( "%d %s", &k, S );
    for( int j = 0; j < k; ++j )
      A[ j ] = j;
    
    l = strlen( S );
    int best = 1234567;
    do { 
      best = min( best, koliko() );
    } while( next_permutation( A, A + k ) );

    printf( "%d\n", best );
  }
  
  return NULA;
}
