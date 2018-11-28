#include <cassert>
#include <cstdio>
#include <vector>
using namespace std;

int pomakni( vector< vector<int> > &V, int r1, int r2 ) {
//printf( "%d-> %d\n", r1, r2 );
    int ret = 0;

    while( r1 < r2 ) {
        swap( V[r1], V[r1+1] );
        ++ret;
        ++r1;
    }
    while( r1 > r2 ) {
        swap( V[r1], V[r1-1] );
        ++ret;
        --r1;
    }

    //printf( " :: %d\n", ret );
    return ret;

}

int get( vector< vector<int> > &V, int r, int n ) {
        int s = n-1;
        for( ; s >= 0; --s )
            if( V[r][s] ) break;
        return s;
}

int main( void ) {

 int test; scanf( "%d", &test );

 for( int cs = 1; cs <= test; ++cs ) {
      int n; scanf( "%d", &n );

      vector< vector<int> > matr = vector<vector<int> > ( n, vector<int> ( n ) );
      for( int i = 0; i < n; ++i ) {
        char buffer[41]; scanf( "%s", buffer );
        for( int j = 0; j < n; ++j )
            matr[i][j] = buffer[j]-'0';
      }

      int sol = 0;
      for( int r = 0; r < n; ++r ) {
         int s = get( matr, r, n );
         if( s > r ) {
            //printf( "r=%d s=%d\n", r, s );
            for( int i = r+1; i < n; ++i )
                if( get( matr, i, n ) <= r ) {
                    //printf( "->%d(%d)\n", i, get(matr,i,n) );
                    sol += pomakni( matr, i, r );
                    break;
                }
         }
       }
      printf( "Case #%d: %d\n", cs, sol );
 }

 return 0;
}
