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

long long n, m, a, c;
long long Y;

long long solve( long long A ) {
  long long l = 0, d = m, s = ( l + d ) / 2, ret;
  //  printf( "pokusavam rjesiti ako mi je jedan krak duzine %lld\n", A );
  while( l < d ) {
    s = ( l + d ) / 2;
    ret = A * s;
    if( ret == a ) { 
      Y = s;
      return ret;
    }

    if( ret < a ) l = s + 1;
    else d = s - 1;
  }

  if( A * l == a ) { Y = l; return l; }
  if( A * d == a ) { Y = d; return l; }
  return -1;
}

inline long long ccw( long long X1, long long Y1, long long X2, long long Y2, long long X3, long long Y3 ) {
  return X1 * ( Y2 - Y3 ) + X2 * ( Y3 - Y1 ) + X3 * ( Y1 - Y2 );
}

int main( void ) {
  scanf ( "%lld", &c );
  for( int tare = 0; tare < c; ++tare ) {
    printf( "Case #%d: ", tare + 1 );
    
    scanf( "%lld%lld%lld", &n, &m, &a );
//     long long l;
//     for( l = 0LL; l <= n; ++l )
//       if( solve( l ) != -1LL ) 
//         break;
    
//     if( l * Y == a ) printf( "%lld %lld %lld %lld %lld %lld\n", 0LL, 0LL, 0LL, l, Y, 0LL );
//     else printf( "IMPOSSIBLE\n" );
    
    long long x1, y1, x2, y2;
    bool b = 1;

    for( x1 = 0; b && x1 <= n; ++x1 )
      for( y1 = 0; b && y1 <= m; ++y1 )
        for( x2 = 0; b && x2 <= n; ++x2 )
          for( y2 = 0; b && y2 <= m; ++y2 ) {
            //            printf( "0,0 %lld,%lld %lld,%lld --> %lld\n", x1, y1, x2, y2, ccw( 0, 0, x1, y1, x2, y2 ) );
            if( ccw( 0, 0, x1, y1, x2, y2 ) == a )
              b = 0;
          }
    
    --x1; --y1; --x2; --y2;
    //    printf( "0,0 %lld,%lld %lld,%lld --> %lld\n", x1, y1, x2, y2, ccw( 0, 0, x1, y1, x2, y2 ) );

    if( b ) printf( "IMPOSSIBLE\n" );
    else printf( "0 0 %lld %lld %lld %lld\n", x1, y1, x2, y2 );
  }

  return NULA;
}
