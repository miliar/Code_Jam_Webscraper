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

const int maxn = 10;

int n, m, a[maxn], b[maxn];
int color[maxn], best[maxn], ans, who[maxn];
vector<int> room[maxn];
int kr;
int p[maxn], next[maxn];

bool ok( int k ) {
  int all = ( 1<<k ) - 1;
  forn( i, kr ) {
    int cmask = 0;
    forn( j, room[i].size() )
      cmask |= 1 << color[ room[i][j] ];

    if ( cmask != all ) return false;
  }

  return true;
}

void setcolors( int mask, int c ) {
  forn( i, n )
    if ( mask & ( 1<<i ) )
      color[i] = c;
}

void check( int k ) {
  if ( k <= ans ) return;
  forn( i, k ) setcolors( who[i], i );
  if ( ok( k ) ) {
    ans = k;
    forn( i, n ) best[i] = color[i];
  }
}

void gen( int mask, int i ) {
//  printf( "gen %d %d\n", mask, i );
  if ( mask == 0 ) check( i );
  else {
    int last = mask ^ ( mask & ( mask-1 ) );
    mask &= mask-1;
    for ( int cur = mask; cur >= 0; cur = ( cur-1 ) & mask ) {
      who[i] = cur ^ last;
      gen( mask ^ cur, i+1 );
      if ( cur == 0 ) break;
    }      
  }
}

bool cmp( int i, int j ) {
  return b[i]-a[i] < b[j]-a[j];
}

void solve() {
  scanf( "%d %d", &n, &m );
  forn( i, m ) scanf( "%d", &a[i] );
  forn( i, m ) scanf( "%d", &b[i] );
  a[m] = 1;                   
  b[m] = n;
  m++;

  forn( i, m ) p[i] = i;
  sort( p, p+m, cmp );
 
  forn( i, n+1 ) next[i] = i+1;

  kr = 0;
  forn( q, m ) {
    int i = p[q];
    int c = 1;
    while ( c != a[i] ) c = next[c];
    room[kr].clear();
    while ( c != b[i] ) {
      room[kr].pb( c-1 );
      c = next[c];
    }
    room[kr++].pb( b[i]-1 );
    next[ a[i] ] = b[i];
  }

  ans = -1;

  gen( (1<<n)-1, 0 );

  printf( "%d\n", ans );
  forn( i, n ) {
    if ( i ) printf( " " );
    printf( "%d", best[i]+1 );
  }
  printf( "\n" );
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