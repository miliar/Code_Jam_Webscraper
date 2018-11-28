#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>

using namespace std;

const char* INPUT_FILE_NAME  = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";
//const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "A-small.in";
//const char* OUTPUT_FILE_NAME = "A-small.out";

bool GetOutput( fstream& inputFileStream )
{
	unsigned int N, K;
	inputFileStream >> N >> K;

	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	bitset<32> binaryValue;
	unsigned int iPos = 0;
	while( K > 0 )
	{
		binaryValue.set( iPos, K & 0x1 );
		++iPos;
		K = K >> 1;
	}

	for( unsigned int i = 0; i < N; ++i)
	{
		if( binaryValue[ i ] == false )
		{
			return false;
		}
	}

	return true;
}

int main()
{
	int T;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> T;

	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	for( int i = 0; i < T; ++i )
	{
		bool bOn = GetOutput( inputFileStream );
		string strOn = bOn ? "ON" : "OFF";

		outputFileStream << "Case #" << i+1 << ": " << strOn << endl;
		cout << "Case #" << i+1 << ": " << strOn << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
