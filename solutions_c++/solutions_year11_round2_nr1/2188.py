#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 100

int t;
char f[MAXN + 1 ][MAXN + 1];
double wp[ MAXN + 1 ], owp[ MAXN + 1 ], oowp[ MAXN + 1 ];
int n;


void ini( void )
	 {
		  scanf( "%d\n", &n );
		  int i, j;
		  for( i=1; i<=n; i++ )
			   {
					for( j=1; j<=n; j++ )
						 scanf( "%c", &f[ i ][ j ] );
					scanf( "\n" );
			   }
		  return;
	 }

void work( void )
	 {
		  int i, j, k;
		  double sum, total = 0, sumt;

		  for( i=1; i<=n; i++ )
			   {
					sum = 0;total = 0;
					for( j=1; j<=n; j++ )
						 {
	  						 if ( f[ i][ j] == '1' )
							  {
								   sum++;
							  }
							 if ( f[ i ][ j] != '.' )
								  total++;
						 }
						 
					wp[ i ] = sum / total;
			   }
		  for( i=1; i<=n; i++ )
			   {
					sumt = 0;
					for( j=1; j<=n; j++ )
						 {
		  						 if ( f[ i ][ j ] == '.' )
									  continue;
								 sum = 0;total = 0;
								 for( k=1; k<=n; k++ )
									  {
										   if ( k == i )
												continue;
										   if ( f[ j ][ k ] == '1' )
												sum++;
										   if ( f [ j][ k ] != '.' )
													 total++;
									  }
								 sumt += ( sum /  total );
						 }
					total = 0;
					for( j=1; j<=n; j++ )
						 if ( f[ i ][ j ] != '.' )
							  total++;
					owp[ i ] = ( sumt / total);
			   }
		  for( i=1; i<=n; i++ )
			   {
					sum = 0;total = 0;
					for( j=1; j<=n; j++ )
						 {
							 if ( f[ i ][ j ] != '.' )
								  {
	     						     sum += owp[ j ];
	 								  total++;
								  }
						 }
					oowp[ i ] = sum / total;
			   }
		  for( i=1; i<=n; i++ )
			   {
					printf( "%.12lf\n", 0.25 * wp[ i ] + 0.50 * owp[ i ] + 0.25 * oowp[ i ] );
			   }
			   
		  return;
	 }
  


int main( void )
	 {
		  freopen( "2a1.in" ,"r", stdin);
		  freopen( "2a1.out", "w", stdout );

		  int i, j;
		  scanf( "%d", &t );
		  for( i=1; i<=t; i++ )
			   {
					printf( "Case #%d:\n", i );
					ini(  );
					work(  );
			   }
		  return 0;
	 }
