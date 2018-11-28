#include <cstdio>
#include <cstring>

using namespace std;

const int MaxL = 505;
const int MOD = 10000;
const int m = 19;

int dp[ MaxL ][ m+1 ];
char s[] = "welcome to code jam";
char a[ MaxL ];

int main( void ) {
  int t;
  scanf( "%d", &t );
  gets( a );
  for( int c = 0; c < t; ++c ) {
    memset( a, 0, sizeof( a ) );
    gets( a );
    int l = 0;
    while( a[l] > 0 && a[l] != '\n' && a[l] != '\0' ) l++;

    memset( dp, 0, sizeof( dp ) );
    dp[0][0] = 1;
    for( int i = 0; i < l; ++i )
      for( int j = 0; j <= m; ++j ) {
	if( j < m && a[i] == s[j] ) {
	  dp[ i+1 ][ j+1 ] += dp[i][j];
	  if( dp[ i+1 ][ j+1 ] >= MOD ) dp[ i+1 ][ j+1 ] -= MOD;
	}
	dp[ i+1 ][j] += dp[i][j];
	if( dp[ i+1 ][j] >= MOD ) dp[ i+1 ][j] -= MOD;
      }

    printf( "Case #%d: %04d\n", c+1, dp[l][m] );
  }
  return 0;
}
