#include <vector>
#include <cstdio>
#include <cassert>
#include <string>
#include <iostream>

using namespace std;

struct testcase
{
	char tiles[50][50];
	int row;
	int col;
};

typedef	vector< testcase >	testcases;

testcases	getTestCase( char *data )
{
	testcases	tcs;

	const char *delim = " \t\n";

	vector<char> data2( data, data + strlen(data) );

	int numberOfTestcases = 0;
	char *token = &data2[0];
	char *next_token = 0;

	token = strtok_s( token, delim, &next_token );
	numberOfTestcases = atoi( token );
	token = next_token;
		
	for( int j = 0; j < numberOfTestcases; ++j )
	{
		token = strtok_s( token, delim, &next_token );
		int ROW = atoi( token );
		token = next_token;

		token = strtok_s( token, delim, &next_token );
		int COL = atoi( token );
		token = next_token;

		testcase	tc;

		tc.row = ROW;
		tc.col = COL;

		for( int y = 0; y < ROW; ++y )
		{
			for( int x = 0; x < COL; )
			{
				char value = 0;
				sscanf(token,"%c", &value );
				++token;

				if( value == 10 )
					continue;

				tc.tiles[y][x] = value;

				++x;
			}
		}

		tcs.push_back( tc );
	}

	return tcs;
}

long getSize( const char *path )
{
	long size = 0;

	FILE *fp = 0;
	if( fopen_s( &fp, path, "rt" ) == 0 )
	{
		fseek( fp, 0, SEEK_END );
		size = ftell( fp );
		fclose( fp );
	}

	return size;
}

void getRead( const char *path, char *buffer, int size, int maxSize )
{
	FILE *fp = 0;
	if( fopen_s( &fp, path, "rt" ) == 0 )
	{
		fread_s( buffer, maxSize, size, 1, fp );
		fclose( fp );
	}
}

void process( testcases &tcs )
{
	for( size_t i = 0; i < tcs.size(); ++i )
	{
		testcase	&tc = tcs[i];

		bool impossible = false;
		for( int y = 0; y < tc.row; ++y )
		{
			int red = 0;
			for( int x = 0; x < tc.col; ++x )
			{
				if( tc.tiles[y][x] == '#' )
					++red;				
			}

			if( red & 0x1 )
			{
				impossible = true;
				break;
			}
		}

		if( impossible == false )
		{
			for( int x = 0; x < tc.col; ++x )		
			{
				int red = 0;
				for( int y = 0; y < tc.row; ++y )
				{
					if( tc.tiles[y][x] == '#' )
						++red;				
				}

				if( red & 0x1 )
				{
					impossible = true;
					break;
				}
			}
		}

		if( impossible == false )
		{
			for( int y = 0; y < tc.row - 1; ++y )
			{
				for( int x = 0; x < tc.col - 1; ++x )
				{
					if( tc.tiles[y][x] == '#' && tc.tiles[y][x + 1] == '#' &&
						tc.tiles[y + 1][x] == '#' && tc.tiles[y + 1][x + 1] == '#' )
					{
						tc.tiles[y][x] = '/';
						tc.tiles[y][x+1] = '\\';
						tc.tiles[y+1][x] = '\\';
						tc.tiles[y+1][x+1] = '/';
					}
				}
			}

			for( int y = 0; y < tc.row; ++y )
			{
				for( int x = 0; x < tc.col; ++x )
				{
					if( tc.tiles[y][x] == '#' )
					{
						impossible = true;
						break;
					}
				}

				if( impossible == true )
					break;
			}
		}

		cout << "Case #" << i+1 << ":" << endl;

		if( impossible == true )
		{
			cout << "Impossible" << endl;
		}

		else
		{
			for( int y = 0; y < tc.row; ++y )
			{
				for( int x = 0; x < tc.col; ++x )
				{
					cout << tc.tiles[y][x];
				}

				cout << endl;
			}
		}
	}
}

int main(int argc, char* argv[])
{
	if( argc < 2 )
		return 0;

	char *path = argv[1];

	long size = getSize( path );

	if( size != 0 )
	{
		vector< char >	buffer( size + 1 );

		getRead( path, &buffer[0], size, size + 1 );

		buffer[ size ] = 0;
		
		testcases	tcs = getTestCase( &buffer[0] );

		process( tcs );
	}

	return 0;
}

