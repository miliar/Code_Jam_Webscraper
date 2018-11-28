// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <cstdio>
#include <cassert>
#include <string>
#include <iostream>

using namespace std;

struct testcase
{
	vector< string >	seq;
	vector< int >		orange_p_seq;
	vector< int >		blue_p_seq;
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
		int numberOfButtons = atoi( token );
		token = next_token;

		testcase	tc;

		for( int i = 0; i < numberOfButtons; ++i )
		{
			token = strtok_s( token, delim, &next_token );
			string R = token;
			token = next_token;

			token = strtok_s( token, delim, &next_token );
			int P = atoi( token );
			token = next_token;

			tc.seq.push_back( R );

			if( R == "O" )
				tc.orange_p_seq.push_back( P );
			else if( R == "B" )
				tc.blue_p_seq.push_back( P );
			else
				assert( false );
		}

		tcs.push_back( tc );
	}

	return tcs;
}

void moveorstay( const string &type, int &pos, int next_pos )
{
	if( next_pos == -1 )
	{
		// stay
		//cout << type << " stay " << pos << " - " << next_pos << endl;
	}

	else
	{
		if( pos < next_pos )
		{
			++pos;
			//cout << type << " move " << pos << " - " << next_pos << endl;
		}

		else if( pos > next_pos )
		{
			--pos;
			//cout << type << " move " << pos << " - " << next_pos << endl;
		}

		else
		{
			// stay
			//cout << type << " stay " << pos << endl;
		}
	}
}

void process( testcases &tcs )
{
	for( size_t i = 0; i < tcs.size(); ++i )
	{
		testcase	&tc = tcs[i];

		assert( tc.seq.empty() == false );

		int cur_pos_O = 1;
		int cur_pos_B = 1;
		vector< string >::iterator type = tc.seq.begin();
		vector< string >::iterator typeEnd = tc.seq.end();
		vector< int >::iterator next_pos_O = tc.orange_p_seq.begin();
		vector< int >::iterator end_pos_O = tc.orange_p_seq.end();
		vector< int >::iterator next_pos_B = tc.blue_p_seq.begin();
		vector< int >::iterator end_pos_B = tc.blue_p_seq.end();

		int count = 0;

		while( true )
		{
			++count;

			if( *type == "O" )
			{
				if( cur_pos_O < *next_pos_O )
				{
					// move
					++cur_pos_O;

					//cout << "O move " << cur_pos_O << endl;

					moveorstay( "B", cur_pos_B, next_pos_B == end_pos_B ? -1 : *next_pos_B );
				}

				else if( cur_pos_O > *next_pos_O )
				{
					// move
					--cur_pos_O;

					//cout << "O move " << cur_pos_O << endl;

					moveorstay( "B", cur_pos_B, next_pos_B == end_pos_B ? -1 : *next_pos_B );
				}

				else
				{
					// push
					//cout << "O push " << (next_pos_O == end_pos_O ? -1 : *next_pos_O) << endl;
					++next_pos_O;

					moveorstay( "B", cur_pos_B, next_pos_B == end_pos_B ? -1 : *next_pos_B );

					++type;
					if( type == typeEnd )
						break;
				}
			}

			else if( *type == "B" )
			{
				if( cur_pos_B < *next_pos_B )
				{
					// move
					++cur_pos_B;

					//cout << "B move " << cur_pos_B << endl;

					moveorstay( "O", cur_pos_O, next_pos_O == end_pos_O ? -1 : *next_pos_O );
				}

				else if( cur_pos_B > *next_pos_B )
				{
					// move
					--cur_pos_B;

					//cout << "B move " << cur_pos_B << endl;

					moveorstay( "O", cur_pos_O, next_pos_O == end_pos_O ? -1 : *next_pos_O );
				}

				else
				{
					// push
					//cout << "B push " << (next_pos_B == end_pos_B ? -1 : *next_pos_B) << endl;
					++next_pos_B;

					moveorstay( "O", cur_pos_O, next_pos_O == end_pos_O ? -1 : *next_pos_O );

					++type;
					if( type == typeEnd )
						break;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}
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

int _tmain(int argc, char* argv[])
{
	char *data = ""\
	"3\n"\
	"4 O 2 B 1 B 2 O 4\n"\
	"3 O 5 O 8 B 100\n"\
	"2 B 2 B 1";

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

