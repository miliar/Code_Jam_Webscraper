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

int x, s, r, n, b[1010], e[1010], w[1010], p[1010];

bool cmp( int i, int j ) {
  return b[i] < b[j];
}

void solve() {
  int tt;
  scanf( "%d %d %d %d %d", &x, &s, &r, &tt, &n );
  ld t = tt;
  forn( i, n ) {
    scanf( "%d %d %d", &b[i], &e[i], &w[i] );
    p[i] = i;
  }

  sort( p, p+n, cmp );

  vector<pii> seg;
//  vector< pair<int, ld> > aseg;
  vector<ld> zseg;
  int lp = 0;
  forn( qi, n ) {
    int i = p[qi];
    if ( b[i] > lp ) {
      seg.pb( pii( s, b[i] - lp ) );
    }
    seg.pb( pii( s + w[i], e[i] - b[i] ) );
    lp = e[i];
  }
  if ( lp < x ) seg.pb( pii( s, x - lp ) );

  sort( seg.begin(), seg.end() );

  int first = 0;
  forn( i, seg.size()+1 ) {
    first = i;
    if ( fabs( t ) < 1e-7 || i == (int)seg.size() ) break;
    ld ctime = (ld)seg[i].second / (ld)( seg[i].first - s + r );
    ld rtime = min( t, ctime );
//    aseg.pb( pii( seg[i].first + r - s, rtime ) );
//    aseg.pb( pii( seg[i].first, ( seg[i].second - ( (seg[i].first + r - s) * rtime ) ) / seg[i].first ) );
    zseg.pb( rtime );
    zseg.pb( ( seg[i].second - ( seg[i].first + r - s ) * rtime ) / seg[i].first );
    t -= rtime;
  }

  ld ans = 0;

  for ( int i=first; i<(int)seg.size(); i++ )
    ans += (ld)seg[i].second / (ld)seg[i].first;
  forn( i, zseg.size() )
    ans += zseg[i];

  printf( "%.10f\n", (double)ans );
}

int main()
{
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    printf( "Case #%d: ", q );
    solve();
  }
  return 0;
}