#include <cstdio>
#include <cstring>
using namespace std;
const int MAXL = 500;
const int LEN = 19;
const int MOD = 10000;

char A[MAXL+1];
char B[LEN+1];

int dp[MAXL+1][LEN+1];

int rek( int a, int b )
{
  if ( b < 0 ) return 1;
  if ( a < 0 ) return 0;

  int &ref = dp[a][b];
  if ( ref != -1 ) return ref;

  ref = rek( a - 1, b );
  if ( A[a] == B[b] ) 
    ref += rek( a - 1, b - 1 );

  if ( ref >= MOD ) ref -= MOD;

  return ref;
}

int main()
{
  memcpy( B, "welcome to code jam", LEN );

  int t; scanf( "%d ", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    gets( A );

    memset( dp, -1, sizeof( dp ) );

    printf( "Case #%d: %04d\n", t_case + 1, rek( strlen( A ) - 1, LEN - 1 ) );
  }
  return 0;
}
