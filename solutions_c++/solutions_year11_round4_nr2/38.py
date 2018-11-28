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

int n, m, d, a[510][510], s[510][510];
char st[510];

int getsum( int i1, int j1, int i2, int j2 ) {
  return s[i2][j2] - s[i1][j2] - s[i2][j1] + s[i1][j1];
}

void solve() {
  scanf( "%d %d %d", &n, &m, &d );
  forn( i, n ) {
    scanf( "%s", st );
    forn( j, n )
      a[i+1][j+1] = st[j] - '0';
  }

  for ( int i=1; i<=n; i++ )
    for ( int j=1; j<=m; j++ )
      s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j];

  int ans = 0;
  forn( i, n )
    forn( j, m ) {
      int klim = min( n-i, m-j );
      for ( int k=3; k<=klim; k++ )
        if ( k&1 ) {
          int half = k >> 1;
          int l = getsum( i, j, i+k, j+half ) - a[i+1][j+1] - a[i+k][j+1];
          int r = getsum( i, j+half+1, i+k, j+k ) - a[i+1][j+k] - a[i+k][j+k];
          int u = getsum( i, j, i+half, j+k ) - a[i+1][j+1] - a[i+1][j+k];
          int d = getsum( i+half+1, j, i+k, j+k ) - a[i+k][j+1] - a[i+k][j+k];

          if ( l == r && u == d ) ans = max( ans, k );
        } else {
          int half = k >> 1;
          int l = getsum( i, j, i+k, j+half ) - a[i+1][j+1] - a[i+k][j+1];
          int r = getsum( i, j+half, i+k, j+k ) - a[i+1][j+k] - a[i+k][j+k];
          int u = getsum( i, j, i+half, j+k ) - a[i+1][j+1] - a[i+1][j+k];
          int d = getsum( i+half, j, i+k, j+k ) - a[i+k][j+1] - a[i+k][j+k];

          if ( l == r && u == d ) ans = max( ans, k );
        } 
    }

  if ( ans == 0 ) printf( "IMPOSSIBLE\n" );
  else printf( "%d\n", ans );
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