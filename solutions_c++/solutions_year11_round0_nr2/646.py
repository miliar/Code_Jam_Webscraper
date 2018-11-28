#include <cstdio>
#include <cstring>

int T, C, D, N;
char c[ 105 ][ 5 ];
char d[ 105 ][ 5 ];
char s[ 105 ];
char st[ 105 ];
int top;

int cnt[ 26 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &C );

    for( int i = 0; i < C; ++i ) {
      scanf( "%s", c[i] );
    }

    scanf( "%d", &D );

    for( int i = 0; i < D; ++i ) {
      scanf( "%s", d[i] );
    }

    scanf( "%d", &N );
    scanf( "%s", s );

    int top = 0;

    for( int i = 0; i < 26; ++i ) cnt[i] = 0;

    for( int i = 0; i < N; ++i ) {
      st[top++] = s[i];
      ++cnt[s[i]-'A'];
      bool good = ( top > 1 );

      while( good ) {
	good = 0;

	for( int j = 0; j < C; ++j ) {
	  if( st[top-2] == c[j][0] && st[top-1] == c[j][1] ||
	      st[top-2] == c[j][1] && st[top-1] == c[j][0] ) {
	    good = 1; 

	    --cnt[st[top-1]-'A']; --top;
	    --cnt[st[top-1]-'A']; --top;

	    st[top++] = c[j][2];
	    ++cnt[c[j][2]-'A'];

	    break;
	  }
	}
      }

      for( int j = 0; j < D; ++j ) {
	if( d[j][0] == st[top-1] && cnt[d[j][1]-'A'] ||
	    d[j][1] == st[top-1] && cnt[d[j][0]-'A'] ) {
	  top = 0;

	  for( int k = 0; k < 26; ++k ) cnt[k] = 0;
	}
      }

    }

    printf( "Case #%d: ", tc );

    putchar( '[' );
    for( int i = 0; i < top; ++i ) {
      putchar( st[i] );
      if( i != top-1 ) printf( ", " );
    }
    putchar( ']' );
    putchar( '\n' );
  }


  return 0;
}
