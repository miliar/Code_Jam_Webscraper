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

typedef vector< string > TPattern;

bool to_red( 
	const TPattern& orig, 
	TPattern& result,
	const size_t rows,
	const size_t cols)
{
	int opened_cols = 0;
	for( size_t i = 0; i < rows; ++i )
	{
		string str;
		int opened_rows = 0;
		int temp_opened_cols = 0;
		for( size_t j = 0; j < cols; ++j )
		{
			char ch = orig[i][j];
			if( ch == '#' )
			{
				if( opened_rows > 0 )
				{
					const char lch = str[j-1];
					if( lch == '/' )
					{
						ch = '\\';
						--opened_rows;
						++temp_opened_cols;
					}
					else if( lch == '\\' )
					{
						ch = '/';
						--opened_rows;
						--opened_cols;
					}
					else
					{
						if( opened_cols > 0 )
						{
							const char uch = result[i-1][j];
							if( uch == '/' )
								ch = '\\';
							else
								ch = '/';
							++opened_rows;
						}
						else
						{
							ch = '/';
							++opened_rows;
						}
					}
				}
				else
				{
						if( i > 0 && opened_cols > 0 )
						{
							const char uch = result[i-1][j];
							if( uch == '/' )
							{
								ch = '\\';
							}
							else
							{
								ch = '/';
							}
							++opened_rows;
						}
						else
						{
							ch = '/';
							++opened_rows;
						}
				}
			}
			str.push_back( ch );
		}
		if( opened_rows != 0 )
			return false;
		result.push_back( str );
		opened_cols += temp_opened_cols;
	}
	return opened_cols == 0;
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
		output_file << "Case #"<< i + 1 <<":\n";
		getline( input_file, sLine );
		
		istringstream iss(sLine);
		vector<string> sValues;
		copy(istream_iterator<string>(iss),
			istream_iterator<string>(),
			back_inserter<vector<string> >(sValues));
		
		int rows = atoi( sValues[0].c_str() );
		int cols = atoi( sValues[1].c_str() );
		
		TPattern pattern;
		pattern.reserve( rows );
		for( int j = 0; j < rows; ++j )
		{
			getline( input_file, sLine );
			pattern.push_back( sLine );
		}
		
		TPattern result;

		if( to_red( pattern, result, rows, cols ) )
		{
			for( TPattern::const_iterator it = result.begin();
				it != result.end(); ++it )
				output_file << *it << endl;
		}
		else
		{
			output_file << "Impossible\n";
		}		
	}
	return 0;
}
