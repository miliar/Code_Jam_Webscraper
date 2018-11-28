#include <vector>
#include <cstdio>
#include <cassert>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

struct testcase
{
	int L;
	int t;
	int N;
	int C;
	int *parsecs;
	int *data;
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
		int L = atoi( token );
		token = next_token;

		token = strtok_s( token, delim, &next_token );
		int t = atoi( token );
		token = next_token;

		token = strtok_s( token, delim, &next_token );
		int N = atoi( token );
		token = next_token;

		token = strtok_s( token, delim, &next_token );
		int C = atoi( token );
		token = next_token;

		testcase	tc;

		tc.L = L;
		tc.t = t;
		tc.N = N;
		tc.C = C;

		tc.parsecs = new int[C];

		for( int i = 0; i < C; ++i )
		{
			token = strtok_s( token, delim, &next_token );
			int parsec = atoi( token );
			token = next_token;

			tc.parsecs[i] = parsec;
		}

		tc.data = new int[N];

		for( int j = 0; j < N; )
		{
			for( int i = 0; i < C; ++i )
			{
				tc.data[j] = tc.parsecs[i];

				++j;

				if( j >= N )
					break;
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

		int time = 0;
		int dist = tc.t*0.5;

		for( int j = 0; j < tc.N; ++j )
		{
			if( tc.data[j] < dist )
			{
				time += tc.data[j]*2;
				dist -= tc.data[j];
				tc.data[j] = 0;
			}

			else
			{
				time += dist*2;
				tc.data[j] -= dist;
				dist = 0;

				break;
			}
		}

		sort( tc.data, tc.data + tc.N, greater<int>() );

		int L = tc.L;
		for( int k = 0; k < tc.N; ++k )
		{
			if( L != 0 )
			{
				if( tc.data[k] != 0 )
				{
					time += tc.data[k];
					tc.data[k] = 0;
				}
				--L;
			}

			else
			{
				if( tc.data[k] != 0 )
				{
					time += tc.data[k]*2;
					tc.data[k] = 0;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << time << endl;
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

