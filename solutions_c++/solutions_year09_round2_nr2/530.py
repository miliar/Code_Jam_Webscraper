#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

const char* INPUT_FILE_NAME  = "B-large.in";
const char* OUTPUT_FILE_NAME = "B-large.out";
//const char* INPUT_FILE_NAME  = "B-small-attempt1.in";
//const char* OUTPUT_FILE_NAME = "B-small-attempt1.out";
//const char* INPUT_FILE_NAME  = "B-small.in";
//const char* OUTPUT_FILE_NAME = "B-small.out";

void GetOutput( vector<int>& output, string number )
{
	for( int i = 0 ; i < 22 ; ++i )
		output[ i ] = 0;

	for( unsigned int i = 0 ; i < number.size() ; ++i )
	{
		output[ number.size() - 1 - i ] = number[ i ] - '0';
	}

	unsigned int i, j;
	for( i = 0 ; i < number.size() + 1 ; ++i )
	{
		int changeCandidateIndex = -1;
		int changeCandidateValue = 99999;
		for( j = 0 ; j < i ; ++j )
		{
			if( output[ j ] > output[ i ] )
			{
				if( output[ j ] < changeCandidateValue )
				{
					changeCandidateIndex = j;
					changeCandidateValue = output[ j ];
				}
			}
		}

		if( changeCandidateIndex != -1 )
		{
			output[ changeCandidateIndex ] = output[ i ];
			output[ i ] = changeCandidateValue;
			sort( output.begin(), output.begin() + i, greater<int>() );
			break;
		}
	}
}

void printNumber( ostream& outputStream, vector<int>& number )
{
	bool numberStarted = false;
	for( int i = 21 ; i >= 0 ; --i )
	{
		if( number[ i ] == 0 )
		{
			if( numberStarted )
				outputStream << number[ i ];
		}
		else
		{
			outputStream << number[ i ];
			numberStarted = true;
		}
	}
}

int main()
{
	int N;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> N;

	for( int i = 0; i < N; ++i )
	{
		string number;
		inputFileStream >> number;

		vector<int> numberVector( 22 );
		GetOutput( numberVector, number );

		outputFileStream << "Case #" << i+1 << ": ";
		printNumber( outputFileStream, numberVector );
		outputFileStream << endl;

		cout << "Case #" << i+1 << ": ";
		printNumber( cout, numberVector );
		cout << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
