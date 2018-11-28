#include <cstdio>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <memory.h>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int,int> pii;


int f[1<<17], okm[1<<17], n, k, a[20][50], g[20][20];

bool check( int m )
{
  forn( i,n ) if ( m & (1<<i) )
    for ( int j=i+1; j<n; j++ ) if ( m & ( 1<<j ) )
      if ( g[i][j] ) return 0;

  return 1;
}

int rec( int m )
{
  if ( m == 0 ) return 0;
  if ( f[m] < n+1 ) return f[m];

  for ( int nm=m; nm>0; nm = ( nm-1 )&m )
    if ( okm[nm] )
    {
      int z = rec( m-nm );
      if ( z+1 < f[m] ) f[m] = z+1;
    }

  return f[m];
}

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    scanf( "%d %d", &n, &k );
    forn( i,n )
      forn( j,k ) scanf( "%d", &a[i][j] );

    forn( i,n )
      for ( int j=i+1; j<n; j++ )
      {
        g[i][j] = g[j][i] = ( a[i][0] == a[j][0] );
        for ( int q=1; q<k && !g[i][j]; q++ )
          g[i][j] = g[j][i] = ( a[i][q] == a[j][q] || a[i][q-1] < a[j][q-1] && a[i][q] > a[j][q] || a[i][q-1] > a[j][q-1] && a[i][q] < a[j][q] );
      }

    forn( i, 1<<n )
    {
      okm[i] = check( i );
      f[i] = n+1;
    }

    printf( "Case #%d: %d\n", tc, rec( (1<<n)-1 ) );
  }
}        