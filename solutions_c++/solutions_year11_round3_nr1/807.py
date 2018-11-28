// GCJR1C.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
using namespace std;


bool has2x2Blue( int row, int col, vector<string>& res )
{
	if( row >= res.size( ) ) return false;
	if( row + 1 >= res.size( ) ) return false;
	if( col >= res[ 0 ].size( ) ) return false;
	if( col + 1 >= res[ 0 ].size( ) ) return false;

	return ( res[ row ][ col ] == '#' &&
		res[ row ][ col + 1 ] == '#' &&
		res[ row + 1 ][ col ] == '#' &&
		res[ row + 1 ][ col + 1 ] == '#' );
}

void replaceIt( int row, int col, vector<string>& res )
{
	res[ row ][ col ] = '/';
	res[ row ][ col + 1 ] = '\\';
	res[ row + 1 ][ col ] = '\\';
	res[ row + 1 ][ col + 1 ] = '/';
	
}

int main(int argc, char* argv[])
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );
	int cases = 0;
	cin >> cases;
	for( int ct = 0; ct < cases; ++ct )
	{

		int rows, cols;
		cin >> rows >> cols;

		vector<string> whiteblue;
		string t;

		for( int i = 0; i < rows; ++i )
		{
			cin >> t;
			whiteblue.push_back( t );			
		}

		//replace

		vector<string> results;

		for( int i = 0; i < whiteblue.size( ); ++i )
		{
			for( int j = 0; j < whiteblue[ i ].size( ); ++j )
			{
				if( has2x2Blue( i, j, whiteblue ) )
				{
					replaceIt( i, j, whiteblue );
				}
			}
		}

		bool hasBlueSymbol = false;

		for( int i = 0; i < whiteblue.size( ); ++i )
		{
			for( int j = 0; j < whiteblue[ i ].size( ); ++j )
			{
				if( whiteblue[ i ][ j ] == '#' )
				{
					hasBlueSymbol = true;
					break;
				}
			}

			if( hasBlueSymbol )
			{
				break;
			}
		}

		cout << "Case #" << ct + 1 << ":" << endl;

		if( hasBlueSymbol )
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for( int i = 0; i < whiteblue.size( ); ++i )
			{
					cout << whiteblue[ i ]<< endl;
			}
		}
	}

	return 0;
}

