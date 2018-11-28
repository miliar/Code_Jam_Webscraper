#include <cmath>
#include <cstdio>
#include <cstring>

#include <vector>
#include <algorithm>

using namespace std;
typedef long double ldouble;

#define IT 40
#define MAX 105

inline bool lt( ldouble a, ldouble b ) {
  return a + 1e-9 < b;
}
inline bool eq( ldouble a, ldouble b ) {
  return !lt( a, b ) && !lt( b, a );
}
inline bool lte( ldouble a, ldouble b ) {
  return lt( a, b ) || eq( a, b );
}

int T, W, L, U, G;
int x, y;

vector< int > lx, ly, ux, uy;

inline ldouble get_left( ldouble x ) {
  ldouble lx0 = x, ly0;
  ldouble ux0 = x, uy0;
  int llast;
  int ulast;
  
  for( int i = 0; i < L-1; ++i ) {
    if( lte( lx[i], x ) && lte( x, lx[i+1] ) ) {
      ldouble k = ldouble( ly[i]-ly[i+1] )/ldouble( lx[i]-lx[i+1] );
      ldouble l = ly[i] - k*lx[i];
      ly0 = k*x + l;
      llast = i;
      break;
    }
  }
  
  for( int i = 0; i < U-1; ++i ) {
    if( lte( ux[i], x ) && lte( x, ux[i+1] ) ) {
      ldouble k = ldouble( uy[i]-uy[i+1] )/ldouble( ux[i]-ux[i+1] );
      ldouble l = uy[i] - k*ux[i];
      uy0 = k*x + l;
      ulast = i;
      break;
    }
  }

  ldouble area = 0.0;

  for( int i = 0; i < llast; ++i ) 
    area += lx[i]*ly[i+1] - ly[i]*lx[i+1];

  area += lx[llast]*ly0 - ly[llast]*lx0;
  area += lx0*uy0 - ly0*ux0;
  area += ux0*uy[ulast] - uy0*ux[ulast];

  for( int i = ulast; i > 0; --i )
    area += ux[i]*uy[i-1] - uy[i]*ux[i-1];

  area = fabs( area );
  
  return area;
}

inline ldouble get_x( ldouble a0 ) {
  ldouble lo = 0.0, hi = W, mid;

  for( int it = 0; it < IT; ++it ) {
    mid = 0.5*( lo + hi );
    if( lt( get_left( mid ), a0 ) ) lo = mid + 1e-9;
    else hi = mid;
  }

  return lo;
}

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    lx.clear();
    ly.clear();
    ux.clear();
    uy.clear();
    scanf( "%d%d%d%d", &W, &L, &U, &G );

    for( int i = 0; i < L; ++i ) {
      scanf( "%d%d", &x, &y );
      lx.push_back( x );
      ly.push_back( y );
    }
    
    for( int i = 0; i < U; ++i ) {
      scanf( "%d%d", &x, &y );
      ux.push_back( x );
      uy.push_back( y );
    }

    if( ux[0] == 0 ) {
      lx.insert( lx.begin(), ux[0] );
      ly.insert( ly.begin(), uy[0] );
      ++L;
    }
    else {
      ux.insert( ux.begin(), lx[0] );
      uy.insert( uy.begin(), ly[0] );
      ++U;
    }

    if( ux[U-1] == W ) {
      lx.insert( lx.end(), ux[U-1] );
      ly.insert( ly.end(), uy[U-1] );
      ++L;
    }
    else {
      ux.insert( ux.end(), lx[L-1] );
      uy.insert( uy.end(), ly[L-1] );
      ++U;
    }

    ldouble area = 0.0;

    for( int i = 0; i < L-1; ++i ) 
      area += lx[i]*ly[i+1] - ly[i]*lx[i+1];

    for( int i = U-1; i > 0; --i )
      area += ux[i]*uy[i-1] - uy[i]*ux[i-1];

    area = fabs( area );

    ldouble fract = area / G;

    printf( "Case #%d:\n", tc );

    for( int i = 1; i <= G-1; ++i ) 
      printf( "%.6Lf\n", get_x( fract*i ) );
  }

  return 0;
}
