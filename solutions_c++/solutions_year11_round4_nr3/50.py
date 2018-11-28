#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long llint;

const int MAXN = 1000005;

int a[MAXN];

int main( void ) {
  for( int i = 2; i*i < MAXN; ++i )
    if( !a[i] )
      for( int j = i*i; j < MAXN; j += i )
	a[j] = 1;

  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {     
    llint n;
    scanf( "%lld", &n );
    
    int m = sqrt( n ) + 1;
    
    llint ans = 1;
    for( int i = 2; i <= m; ++i )
      if( !a[i] ) {
	llint c = 0, x = i;
	while( x <= n ) x *= i, c++;
	ans += c-1;
      }
    
    if( n == 1 ) ans = 0;
    printf( "Case #%d: ", c );
    printf( "%lld\n", ans );
  }
  return 0;
}

