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
#define foreach( it, a ) for ( __typeof((a).begin()) it = (a).begin(); it != (a).end(); it++ )
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

multiset<int> ss, snew;
int n, a[1010];

void solve() {
  scanf( "%d", &n );
  forn( i, n ) scanf( "%d", &a[i] );
  sort( a, a+n );

  int ans = 1010;
  ss.clear();

  int last = -2;
  for ( int i=0; i<n; ) {
    int j = i;
    for ( j=i; j < n && a[j] == a[i]; j++ );

    if ( a[i] > last+1 ) {
      if ( !ss.empty() ) ans = min( ans, *ss.begin() );
      ss.clear();
    }

    int cnt = j-i;
    snew.clear();
    int q = 0;
    foreach( it, ss ) {
      q++;
      if ( q <= cnt ) snew.insert( (*it)+1 );
      else {
        ans = min( ans, *it );
        break;
      }
    }

    ss = snew;

    cnt = max( 0, cnt - (int)ss.size() );
    forn( q, cnt ) ss.insert( 1 );

    last = a[i];
    i = j;
/*
    printf( "%d:", ss.size() );
    foreach( it, ss ) printf( " %d", *it );
    printf( "\n" );
*/
  }

  if ( !ss.empty() ) ans = min( ans, *ss.begin() );

  if ( ans == 1010 ) ans = 0;

  printf( "%d\n", ans );
}


int main()
{
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    fprintf( stderr, "test %d\n", q );
    printf( "Case #%d: ", q );
    solve();
  }
  return 0;
}