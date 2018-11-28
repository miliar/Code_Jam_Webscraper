#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 50

char f[ MAXN + 1 ][ MAXN + 1 ];
int r, c;

void ini( void )
	 {
		  scanf( "%d %d\n", &r, &c );
		  int i, j;
		  for( i=1; i<=r; i++ )
			   {
					for( j=1; j<=c; j++ )
						 scanf( "%c",  &f[ i ][ j ]);
					scanf( "\n" );
			   }
		  return;
	 }

bool work( void )
	 {
		  int i, j;
		  for( i=1; i<=r; i++ )
			   {
					for( j=1; j<=c; j++)
						 {
							  if ( f[ i ][ j ] == '#' )
								   {
										if ( j < c && i < r && f[ i + 1 ][ j ] == '#' && f[ i ][ j
	 + 1] == '#' && f[ i + 1 ][ j + 1 ] == '#')
											 {
												  f[ i ][ j ] = '/';
												  f[ i ][ j + 1 ] = '\\';
												  f[ i + 1][ j ] = '\\';
												  f[ i + 1 ][ j + 1 ] = '/';
											 }
										else
											 return false;
								   }
						 }
			   }
		  return true;
	 }

void out( void )
	 {
		  int i, j;
		  for( i=1; i<=r; i++ )
			   {
					   for( j=1; j<=c; j++ )
							printf( "%c", f[ i ][ j ] );
					   printf( "\n" );
			   }
		  return;
					
	 }

int main( void )
	 {
		  freopen( "3a1.in", "r", stdin );
		  freopen( "3a1.out", "w", stdout );
		  int t;
		  int i;

		  scanf( "%d\n", &t );

		  for( i=1; i<=t; i++ )
			   {
					ini(  );
					printf( "Case #%d:\n" , i);
					if (work(  ))
						 {
							  out(  );
						 }
					else
						 printf( "Impossible\n" );
			   }
		  
		  return 0;
	 }
