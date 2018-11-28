#include <cmath>
#include <cstdio>
#include <cstring>

#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 1005

int T, X, S, R, N;
double t;

int B[ MAXN ];
int E[ MAXN ];
int w[ MAXN ];

struct interval {
  int l, r, w;
  interval( int L, int R, int W ) { l = L; r = R; w = W; }
  inline int len() { return r - l; }
};

inline bool operator<( interval a, interval b ) {
  return ( a.w < b.w );
}

vector< interval > e;

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%d%d%lf%d", &X, &S, &R, &t, &N );

    e.clear();

    for( int i = 0; i < N; ++i ) {
      scanf( "%d%d%d", B+i, E+i, w+i );
      e.push_back( interval( B[i], E[i], w[i] ) );
    }

    if( B[0] != 0 ) e.push_back( interval( 0, B[0], 0 ) );

    for( int i = 0; i < N-1; ++i ) 
      if( E[i] != B[i+1] ) e.push_back( interval( E[i], B[i+1], 0 ) );

    if( E[N-1] != X ) e.push_back( interval( E[N-1], X, 0 ) );

    sort( e.begin(), e.end() );

    double Sol = 0.0;

    for( int i = 0; i < e.size(); ++i ) {
      if( fabs( t ) <= 1e-9 ) t = 0.0;
      double go = min( t*( R + e[i].w ), (double)e[i].len() );
      t -= double( go ) / double( R + e[i].w );
      Sol += double( go ) / double( R + e[i].w ) + double( e[i].len() - go ) / double( S + e[i].w );
    }

    printf( "Case #%d: %.6lf\n", tc, Sol );
  }

  return 0;
}
