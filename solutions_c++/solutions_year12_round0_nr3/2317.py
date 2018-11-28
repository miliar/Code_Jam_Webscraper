#include <cstdio>
#include <cstring>

#include <set>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T, A, B, C;
string s, z;

char buff[ 105 ];

vector< int > pairs[ 2000005 ];

void brute_pairs() {
  for( int i = 1; i <= 2000000; ++i ) {
    sprintf( buff, "%d", i );
    s = string( buff );

    set< int > r;

    for( int j = 1; j < s.size(); ++j ) {
      z = s.substr( j, s.size() - j ) + s.substr( 0, j );

      if( z[0] != '0' ) {
	sscanf( z.c_str(), "%d", &C );
	if( C != i ) r.insert( C );
      }
    }

    while( !r.empty() ) {
      pairs[i].push_back( *r.begin() );
      r.erase( r.begin() );
    }
  }
}

int main( void )
{
  brute_pairs();

  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%d", &A, &B );

    int Sol = 0;

    for( int i = A; i <= B; ++i ) {
      sprintf( buff, "%d", i );
      s = string( buff );

      for( int j = 0; j < pairs[i].size(); ++j ) 
	if( pairs[i][j] >= A && pairs[i][j] <= B ) ++Sol;
    }

    printf( "Case #%d: %d\n", tc, Sol / 2 );
  }

  return 0;
}
