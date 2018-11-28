#include <cstdio>
#include <string>
#include <vector>
#include <memory.h>
#include <cstring>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

struct point {
  double x, y;
};

int W, kb, kt, n;
point pb[110], pt[110];

ld getS( int k, point* p, ld xx ) {
//  printf( "getS xx=%.5f\n", (double)xx );
  ld res = 0;
  forn( i, k-1 ) {
//    printf( "%.5f - %.5f\n", double(p[i].x), double(p[i+1].x) );
    if ( p[i+1].x < xx ) {
      res += ( p[i+1].x - p[i].x ) * ( p[i+1].y + p[i].y );
    } else {
      ld c = ( xx - p[i].x ) / ( p[i+1].x - p[i].x );
      ld yy = p[i].y + ( p[i+1].y - p[i].y ) * c;
      res += ( xx - p[i].x ) * ( p[i].y + yy );
      break;
    }
  }
  return res * 0.5;
}

ld getS( ld xx ) {
//  printf( "getS up = %.5f\n", (double)getS( kt, pt, xx ) );
//  printf( "getS down = %.5f\n", (double)getS( kb, pb, xx ) );
  return getS( kt, pt, xx ) - getS( kb, pb, xx );
}

void solve() {
  scanf( "%d %d %d %d", &W, &kb, &kt, &n );

  double my = 1e9;

  forn( i, kb ) {
    scanf( "%lf %lf", &pb[i].x, &pb[i].y );
    if ( pb[i].y < my ) my = pb[i].y;
  }
  forn( i, kt ) {
    scanf( "%lf %lf", &pt[i].x, &pt[i].y );
    if ( pt[i].y < my ) my = pt[i].y;
  }

//  forn( i, kb ) { pb[i].y -= my; printf( "%.5f %.5f\n", pb[i].x, pb[i].y ); }
//  forn( i, kt ) { pt[i].y -= my; printf( "%.5f %.5f\n", pt[i].x, pt[i].y ); }
  forn( i, kb ) pb[i].y -= my;
  forn( i, kt ) pt[i].y -= my;

  ld total = getS( W );

//  printf( "total = %.5f\n", (double)total );

  forn( i, n-1 ) {
    ld cur = total / n * (i+1);

    ld l = 0, r = W, m;
    forn( i, 300 ) {
      m = ( l+r ) * 0.5;
      if ( getS( m ) > cur ) r = m;
      else l = m;
    }

    printf( "%.10f\n", (double)( (l+r) * 0.5 ) );
  }
}

int main()
{
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    printf( "Case #%d:\n", q );
    solve();
  }
  return 0;
}