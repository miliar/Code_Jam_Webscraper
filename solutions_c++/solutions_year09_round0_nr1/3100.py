
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define FILENAME_IN "A-large.in"
#define FILENAME_OUT "A-large.out"

int main()
{
	ifstream fin( FILENAME_IN );
	if ( !fin )
	{
		return 1;
	}

	ofstream fout( FILENAME_OUT );
	if ( !fout )
	{
		return 1;
	}

	int L = 0;
	int D = 0;
	int N = 0;
	vector< string > alphabet;
	vector< string > testcases;

	fin >> L >> D >> N;

	// Remove the newline symbol
	fin.get();

	// Because of some stupid compilers
	int i = 0;

	std::string word;
	for ( i = 0; i < D; ++i )
	{
		getline( fin, word );
		alphabet.push_back( word );
	}

	std::string test;
	for ( i = 0; i < N; ++i )
	{
		getline( fin, test );
		testcases.push_back( test );
	}

	i = 1;
	for ( vector< string >::iterator iter = testcases.begin(); iter != testcases.end(); ++iter, ++i )
	{
		int result = 0;
		std::string::iterator iterTest = (*iter).begin();

		std::string token;
		std::vector< std::string > vTokens;
		bool bInPattern = false;

		while ( iterTest != (*iter).end() )
		{
			if ( *iterTest == '(' )
			{
				bInPattern = true;
			}
			else if ( *iterTest == ')' )
			{
				bInPattern = false;

				vTokens.push_back( token );
				token.clear();
			}
			else
			{
				if ( bInPattern )
				{
					token += *iterTest;
				}
				else
				{
					token = *iterTest;
					vTokens.push_back( token );
					token.clear();
				}
			}

			++iterTest;
		}

		for ( std::vector< std::string >::iterator iterWords = alphabet.begin();
			  iterWords != alphabet.end();
			  ++iterWords  )
		{
			std::vector< std::string >::iterator iterTokens = vTokens.begin();
			bool bMatch = true;

			for ( std::string::iterator iWord = (*iterWords).begin();
				  iWord != (*iterWords).end();
				  ++iWord, ++iterTokens )
			{
				if ( (*iterTokens).find_first_of( *iWord ) == std::string::npos )
				{
					bMatch = false;
					break;
				}
			}

			if ( bMatch )
			{
				++result;
			}
		}

		fout << "Case #" << i << ": " << result << std::endl;
	}

	fout.close();
	fin.close();

	return 0;
}
