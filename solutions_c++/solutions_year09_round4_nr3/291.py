#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

vector< vector<int> > V;
int n, k;
int bio[100], anc[100];

int cmp( vector<int> A, vector<int> B ) {
    for( int i = 0; i < k; ++i )
        if( A[i] <= B[i] ) return 0;
    return 1;
}

int dfs( int s ) {
    if( bio[s] ) return 0;
    bio[s] = 1;

    for( int i = 0; i < n; ++i ) {
        if( cmp( V[s], V[i] ) ) {
            //printf( "%d -> %d\n", s, i );
            if( anc[i] == -1 || dfs( anc[i] ) ) {
                anc[i] = s;
                return 1;
            }
        }
    }
    return 0;
}

int main( void ) {

 int test; scanf( "%d", &test );

 for( int cs = 1; cs <= test; ++cs ) {
      scanf( "%d%d", &n, &k );

      V.clear();
      for( int i = 0; i < n; ++i ) {
            vector<int> val( k );
            for( int j = 0; j < k; ++j ) scanf( "%d", &val[j] );
            // for( int j = 0; j < k; ++j ) printf( "%d ", val[j] ); puts( "" );
            V.push_back( val );
      }

      int match = 0;
      memset( anc, -1, sizeof anc );

      for( int i = 0; i < n; ++i ) {
        memset( bio, 0, sizeof bio );
        match += dfs( i );
      }

//printf( "%d\n", match );
//    for( int i = 0; i < n; ++i ) printf( "%d %d\n", anc[i], i );

      printf( "Case #%d: %d\n", cs, n - match );
 }


 return 0;
}
