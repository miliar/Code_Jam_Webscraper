#include<iostream>
#include<cstdlib>
using namespace std;

char word[ 5001 ][ 16 ];
char data[  15  ][ 27 ];

int main()
{
	FILE *fp = fopen( "A-small-attempt0.out" , "w" );
	int L,D,N;
	cin >> L >> D >> N;
	for ( int i = 1 ; i <= D ; ++ i )
		cin >> word[ i ];
	
	for ( int i = 1 ; i <= N ; ++ i )
	{
		for ( int j = 0 ; j < 15 ; ++ j )
		for ( int k = 0 ; k < 26 ; ++ k )
			data[ j ][ k ] = '\0';
		char a;cin >> a;
		int  count = 0;
		while ( a != '\n' )
		{ 
			if ( a == '(' )
			{
				int move = 0;
				while ( cin >> a && a != ')' )
					data[ count ][ move ++ ] = a;
				data[ count ][ move ] = '\0';
			}
			else 
			{
				data[ count ][ 0 ] = a;
				data[ count ][ 1 ] = '\0';
			}
			a = getchar();
			++  count;
		}
		int put = 0;
		for ( int p,k,j = 1 ; j <= D ; ++ j )
		{
			for ( k = 0 ; k < L ; ++ k )
			{
				for ( p = 0 ; data[ k ][ p ] ; ++ p )
					if ( data[ k ][ p ] == word[ j ][ k ] )
						break;
				if ( !data[ k ][ p ] ) break;
			}
			if ( k == L )
				++ put;
		}
		fprintf( fp , "Case #%d: %d\n",i,put);
	}
	fclose( fp );
} 
