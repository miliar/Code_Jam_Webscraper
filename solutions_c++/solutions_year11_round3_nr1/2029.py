#include <iostream>
#include "../common/defines.h"
using namespace std;

int main()
{
	CASES( c )
	{
		int h, w;
		cin >> h >> w;
		char** tiles = new char*[h];

		REP( i, h )
		{
			tiles[i] = new char[w];
			cin >> tiles[i];
		}
		REP( i, h ) REP( j, w )
		{
			if( tiles[i][j] == '#' )
			{
				if( j + 1 >= w || tiles[i][j+1] != '#' ) goto imp;
				if( i + 1 >= h || tiles[i+1][j] != '#' ) goto imp;
				if( i + 1 >= h|| j + 1 >= w || tiles[i+1][j+1] != '#' ) goto imp;

				tiles[i][j] = '/';
				tiles[i][j+1] = '\\';
				tiles[i+1][j] = '\\';
				tiles[i+1][j+1] = '/';
			}
		}
		
		ANSWER( "" );
		REP( i, h ) cout << tiles[i] << "\n";
		continue;
imp:
		ANSWER( "\nImpossible" );
	}
	return 0;
}
