#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <stdlib.h>

using namespace std;
typedef map<char, char>  PairMap;
typedef set<char>        CharSet;
struct CombMapValue 
{
	PairMap map;
	CharSet set;
};
typedef map<char, CombMapValue>  CombMap;
typedef map<char, CharSet>       OppoMap;


void calculate( ifstream& input, ofstream& output )
{
	unsigned combines = 0;
	input >> combines;


	CombMap combMap;
	for (unsigned i = 0; i < combines; ++i)
	{
		string pairs;
		input >> pairs;
		combMap[ pairs[0] ].map.insert(PairMap::value_type(pairs[1], pairs[2]));
		combMap[ pairs[0] ].set.insert(pairs[1]);

		combMap[ pairs[1] ].map.insert(PairMap::value_type(pairs[0], pairs[2]));
		combMap[ pairs[1] ].set.insert(pairs[0]);
	}

	unsigned oppos = 0;
	input >> oppos;
	
	OppoMap oppoMap;
	for (unsigned i = 0; i < oppos; ++i)
	{
		string pairs;
		input >> pairs;
		oppoMap[ pairs[0] ].insert(pairs[1]);
		oppoMap[ pairs[1] ].insert(pairs[0]);
	}

	unsigned len = 0;
	input >> len;

	string inString;
	input >> inString;

	CharSet combCheck;
	typedef map<char, unsigned> OppoCheck;
	OppoCheck oppoCheck;

	for (unsigned i = 0; i < len; ++i)
	{ 
		if ( inString[i] == 0x7f ) continue;

		if ( combCheck.find(inString[i]) != combCheck.end() )
		{
			char *lastChar;
			for ( int j = i - 1; j >= 0; --j )
			{
				if ( inString[j] != 0x7f ) 
				{
					lastChar = &inString[j];
					break;
				}
			}
			OppoMap::iterator it2 = oppoMap.find(*lastChar);
			if (  it2 != oppoMap.end() )
			{
				for (CharSet::iterator it = it2->second.begin(); it != it2->second.end(); ++it )
				{
					OppoCheck::iterator it3 = oppoCheck.find(*it);
					if ( it3 != oppoCheck.end())
					{
						it3->second -= 1;
						if ( it3->second == 0 ) oppoCheck.erase(it3);
					}

				}
			}

			*lastChar = combMap[*lastChar].map[inString[i]];
			// Place holder as invalid string
			inString[i] = 0x7f;
			//combCheck = combMap[*lastChar].set;
			i = i - 1;
		}

		if ( oppoCheck.find(inString[i]) != oppoCheck.end() )
		{

			memset( &inString[0], 0x7f, i + 1 );
			combCheck.clear();
			oppoCheck.clear();
			continue;
		}

		// This is a combineable char
		CombMap::iterator it = combMap.find(inString[i]);
		if (  it != combMap.end() )
		{
			combCheck = it->second.set;
		}
		else
		{
			combCheck.clear();
		}

		OppoMap::iterator it2 = oppoMap.find(inString[i]);
		if (  it2 != oppoMap.end() )
		{
			for (CharSet::iterator it = it2->second.begin(); it != it2->second.end(); ++it)
			{
				oppoCheck[*it] += 1;
			}
		}
	}

	output << '[';
	bool beg = true;
	for (unsigned i = 0; i < len; ++i )
	{
		if ( inString[i] != 0x7f )
		{
			if ( !beg )
			{
				output << ", ";
			}
			output << inString[i];
			if ( beg ) beg = false;
		}
	}

	output << ']' << endl;
}

int main( int argc, char *argv[] )
{

	if ( argc != 3 )
	{
		cerr << "Usage: Calculate <Input_File_Name> <Output_File_Name>";
		return EXIT_FAILURE;
	}
	else
	{
		string inputFile( argv[1] ), outputFile ( argv[2] );
		cout << "Get input from: " << inputFile << endl;
		cout << "Output file is: " << outputFile << endl;
		
		ifstream input( inputFile.c_str() );
		unsigned cases;
		input >> cases;
		cout << "We have got " << cases << " cases to cover" << endl;

		ofstream output( outputFile.c_str() );

		for ( unsigned i = 1; i <= cases; ++i )
		{
			output << "Case #" << i << ": "; 
			calculate( input, output );
		}

	}
	return EXIT_SUCCESS;
}
