#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 36
#define MAXM 28
#define MAXS 100

int t;
char rules[ MAXN + 1  ][ 3 ];
char op[ MAXM + 1 ][ 2 ];
char str[ MAXS + 1 ];
char result[ MAXS + 1 ];
int c, d, n;
int lr;

void ini( void )
	 {
		  scanf( "%d ", &c );
		  int i;
		  for( i=1; i<=c; i++ )
					scanf( "%c%c%c ", &rules[ i ][ 0 ], &rules[ i ][ 1 ],
	 &rules[ i ][ 2 ] );
		  scanf( "%d ", &d );
		  for( i=1; i<=d; i++ )
			   scanf( "%c%c ", &op[ i ][ 0 ], &op[ i ][ 1 ] );
		  scanf( "%d ", &n );
		  scanf( "%s\n", str );
		  return ;
		  
	 }

void work(  )
	 {
		  int i, j, k;
		  int s1[ MAXS + 1 ], s2[ MAXS + 1 ], s3[ MAXS + 1 ], s4[ MAXS + 1 ];
		  int ls2 = 0, ls1 = 0;
		
		  for( i=0; i<=MAXM + 1; i++ )
			   s2[ i ] = s1[ i ] = -1;
          memset( s4, 0, sizeof( s4 ) );
		  char temp;  bool flag, flag2;
			   
		  lr = 0;
		  for( i=0; i<n; i++ )
			   {
					flag = false;
					temp = str[ i ];
					if ( ls1 > 0 )
						 {
							  for( j=1; j<=ls1; j++ )
								   if ( temp == rules[ s1[ j ] ][ 1 - s3[ j ] ] )
              					   {
									   temp = rules[ s1[ j ] ][ 2 ];
									   lr--;if (flag2) ls2--;
									   break;
								   }
						 }
					if ( ls2 > 0 )
						 {
							  for( j=1; j<=ls2; j++ )
								   if ( temp == op[ j ][ 1 - s4[ j ] ] )
										{
											 lr = 0;
											 ls1 = 0;
											 ls2 = 0;
											 flag = true;
											 break;
										}
						 }
					if ( flag ) continue;
					
					lr++;
					result[ lr ] = temp;

					ls1 = 0;
					for( j=1; j<=c; j++ )
						 {
							  if ( temp == rules[ j ][ 0 ] )
								  {
									   ls1++;
									   s1[ ls1 ] = j;
									   s3[ ls1 ] = 0;
								  }
							  else if ( temp == rules[ j ][ 1 ] )
								   {
										ls1++;
										s1[ ls1 ] = j;
										s3[ ls1 ] = 1;
								   }
						 }
					flag2 = false;
					for ( j=1; j<=d; j++ )
						 {
							  if ( temp == op[ j ][ 0 ] )
								   {
										ls2++;
										s2[ ls2 ] = j;
										s4[ ls2 ] = 0;
										flag2 = true;
								   }
							  else if ( temp == op[ j ][ 1 ] )
								   {
										ls2++;
										s2[ ls2 ] = j;
										s4[ ls2 ] = 1;
										flag2 = true;
								   }
						 }
			   }
		  
		  return ;
	 }



int main( void )
	 {
		  int i, j;
		  freopen( "2.in", "r", stdin );
		  freopen( "2.out", "w", stdout );

		  scanf( "%d\n", &t );
		  for( i=1; i<=t; i++ )
			   {
					ini(  );
					work(  );
					printf( "Case #%d: [", i );
					for( j=1; j<lr; j++ )
						 printf( "%c, ", result[ j ] );
					if (lr != 0 ) printf( "%c]\n", result[ j ] );
					else printf( "]\n" );
			   }
		  return 0;
	 }
