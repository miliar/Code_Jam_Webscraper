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

int N, n;
long long X[ 102 ], Y[ 102 ];
long long A, B, C, D, M, X0, Y0;

int main( void ) {
  scanf ( "%d", &N );
  for( int it = 0; it < N; ++it ) {
    long long ret = 0;
    scanf( "%d%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &X0, &Y0, &M ); 
    
    for( int i = 0; i < n; ++i ) {
      X[ i ] = X0;
      Y[ i ] = Y0;
      X0 = ( A * X0 + B ) % M;
      Y0 = ( C * Y0 + D ) % M;
    }
    
    for( int i = 0; i < n; ++i ) 
      for( int j = i+1; j < n; ++j ) 
        for( int k = j+1; k < n; ++k ) 
          if( ( X[ i ] + X[ j ] + X[ k ] ) % 3 == 0 && ( Y[ i ] + Y[ j ] + Y[ k ] ) % 3 == 0 ) 
            ++ret;
    
    printf( "Case #%d: %lld\n", it + 1, ret );
  }


  return NULA;
}
