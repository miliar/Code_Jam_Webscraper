#ifndef _WIN32_WINNT            // Specifies that the minimum required platform is Windows Vista.
#define _WIN32_WINNT 0x0600     // Change this to the appropriate value to target other versions of Windows.
#endif

#include <stdio.h>
#include <tchar.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>
#include <algorithm>
#include <iomanip>

using namespace std;

bool harmony( 
	int& result,
	const int iLow,
	const int iHigh,
	const vector<int>& other )
{
	for( int i = iLow; i <= iHigh; ++i )
	{
		bool found = true;
		for( vector<int>::const_iterator it = other.begin();
			it != other.end(); ++it )
		{
			const int val = *it;
			if( (val > i ? val % i != 0 : i % val != 0) )
			{
				found = false;
				break;
			}
		}
		if( found )
		{
			result = i;
			return true;
		}
	}
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 3 )
	{
		cerr << "Invalid amount of arguments!";
		return 1;
	}

	ifstream input_file( argv[1] );
	if( !input_file.is_open() )
	{
		cerr << "Cannot open input file!";
		return 2;
	}

	ofstream output_file( argv[2] );
	if( !output_file.is_open() )
	{
		cerr << "Cannot open output file!";
		return 3;
	}

	string sLine;
	getline( input_file, sLine );
	int iCases = atoi( sLine.c_str() );
	for( int i = 0; i < iCases; ++i )
	{
		output_file << "Case #"<< i + 1 <<": ";
		getline( input_file, sLine );
		
		istringstream iss(sLine);
		vector<string> sValues;
		copy(istream_iterator<string>(iss),
			istream_iterator<string>(),
			back_inserter<vector<string> >(sValues));
		
		int iPlayers = atoi( sValues[0].c_str() );
		int iLow = atoi( sValues[1].c_str() );
		int iHigh = atoi( sValues[2].c_str() );
		
		getline( input_file, sLine );
		
		istringstream iss2(sLine);
		vector<string> sValues2;
		copy(istream_iterator<string>(iss2),
			istream_iterator<string>(),
			back_inserter<vector<string> >(sValues2));
		
		vector<int> iValues;
		iValues.reserve( sValues2.size() );

		for( size_t i = 0; i < sValues2.size(); ++i )
			iValues.push_back( atoi( sValues2[i].c_str() ) );

		int result = iLow;
		if( harmony( result, iLow, iHigh, iValues ) )
			output_file << result;
		else
			output_file << "NO";
		output_file << endl;
	}
	return 0;
}
