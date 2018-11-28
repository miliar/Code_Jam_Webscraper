#include <iostream>
#include <string.h>
using namespace std;

const	int		max_data_n = 5004;

const 	int		max_length = 15;
 
string 	data[ max_data_n ];

int main()
{
	freopen( "a.in" , "r" , stdin );
	freopen( "a.out" , "w" , stdout );
	int		length1;
	int		data_n;
	int		mode_n;
	bool	map[ max_length ][ 26 ];
	cin >> length1 >> data_n >> mode_n;
	for ( int i = 0 ; i < data_n ; ++ i )
		cin >> data[ i ];
	int		count;
	for ( int i = 0 ; i < mode_n; ++ i )
	{
		string mode;
		cin >> mode;		
		int p = 0;
		
		for ( int j = 0 ; j < max_length ; ++ j )
			for ( int k = 0 ; k < 26 ; ++ k )
				map[ j ][ k ] = false;
		for ( int j = 0 ; j < length1 ; ++ j )
		{
			if ( mode[ p ] == '(' )
			{
				++ p;
				while ( mode[ p ] != ')' )
				{
					map[ j ][ mode[ p ] - 'a' ] = true;
					++ p;
				}
			}
			else
				map[ j ][ mode[ p ] - 'a' ] = true;
			++ p;
		}
		bool	able;
		count  = 0;
		for ( int j = 0 ; j < data_n ; ++ j )
		{
			able = true;
		
			for ( int k = 0 ; k < length1 ; ++ k )		
			if ( ! map[ k ][ data[ j ][ k ] - 'a' ] )
			{
				able = false;
				break;
			}
			if ( able )
			 ++ count;
		}
		cout << "Case #" << i + 1 << ": " << count << "\n";
	}
	return 0;
	
}

