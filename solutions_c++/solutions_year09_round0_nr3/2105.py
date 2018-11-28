#include<iostream>
#include<cstdlib>
#include<string>
using namespace std;

char ch[ 502 ];
char as[ 20 ] = "welcome to code jam";

int dfs( int k , int s , int L )
{
	if ( k == 19 ) return 1;
	if ( s >= L ) return 0;
	int i,value = 0;
	for ( i = s ; i < L ; ++ i )
	if  ( ch[ i ] == as[ k ] )
	{
		int move = 1;
		while ( ch[ i+1 ] == as[ k ] )
		{
			++ move;
			++ i;
		}
		value = ( value + move*dfs( k+1 , i+1 , L ) )%10000;
	}
	return value;
}

int main()
{
	FILE *fp = fopen( "C-small-attempt6.out" , "w" );
	int T;cin >> T;getchar();
	for ( int i = 1 ; i <= T ; ++ i )
	{
		gets( ch );
		int L = strlen( ch );
		int sum = 0;
		for ( int j = 0 ; j < L ; ++ j )
			if ( ch[ j ] == 'w' )
			{
				int move = 1;
				while ( ch[ j+1 ] == 'w' )
				{
					++ move;
					++ j;
				}
				sum = ( sum + move*dfs( 1 , j+1 , L ) )%10000;
			}
		fprintf( fp , "Case #%d: " , i );
		if ( sum < 10 )
			fprintf( fp , "000" );
		else if ( sum < 100 )
			fprintf( fp , "00" );
		else if ( sum < 1000 )
			fprintf( fp , "0");
		fprintf( fp , "%d\n" , sum );
	}
	fclose( fp );
}
