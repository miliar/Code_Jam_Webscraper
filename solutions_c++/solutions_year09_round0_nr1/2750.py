#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const char* INPUT_FILE_NAME  = "A-small-attempt1.in";
const char* OUTPUT_FILE_NAME = "A-small-attempt1.out";

bool checkWithCandidates( set<string>& dictionary, string& prefix )
{
	int prefixSize = prefix.size();

	for each ( const string& word in dictionary )
	{
		if( word.substr( 0, prefixSize ).compare( prefix ) == 0 )
			return true;
	}
	return false;
}

void createCandidateSet( int L, set<string>& candidates, string& pattern, set<string>& dictionary )
{
	int curIndex = 0;
	for( int i = 0; i < L; ++i )
	{
		if( pattern[ curIndex ] == '(' )
		{
			int endIndex = pattern.find( ')', curIndex );

			set<string> newCandidates;
			for( int j = curIndex + 1; j < endIndex; ++j )
			{
				string currentChar = pattern.substr( j, 1 );

				if( candidates.size() == 0 )
				{
					if( checkWithCandidates( dictionary, currentChar ) )
						newCandidates.insert( currentChar );
				}
				else
				{
					for each ( const string& candidate in candidates )
					{
						string newStr = candidate + currentChar;
						if( checkWithCandidates( dictionary, newStr ) )
							newCandidates.insert( newStr );
					}
				}
			}
			swap( newCandidates, candidates );

			curIndex = endIndex + 1;
		}
		else
		{
			string currentChar = pattern.substr( curIndex, 1 );

			if( candidates.size() == 0 )
				candidates.insert( currentChar );
			else
			{
				set<string> newCandidates;
				for each ( const string& candidate in candidates )
				{
					newCandidates.insert( candidate + currentChar );
				}
				swap( newCandidates, candidates );
			}
			++curIndex;
		}
	}
}

int main()
{
	int L, D, N;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);

	inputFileStream >> L >> D >> N;

	// dictionary »ý¼º
	set<string> dictionary;

	for( int i = 0; i < D; ++i )
	{
		inputFileStream >> strInput;
		dictionary.insert( strInput );
	}

	for( int i = 0; i < N; ++i )
	{
		inputFileStream >> strInput;
		set<string> candidates;
		createCandidateSet( L, candidates, strInput, dictionary );

		set<string> result;
		set_intersection( dictionary.begin(), dictionary.end(), candidates.begin(), candidates.end(), inserter( result, result.begin() ) );

		outputFileStream << "Case #" << i+1 << ": " << result.size() << endl;
		cout << "Case #" << i+1 << ": " << result.size() << endl;
		for each ( const string& r in result )
			cout << r << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}

/*
string convertNumber(const string alien_number, const string source_lan, const string target_lan)
{
	AlienNumber alienNumberFrom(source_lan);
	AlienNumber alienNumberTo(target_lan);

	alienNumberFrom.setAlienNumber(alien_number);
	long lNumber= alienNumberFrom.getLongNumber();

	alienNumberTo.setLongNumber(lNumber);
	return alienNumberTo.getAlienNumber();
}
*/