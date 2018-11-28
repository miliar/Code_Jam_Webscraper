#include <cstring>
#include <cstdio>

#define maxn 100

const int dx[4] = { -1, 0, 1, 0 };
const int dy[4] = { 0, 1, 0, -1 };
const int ord[] = { 0, 3, 1, 2 };

int r, c, a[maxn][maxn];
int graph[maxn][maxn][4];
char sol[maxn][maxn];

int gdje( int x, int y ) {
   int m = -1;
   for( int i = 0; i < 4; ++i ) {
      int nr = x+dx[ ord[i] ], nc = y+dy[ ord[i] ];
      if( nr < 0 || nr == r ) continue;
      if( nc < 0 || nc == c ) continue;
      if( a[nr][nc] >= a[x][y] ) continue;

      if( m == -1 || a[nr][nc] < a[x+dx[m]][y+dy[m]]) m = ord[i];
   }
   return m;
}

void load() {
   scanf( "%d%d", &r, &c );
   for( int i = 0; i < r; ++i )
      for( int j = 0; j < c; ++j ) scanf( "%d", &a[i][j] );
}

void dfs( int i, int j, char t ) {
   sol[i][j] = t;
   for( int k = 0; k < 4; ++k )
      if( graph[i][j][k] && !sol[i+dx[k]][j+dy[k]]) dfs( i+dx[k], j+dy[k], t );
}

void solve() {
   memset( graph, 0, sizeof graph );

   for( int i = 0; i < r; ++i )
      for( int j = 0; j < c; ++j ) {
            int g = gdje( i, j );
            if( g == -1 ) continue;
            graph[i][j][g] = graph[ i+dx[g] ][ j+dy[g] ][ g^2 ] = 1;
      }

   memset( sol, 0, sizeof sol );

   char t = 'a';
   for( int i = 0; i < r; ++i )
      for( int j = 0; j < c; ++j )
         if( sol[i][j] == 0 ) dfs( i, j, t++ );

   for( int i = 0; i < r; ++i ) {
      for( int j = 0; j < c; ++j ) {
         if( j ) printf( " " );
         printf( "%c", sol[i][j] );
      }
      printf( "\n" );
   }     
}

int main(void) {
   int T;
   scanf( "%d", &T );
   for( int i = 0; i < T; ++i ) {
      printf( "Case #%d:\n", i+1 );
      load();
      solve();
   }
   return 0;
}
