#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int B = 8;

char b[] = "QWERASDF";
char op[300][300];
char fs[300][300];
char s[1000];

int cnt[300];
int a[1000], m;

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    memset( op, 0, sizeof( op ) );
    memset( fs, -1, sizeof( fs ) );
    memset( cnt, 0, sizeof( cnt ) );
    m = 0;

    int n;
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i ) {
      scanf( " %s", s );
      fs[s[0]][s[1]] = fs[s[1]][s[0]] = s[2];
    }
    
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i ) {
      scanf( " %s", s );
      op[s[0]][s[1]] = op[s[1]][s[0]] = 1;
    }

    scanf( "%d %s", &n, s );
    for( int i = 0; i < n; ++i )
      if( m > 0 && fs[s[i]][a[m-1]] != -1 ) cnt[ a[m-1] ]--, a[m-1] = fs[ s[i] ][ a[m-1] ], cnt[a[m-1]]++; else {
	int ok = 1;
	for( int j = 0; j < 8; ++j )
	  if( op[ b[j] ][ s[i] ] && cnt[ b[j] ] > 0 ) { ok = 0; break; }
	if( !ok ) { m = 0; memset( cnt, 0, sizeof( cnt ) ); }
	if( ok ) a[m++] = s[i], cnt[ a[m-1] ]++;
      }

    printf( "Case #%d: [", c );
    for( int i = 0; i < m; ++i ) {
      if( i > 0 ) printf( ", " );
      putchar( a[i] );
    }
    printf( "]\n" );
  }
  return 0;
}
