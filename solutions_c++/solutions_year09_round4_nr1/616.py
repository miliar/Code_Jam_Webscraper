#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <list>
#include <algorithm>

using namespace std;

const char* INPUT_FILE_NAME  = "A-large.in";
const char* OUTPUT_FILE_NAME = "A-large.out";
//const char* INPUT_FILE_NAME  = "A-small-attempt0.in";
//const char* OUTPUT_FILE_NAME = "A-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "A-small.in";
//const char* OUTPUT_FILE_NAME = "A-small.out";

int GetOutput( fstream& inputFileStream )
{
	int N;
	inputFileStream >> N;

	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	list<int> rows;

	for( int i = 0 ; i < N ; ++i )
	{
		inputFileStream.getline(buffer, 8192);
		string strInput = buffer;

		int maxOne = 0;
		for( int j = 0; j < N ; ++j )
		{
			if( strInput[ j ] == '1' )
			{
				maxOne = j;
			}
		}
		rows.push_back( maxOne );
	}

	int currentRow = 0;
	int moveCount = 0;

	for( currentRow = 0 ; currentRow < N ; ++currentRow )
	{
		list<int>::const_iterator it;
		int currentMoveCount = 0;
		for( it = rows.begin() ; it != rows.end() ; ++it, ++currentMoveCount )
		{
			if( *it <= currentRow )
			{
				moveCount += currentMoveCount;
				rows.erase( it );
				break;
			}
		}
	}

	return moveCount;
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
		int count = GetOutput( inputFileStream );

		outputFileStream << "Case #" << i+1 << ": " << count << endl;
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
