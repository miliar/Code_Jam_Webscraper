#include <cstdio>
#include <cstring>
const int NULA = 0;
const int MAXN = 20;
const int MAXL = 1000;
const char *trazi = "welcome to code jam";

int n, m;
char buff[ MAXL ];
int num[ MAXN ];

int solve( char *S ) {
  if( *S == 0 ) return num[18];
  
  for( int i = 0; i < m; ++i )
    if( trazi[i] == *S )
      if( i ) num[i] += num[i-1];
      else ++num[0];

  return solve( S+1 );
}

int main( void ) {
  m = strlen( trazi );
  scanf( "%d%*c", &n );
  for( int i = 0; i < n; ++i ) {
    fgets( buff, sizeof( buff ), stdin );
    memset( num, 0, sizeof( num ) );
    printf( "Case #%d: %.4d\n", i+1, solve( buff ) );
  }

  return NULA;
}


