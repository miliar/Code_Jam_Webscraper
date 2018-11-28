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

const int inf = 100000;

int n, m, F, TC, u[53][53][53][53], f[53][53][53][53];
char a[60][60];

int frow( int& i, int j )
{
//  printf( "-----> frow: i=%d\n", i );
  int bi = 1;
  while ( a[i+1][j] == '.' ) { i++; bi++; }
//  printf( "-----> frow: i=%d\n", i );
  return bi;
}

int rec( int i, int j, int lj, int rj )
{
//  fprintf( stderr, "rec i=%d, j=%d, lj=%d, rj=%d\n", i, j, lj, rj );
//  if ( i == n-1 ) { fprintf( stderr, "exit, last row\n" ); return 0; }
  if ( i == n-1 ) return 0;
  if ( u[i][j][lj][rj] == TC ) return f[i][j][lj][rj];
  u[i][j][lj][rj] = TC;

  int& res = f[i][j][lj][rj];
  res = inf;

  int li = j, ri = j;
  while ( a[i][li-1] == '.' && a[i+1][li-1] == '#' ) li--;
  while ( a[i][ri+1] == '.' && a[i+1][ri+1] == '#' ) ri++;
//  fprintf( stderr, "  li=%d, ri=%d\n", li, ri );

  if ( a[i+1][li-1] == '.' && a[i][li-1] == '.' )
  {
    int ti = i+1;
    if ( frow( ti, li-1 ) <= F )
    {
      int z = rec( ti, li-1, 0, 0 );
      if ( z < res ) res = z;
    }
  }

  if ( a[i+1][ri+1] == '.' && a[i][ri+1] == '.' )
  {
    int ti = i+1;
    if ( frow( ti, ri+1 ) <= F )
    {
      int z = rec( ti, ri+1, 0, 0 );
      if ( z < res ) res = z;
    }
  }

  for ( int lc=li; lc<=ri; lc++ )
  {
    for ( int rc=lc; rc<=ri; rc++ )
    {
      a[i+1][rc] = '.';

      if ( lc > li )
      {
        int ti = i+1;
        if ( frow( ti, lc ) <= F )
        {
          int z = rc-lc+1 + rec( ti, lc, lc, rc );
          if ( z < res ) res = z;
        }
      }

      if ( rc < ri )
      {
        int ti = i+1;
        if ( frow( ti, rc ) <= F )
        {
          int z = rc-lc+1 + rec( ti, rc, lc, rc );
          if ( z < res ) res = z;
        }
      }
    }

    for ( int rc=lc; rc<=ri; rc++ ) a[i+1][rc] = '#';
  }

  return res;
}

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    fprintf( stderr, "test %d...", tc );
    TC = tc;
    scanf( "%d %d %d\n", &n, &m, &F );
    forn( i,n )
    {
      gets( a[i]+1 );
      a[i][0] = a[i][m+1] = '#';
    }          

    forn( j,m+2 ) a[n][j] = '#';

    printf( "Case #%d: ", tc );
    int ans = rec( 0, 1, 0, 0 );
    if ( ans < inf ) printf( "Yes %d\n", ans );
    else printf( "No\n" );
    fprintf( stderr, "complete!\n" );
  }
}        