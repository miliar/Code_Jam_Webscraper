#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const char* INPUT_FILE_NAME  = "C-large.in";
const char* OUTPUT_FILE_NAME = "C-large.out";
//const char* INPUT_FILE_NAME  = "C-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "C-small-attempt0.out";

const string WELCOME = "welcome to code jam";
const int WELCOME_SIZE = 19;

int GetOutput( const string& strInput )
{
	int strSize = strInput.size();
	int count[ WELCOME_SIZE + 1 ];
	for( int i = 0; i <= WELCOME_SIZE ; ++i )
		count[ i ] = 0;
	for( int i = 0; i <= strSize; ++i )
	{
		char currentChar = strInput[ i ];

		if( currentChar == 'w' )
		{
			++count[ 0 ];
			if( count[ 0 ] > 10000 )
				count[ 0 ] %= 10000;
		}
		for( int j = 1; j < WELCOME_SIZE ; ++j )
		{
			if( currentChar == WELCOME[ j ] )
			{
				count[ j ] += count[ j-1 ];
				if( count[ j ] > 10000 )
					count[ j ] %= 10000;
			}
		}
	}

	return count[ WELCOME_SIZE-1 ]; 
}

string getZeroPadding( int num )
{
	string zeros;
	if( num < 10 )
		return "000";
	else if( num < 100 )
		return "00";
	else if( num < 1000 )
		return "0";
	else
		return "";
};

int main()
{
	int N;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);

	inputFileStream >> N;

	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	for( int i = 0; i < N; ++i )
	{
		inputFileStream.getline(buffer, 8192);
		strInput = buffer;

		int count = GetOutput( strInput );

//		if( count > 10000 )
//			count %= 10000;

		outputFileStream << "Case #" << i+1 << ": " << getZeroPadding( count ) << count << endl;
		cout << "Case #" << i+1 << ": " << getZeroPadding( count ) << count << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
