#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>

using std::cin;
using std::cout;
using std::string;
using std::vector;

typedef std::pair<int,int>	pi;

typedef unsigned __int64 u64;

int read_int() { int r; cin >> r; return r; }
string read_str() { string s; cin >> s; return s; }


int Solve()
{
	int R = read_int();
	int C = read_int();

	char * matrix = new char[R*C];

	memset( matrix, 0, R*C );

	for( int r = 0; r < R; ++r )
	{
		string row = read_str();
		for( int c = 0; c < C; ++c )
		{
			char tile_col = row[c];
			if( row[c] != '#' )
				tile_col = '.';
			matrix[ r*C + c ] = tile_col;
		}
	}

	bool failed = false;

	for( int r = 0; r < R &&!failed; ++r )
	{
		for( int c = 0; c < C && !failed; ++c )
		{
			if( matrix[r*C+c] == '#' )
			{
				// If at the edge then fail
				if( c+1 >= C || r+1 >= R )
				{
					failed = true;
					break;
				}

				if( matrix[r*C + c+1] != '#' ||
					matrix[(r+1)*C + c] != '#' ||
					matrix[(r+1)*C + c+1] != '#')
				{
					failed = true;
					break;
				}

				matrix[r*C + c] = '/';
				matrix[r*C + c+1] = '\\';
				matrix[(r+1)*C + c] = '\\';
				matrix[(r+1)*C + c+1] = '/';
			}
		}
	}

	if( failed )
	{
		delete [] matrix;
		printf( "Impossible\n" );
		return 0;
	}


	for( int r = 0; r < R; ++r )
	{
		for( int c = 0; c < C; ++c )
		{
			char tile = matrix[r*C+c];
			printf( "%c", tile );
		}
		printf( "\n" );
	}
	delete [] matrix;

	return 1;
}

int main(int argc, char* argv[])
{
	//freopen( "test.txt", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\A-large.in", "r", stdin );
	freopen( "C:\\Users\\Paul\\Downloads\\A-large.out", "w", stdout );

	int num_tests = read_int();

	for( int i = 0; i < num_tests; ++ i )
	{
		printf( "Case #%d:\n", i+1 );
		Solve();
		//printf( "%d\n", res );
	}

	return 0;
}

