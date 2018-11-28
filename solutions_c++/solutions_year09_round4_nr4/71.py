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

int n, x[50], y[50], r[50];
double g[50][50];
int c1, c2, id1[50], id2[50];
double lim;

int dist( int i, int j )
{
  return ( x[i]-x[j] )*( x[i]-x[j] ) + ( y[i]-y[j] )*( y[i]-y[j] );
}

bool rec( int i )
{
  if ( i == n ) return 1;

  id1[ c1++ ] = i;
  int fl = 1;
  for ( int j=0; j<c1 && fl; j++ )
    if ( g[i][ id1[j] ] > lim ) fl = 0;

  if ( fl ) if ( rec( i+1 ) ) return 1;
  c1--;

  id2[ c2++ ] = i;
  fl = 1;
  for ( int j=0; j<c2 && fl; j++ )
    if ( g[i][ id2[j] ] > lim ) fl = 0;

  if ( fl ) if ( rec( i+1 ) ) return 1;
  c2--;

  return 0;
}


bool check( double m )
{
//  printf( "Checking %.3f...\n", m );
  lim = m;
  c1 = c2 = 0;
  return ( rec( 0 ) );
}

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    scanf( "%d", &n );
    forn( i,n )
      scanf( "%d %d %d", &x[i], &y[i], &r[i] );

    forn( i,n )
      for ( int j=i; j<n; j++ )
        g[i][j] = g[j][i] = sqrt( dist( i, j ) ) + r[i] + r[j];


    double l = 0.0, r = 1000000000.0;
    while ( r-l > 1e-7 )
    {
      double m = ( l+r ) / 2.0;
      if ( check( m ) ) r = m;
      else l = m;
    }

    printf( "Case #%d: %.7f\n", tc, r/2.0 );
  }
}        