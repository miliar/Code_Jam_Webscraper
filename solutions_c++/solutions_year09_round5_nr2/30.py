#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MOD = 10009;

char b[ 100002 ];
char s[ 100002 ];
int C[30][30];
int f[30][30];
int c[30], h[30];
int r, n, q, l;

int eval() {
  int z, p;
  z = p = 0;
  while( p < l ) {
    int r = 1;
    while( !isalpha( s[p] ) && p < l ) p++;
    if( p >= l ) break;
    while( isalpha( s[p] ) && p < l ) r = ( r*h[s[p]-'a'] )%MOD, p++;
    z += r;
  }
  return z;
}

void rec( int x, int w ) {
  if( x > n ) return;
  if( w == 0 && x == n ) {
    int g = 0, p = 1, e = q;
    memset( h, 0, sizeof( h ) );
    for( int i = 0; i < n; ++i ) {
      p = ( p*C[e][c[i]] )%MOD, e -= c[i];
      for( int j = 0; j < 26; ++j )
	h[j] += c[i]*f[i][j];
    }
    g = eval();
    r = ( r + p*g )%MOD;
    return;
  }
  for( int i = 0; i <= w; ++i ) {
    c[x] = i;
    rec( x+1, w-i );
  }
}
    
int main( void ) {
  C[0][0] = 1;
  for( int i = 1; i < 30; ++i ) {
    C[i][0] = 1;
    for( int j = 1; j <= i; ++j ) {
      C[i][j] = C[i-1][j-1] + C[i-1][j];
      if( C[i][j] >= MOD ) C[i][j] -= MOD;
    }
  }

  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    scanf( "%s", s );
    l = strlen( s );
    int k;
    scanf( "%d %d", &k, &n );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", b );
      int p = strlen( b );
      memset( f[i], 0, sizeof( f[i] ) );
      for( int j = 0; j < p; ++j )
	f[i][ b[j]-'a' ]++;
    }

    printf( "Case #%d:", d );
    for( int w = 1; w <= k; ++w ) {
      q = w, r = 0;
      rec( 0, w );
      printf( " %d", r );
    }
    putchar( '\n' );
  }
  return 0;
}
