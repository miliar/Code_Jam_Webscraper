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

const int maxn = 410;

vector<int> g[maxn], level[maxn];
int d[maxn], q[maxn], qb, qf, n, m, a, b;
int u[maxn][maxn], it;
int uc[maxn], itc;
pii qp[maxn*maxn];
int f[maxn][maxn];

int countcommon( int i, int j, int k ) {
  itc++;
  int res = 0;
  forn( q, g[i].size() )
    if ( g[i][q] != j && g[i][q] != k )
      if ( uc[ g[i][q] ] != itc ) {
        res++;
        uc[ g[i][q] ] = itc;
      }
  forn( q, g[j].size() )
    if ( g[j][q] != i && g[j][q] != k )
      if ( uc[ g[j][q] ] != itc ) {
        res++;
        uc[ g[j][q] ] = itc;
      }
  if ( k != -1 )
  forn( q, g[k].size() )
    if ( g[k][q] != j && g[k][q] != i )
      if ( uc[ g[k][q] ] != itc ) {
        res++;
        uc[ g[k][q] ] = itc;
      }
  return res;
}

void solve() {
  scanf( "%d %d", &n, &m );
  forn( i, n ) g[i].clear(), d[i] = -1; // level[i].clear();

  bool flag = false;

  forn( i, m ) {
    scanf( "%d,%d", &a, &b );
    g[a].pb( b );
    g[b].pb( a );
    if ( a == 0 && b == 1 ) flag = true;
  }

  if ( flag ) {
    printf( "0 %d\n", g[0].size() );
    return;
  }

  qb = qf = 0;

  q[qf++] = 0;
  d[0] = 0;

  while ( qb < qf ) {
    int x = q[qb++];

    forn( i, g[x].size() )
      if ( d[ g[x][i] ] == -1 ) {
        q[qf++] = g[x][i];
        d[ g[x][i] ] = d[x] + 1;
//        level[ d[x]+1 ].pb( g[x][i] );
      }      
  }

  qb = qf = 0;

  it++;

  forn( i, g[0].size() )
    if ( d[ g[0][i] ] == 1 ) {
      qp[ qf++ ] = pii( 0, g[0][i] );
      f[0][ g[0][i] ] = countcommon( 0, g[0][i], -1 ); 
      u[0][ g[0][i] ] = it;
    }

  while ( qb < qf ) {
    pii cur = qp[ qb++ ];

    if ( d[cur.second] == d[1]-1 ) continue;

    int z = countcommon( cur.first, cur.second, -1 );

    forn( i, g[ cur.second ].size() ) {
      int y = g[ cur.second ][i];
      if ( d[y] != d[ cur.second ] + 1 ) continue;
      int c = countcommon( cur.first, cur.second, y );

      if ( u[cur.second][y] == it ) f[cur.second][y] = max( f[cur.second][y], f[cur.first][cur.second] + c - z );
      else {
        f[cur.second][y] = f[cur.first][cur.second] + c - z;
        u[cur.second][y] = it;
        qp[ qf++ ] = pii( cur.second, y );
      }
    }
  }

  int ans = 0;

  forn( i, n )
    forn( j, g[i].size() )
      if ( d[ g[i][j] ] == d[1]-1 && u[i][ g[i][j] ] == it ) {
        bool ok = false;
        forn( q, g[1].size() )
          if ( g[1][q] == g[i][j] ) {
            ok = true;
            break;
          }

        if ( ok ) ans = max( ans, f[i][ g[i][j] ] );
      }
/*
  forn( i, n )
    forn( j, g[i].size() )
      if ( u[i][ g[i][j] ] == it ) {
        printf( "f[%d][%d] = %d\n", i, g[i][j], f[i][ g[i][j] ] );
      }
*/
  printf( "%d %d\n", d[1]-1, ans );
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