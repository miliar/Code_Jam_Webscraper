#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;

bool specmatch( char c, std::string& letters )
{
	for ( size_t i = 0; i < letters.size( ); i++ )
	{
		if ( c == letters[ i ] )
			return true;
	}

	return false;
}

bool isMatch( std::string& spec, std::string& word )
{
	size_t specLoc = 0;
	/* Try to match each element against that part of the spec */
	size_t count = 0;
	for ( size_t i = 0; i < word.size( ); i++ )
	{
		/* Attempt to retrieve the first letter from the spec */
		if ( spec[ specLoc ] != '(' )
		{
			if ( spec[specLoc] == word[ i ] )
			{
				count++;
				specLoc++;
				continue;
			}
			else
				return false;
		}

		/* Handle the case where we've got parenthesese */
		std::string paren;
		specLoc++;
		for ( ; spec[specLoc]!=')'; specLoc++ )
		{
			paren += spec[specLoc];
		}
		specLoc++;
		if ( specmatch( word[ i ], paren ) )
		{
			count++;
			continue;
		}

		return false;
	}
	if ( count == word.size( ) )
		return true;
	return false;
}

int main( )
{
	int L,N,D;

	cin >> L >> D >> N;

	/* Read D number of words in dictionary */
	std::vector< std::string > dictionary;

	//_asm int 3;
	for ( int i = 0; i < D; i++ )
	{
		std::string temp;
		cin >> temp;
		dictionary.push_back( temp );
	}

	/* Parse the inputs */
	for ( int i = 0; i < N; i++ )
	{
		std::string toDecode;
		cin >> toDecode;

		/* Parse this monster into what we need */
		std::vector< std::string > cutDown;

		/* Copy any that match the requirements */
		size_t count = 0;
		for ( size_t j = 0; j < dictionary.size( ); j++ )
		{
			if ( isMatch( toDecode, dictionary[ j ] ) )
				count++;
		}

		cout << "Case #" << (i+1) << ": " << count << std::endl;
	}
}