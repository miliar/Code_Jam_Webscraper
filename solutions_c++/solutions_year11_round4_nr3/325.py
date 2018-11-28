#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long llint;

#define MAXN 1005

int T, N;

int b[ MAXN ];
int g[ MAXN ];
int t[ MAXN ];

inline int brute( int N ) {
  if( N == 1 ) return 0;

  int Max = 1;
  int Min = 0;

  for( int i = 2; i <= N; ++i ) {
    t[i] = 0;
    int v = i; while( v % b[i] == 0 ) v /= b[i];
    Max += ( v == 1 );
  }

  for( int i = N; i >= 2; --i ) {
    if( !g[i] ) continue;
    if( t[b[i]] ) continue;

    llint mult = 1;

    for( int j = i; j >= 2; --j ) {
      if( !g[j] ) continue;
      if( t[b[j]] ) continue;
      if( mult*j > N ) continue;

      mult *= j;
      t[b[j]] = 1;
    }

    ++Min;
  }

  return Max - Min;
}

int main( void )
{
  for( int i = 2; i < MAXN; ++i ) {
    if( b[i] ) continue;
    for( int j = i; j < MAXN; j += i )
      b[j] = i;
  }

  for( int i = 2; i < MAXN; ++i ) {
    g[i] = ( ( b[i] == i ) || ( g[ i / b[i] ] ) );
  }

  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );
    printf( "Case #%d: %d\n", tc, brute( N ) );
  }

  return 0;
}
