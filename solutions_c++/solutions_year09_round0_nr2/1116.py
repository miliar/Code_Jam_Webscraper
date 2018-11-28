#include <cstdio>
#include <memory.h>
using namespace std;

const int di[] = { -1, 0, 0, 1 };
const int dj[] = { 0, -1, 1, 0 };

int n, m, a[110][110], kp, p[110][110];

int dfs( int i, int j )
{
  if ( p[i][j] > -1 ) return p[i][j];
  int lo = 100000, ti=-1, tj=-1;
  for ( int q=0; q<4; q++ )
  {
    int ci = i+di[q];
    int cj = j+dj[q];
    if ( ci >= 0 && ci < n && cj >=0 && cj < m && a[ci][cj] < lo )
    {
      ti = ci;
      tj = cj;
      lo = a[ci][cj];
    } 
  }

  if ( lo >= a[i][j] ) p[i][j] = kp++;
  else p[i][j] = dfs( ti, tj );

  return p[i][j];
}

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    scanf( "%d %d", &n, &m );
    for ( int i=0; i<n; i++ )
      for ( int j=0; j<m; j++ )
        scanf( "%d", &a[i][j] );

    memset( p, 0xff, sizeof(p) );

    kp = 0;
    for ( int i=0; i<n; i++ )
      for ( int j=0; j<m; j++ )
        if ( p[i][j] == -1 ) dfs( i, j );

    printf( "Case #%d:\n", tc );
    for ( int i=0; i<n; i++ )
    {
      for ( int j=0; j<m; j++ )
      {
        if ( j ) printf( " " );
        putchar( 'a'+p[i][j] );
      } 
      printf( "\n" );
    }
  }
}