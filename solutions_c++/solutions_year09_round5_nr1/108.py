#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
#include <cmath>
#include <set>
#include <utility>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
#define mp make_pair
#define Sort( n ) sort( n.begin(), n.end() )
typedef vector< pair<int,int> > VP;

const int dx[] = { -1, 0, 1, 0 };
const int dy[] = { 0, -1, 0, 1 };

VP stp, finp, qv[10000010], cur, nn;
int qd[ 10000010 ], qp[ 10000010 ];
int n, m, k, beg, fin;
vector<int> g[10];
bool u[10];
char s[20];
set< VP > ss;
int a[20][20];

int aa( int x )
{
  return x < 0 ? -x : x;
}

int dfs( int x )
{
  int res = 1;
  u[x] = 1;
  forn( i,g[x].size() )
    if ( !u[ g[x][i] ] )
      res += dfs( g[x][i] );
  return res;
}

int danger( VP a )
{
  forn( i, k ) g[i].clear();
  forn( i, k )
    forn( j, i )
      if ( aa( a[i].first-a[j].first ) + aa( a[i].second - a[j].second ) == 1 )
      {
        g[i].push_back( j );
        g[j].push_back( i );
      }
  forn( i,k ) u[i] = 0;
  if ( dfs(0) == k ) return 0; else return 1;
}

void PP( VP a )
{
  forn( i,k ) printf( "(%d,%d) ", a[i].first, a[i].second );
  printf( "\n" );
}

int main()
{
  int t;
  scanf( "%d", &t );
  for ( int tc=1; tc<=t; tc++ )
  {
    fprintf( stderr, "test %d...\n", tc );
    scanf( "%d %d\n", &n, &m );
    printf( "Case #%d: ", tc );
    stp.clear();
    finp.clear();
    memset( a, 0, sizeof(a) );
    forn( i,n )
    {
      gets( s );
      forn( j,m ) if ( s[j] == '#' ) a[i+1][j+1] = 1;
      else
      {
        a[i+1][j+1] = 0;
        if ( s[j] == 'o' || s[j] == 'w' ) stp.pb( mp( i+1,j+1 ) );
        if ( s[j] == 'x' || s[j] == 'w' ) finp.pb( mp( i+1,j+1 ) );
      }
    }
    forn( i,n+2 )
      a[i][0] = a[i][m+1] = 1;
    forn( i,m+2 )
      a[0][i] = a[n+1][i] = 1;
    Sort( stp );
    Sort( finp );
    k = stp.size();

    if ( stp == finp )
    {
      printf( "0\n" );
      continue;
    }

    ss.clear();
    beg = fin = 0;
    qv[ fin ] = stp;
    qp[ fin ] = 0;
    qd[ fin ] = 0;
    fin++;
    ss.insert( stp );

    int ok = 0;
    while ( beg < fin )
    {
      cur = qv[ beg ];
      int cp  = qp[ beg ];
      int cd  = qd[ beg ];
      beg++;
//      printf( "\n  Now - " ); PP( cur );

      forn( i,k ) a[ cur[i].first ][ cur[i].second ] = 1;

      forn( i,k )
      {
        int nx = cur[i].first;
        int ny = cur[i].second;
        forn( q,4 )
        {
          cur[i].first = nx+dx[q];
          cur[i].second = ny+dy[q];
          if ( a[ cur[i].first ][ cur[i].second ] == 1 || a[ nx-dx[q] ][ ny-dy[q] ] == 1 ) continue;
          int fd = danger( cur );
//          printf( "Looka " ); PP( cur );
//          printf( "danger == %d\n", fd );
          if ( cd && fd ) continue;
//          printf( "Try to " ); PP( cur );
          nn = cur;
          Sort( nn );
          if ( ss.find( nn ) == ss.end() )
          {
            ss.insert( nn );
            qv[ fin ] = nn;
            qp[ fin ] = cp+1;
            qd[ fin ] = fd;
            fin++;
//            printf( "-> " ); PP( nn );

            if ( nn == finp )
            {
              printf( "%d\n", cp+1 );
              ok = 1;
              break;
            }
          }
        }
        cur[i].first = nx, cur[i].second = ny;
        if ( ok ) break;
      }

      forn( i,k ) a[ cur[i].first ][ cur[i].second ] = 0;

      if ( ok ) break;
    }

    if ( ok == 0 ) printf( "-1\n" );
  }
}