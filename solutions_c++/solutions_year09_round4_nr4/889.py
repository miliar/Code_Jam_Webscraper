#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int NULA = 0;

const int MAXN = 70;

struct krug {
  double x, y, r;
  
  void get( void ) {
    scanf( "%lf%lf%lf", &x, &y, &r );
  }
};

bool operator < ( const krug &A, const krug &B ) {
  if( A.x != B.x ) return A.x < B.x;
  if( A.y != B.y ) return A.y < B.y;
  if( A.r != B.r ) return A.r < B.r;

  return 0;
}

int n;
krug K[MAXN];
double sol;
double tmp;

inline double dist( double a, double b, double c, double d ) {
  return sqrt( (a-c)*(a-c) + (b-d)*(b-d) );
}

inline double dist( krug a, krug b ) {
  return dist( a.x, a.y, b.x, b.y );
}

int main( void ) {
  int c;
  scanf( "%d", &c );
 
  for( int C = 0; C < c; ++C ) {
    sol = 1e1000;
    scanf( "%d", &n ); 
    for( int i = 0; i < n; ++i )
      K[i].get();

    tmp = -1e100;

    if( n == 3 ) {
      sort( K, K+n );

      // for( int i = 0; i < n; ++i ) 
      //   for( int j = 0; j < n; ++j ) 
      //     printf( "dist[ %d ][ %d ]: %.3lf\n", i, j, dist(X[i],Y[i], X[j],Y[j]) );
      
      for( int i = 0; i < 30; ++i ) {
        tmp = max( K[2].r, ( K[0].r + K[1].r + dist( K[0], K[1] ) ) / 2. );


        // printf( "%g %g %g: %8.3lf  ", X[0], X[1], X[2], tmp );
        // for( int i = 0; i < n; ++i ) 
        //   printf( "(%g,%g) ", X[i], Y[i] );
        // printf( "\n" ); 

        sol = min( tmp, sol );
        
        next_permutation( K, K+n );
      }
    }
    
    else if( n == 2 ) 
      sol = max( K[0].r, K[1].r );
    else 
      sol = K[0].r;
    
    
    printf( "Case #%d: %.8lf\n", C+1, sol );
  }



  return NULA;
}

