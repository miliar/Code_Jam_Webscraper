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

const int maxn = 1000010;

int n, d, x[maxn], cnt[maxn];

bool check( ld tt ) {
  ld last = -1e100;
  forn( i, n )
    forn( j, cnt[i] ) {
      last = max( last + d, x[i] - tt );
      if ( fabs( last - x[i] ) > tt + 1e-9 ) return false;
    }
  return true;
}

void solve() {
  scanf( "%d %d", &n, &d );
  forn( i, n )
    scanf( "%d %d", &x[i], &cnt[i] );

  ld l = 0, r = 1e100, m;
//  int it = 0;
  while ( r-l > 1e-4 ) {
//    it++;
    m = ( l+r ) * 0.5;
    if ( check( m ) ) r = m;
    else l = m;
  }

  ll z = (ll)(r*10+0.2);
  r = z * 0.1;
  printf( "%.10f\n", (double)r );
}

int main()
{
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    fprintf( stderr, "test %d\n", q );
    printf( "Case #%d: ", q );
    solve();
/*    if ( q == 33 ) {
      fprintf( stderr, "%d %d\n", n, d );
      forn( i, n ) fprintf( stderr, "%d %d\n", x[i], cnt[i] );
    } */
  }
  return 0;
}