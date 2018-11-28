#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 10000

long long l, h;
int n;

long long t[ MAXN + 1 ];

void ini( void )
	 {
		  scanf( "%d %lld %lld", &n, &l, &h );
		  int i;
		  for( i=1; i<=n; i++ )
			   scanf( "%lld", &t[ i ]);
		  return;
	 }

bool work( void )
	 {
		  long long i;
		  int j;
		  bool flag;
		  for( i=l; i<=h; i++ )
			   {
					flag = true;
					for ( j=1; j<=n; j++ )
						 if ( !( i % t[ j ] == 0 || t[ j ] % i == 0 ) )
							  {
								   flag = false;
								   break;
							  }
					if ( flag )
						 {
							  printf( "%lld\n", i );
							  return true;
						 }
			   }
		  return false;
	 }

int main( void )
{
	 int i, j;
	 freopen( "3a3.in", "r", stdin );
	 freopen( "3a3.out", "w", stdout );

	 int t;
	 scanf( "%d", &t );
	 for( i=1; i<=t; i++ )
		  {
			   ini(  );
			   printf( "Case #%d: ", i );
			   if ( !work (  ) )
					printf( "NO\n" );
		  }
	 return 0;
	 
}
