#include <iostream>
using namespace std;

char 	data[ 600 ];
int		func[ 255 ];


int main()
{
	freopen( "a.in" , "r" , stdin );
	freopen( "a.out" , "w" , stdout );
	memset( func  , 0 ,sizeof ( func) );
	string  a = " welcome to code jam";//这里没有俩字符是一样的。。如果有相邻的俩字符是一样的呢？ 
	int		dp[ 50 ];
	int		temp = 1;
	int		case_n;
	scanf( "%d\n"  , & case_n );
	int		lenght1;
	char 	mc;
	for ( int count = 1 ; count <= case_n ; ++ count )
	{
		memset( dp , 0 , sizeof( dp ) );
		dp[ 0 ] = 1;
		scanf( "%c" , & mc );
		while ( mc != '\n' )
		{
			for ( int i = 1 ; i < a.length() ; ++ i )
			if ( mc == a[ i ] )
			{
				dp[ i ] += dp[ i - 1 ];
				dp[ i ] %= 10000;
			}
			scanf( "%c" , & mc );
		}
		int res = dp[ a.length() - 1 ];
		
		printf( "Case #%d: " , count  );
		
		
		if ( res < 1000 )
			printf( "0" );
		if ( res < 100 )
			printf( "0" );
		if ( res < 10 )
			printf( "0" );
		printf( "%d\n", res );
	}
}
