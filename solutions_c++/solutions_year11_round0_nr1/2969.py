#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define MAXN 100

int k, n;
char p[ MAXN + 1 ];
int d[ MAXN + 1 ];

inline int absl(int a  )
	 {
		  return ( a > 0 ? a : -a );
	 }

inline int max( int a, int b )
	 {
		  return ( (a) > (b) ? (a) : (b) );
	 }

void ini( void )
	 {
		  scanf( "%d ", &n );

		  int i, j; n += 2;
		  for( i=2; i<n; i++ )
					scanf( "%c %d ", &p[ i ], &d[ i ]);

		  return;
	 }

int work( void )
	 {
		  p[ 0 ] = 'B'; p[ 1 ] = 'O';
		  d[ 0 ] = 1; d[ 1 ] = 1;
		  int i, j;
		  int f[ MAXN + 1 ];
		  memset( f, 0, sizeof( f ) );
		  for( i=2; i<n; i++ )
			   {
					for( j=i-1; j>=0; j-- )
							  if ( p[ i ] == p[ j ] )
								   break;
					f[ i ] = max( f[ i - 1 ], f[ j ] + absl(
     						   d[ i ] - d[ j ] ) ) + 1;
			   }
		  return f[ n - 1 ];
	 }


int main( void )
	 {
  		  freopen( "1.in" , "r", stdin);
		  freopen( "1.out", "w", stdout );


		  scanf( "%d", &k );
		  int i;

  		  for( i=1; i<=k; i++ )
			   {
					ini(  );
					printf( "Case #%d: %d\n", i, work(  ));
			   }
		  return 0;
	 }
