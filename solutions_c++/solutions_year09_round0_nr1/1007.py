////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2009
// Qualificatino Round - A. 
//
// Author : Kang, Jin-Kook, 2009.09.03
//
// * 
//

#include <stdio.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//
/*
Input 
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

Output 
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

#define MAX_CHARS	26	// Lowercase alphabet
#define MAX_L		15
typedef vector< map< char, bool > >	WordInfo;

WordInfo parseWord( string& word, const int l )
{
	int len = word.size();
	int index = -1;
	bool bOpen = false;

	WordInfo info;
	info.resize( l );

	for ( int i = 0; i < len; ++i ) {
		char c = word[ i ];
		if ( c == '(' ) {
			bOpen = true;
			++index;
		}
		else if ( c == ')' ) {
			bOpen = false;
		}
		else {
			if ( bOpen ) {
				info[ index ][ c ] = true;
			}
			else {
				info[ ++index ][ c ] = true;
			}
		}
	}

	/*
	for ( int i = 0; i < info.size(); ++i ) {
		vector< char >& inner = info[ i ];
		printf( "%d : ", i );
		for ( int j = 0; j < inner.size(); ++j ) {
			printf( "%c\t", inner[ j ] );
		}
		printf( "\n" );
	}
	*/

	return info;
}

int countMatches( vector< string >& dict, const int l, WordInfo& word )
{
	int count = 0;

	for ( int i = 0, len = dict.size(); i < len; ++i ) {
		string& cand = dict[ i ];
		bool bMatched = true;

		for ( int index = 0; index < l; ++index ) {
			if ( word[ index ][ cand[ index ] ] == false ) {
				bMatched = false;
				break;
			}
		}

		if ( bMatched ) ++count;
	}

	return count;
}

int main( int argc, char *argv[] )
{
	int count, l, d;
	cin >> l >> d >> count;

	// load dictionary
	vector< string > dict;
	string word;
	for ( int j = 0; j < d; ++j ) {
		cin >> word;
		dict.push_back( word );
	}

	// count
	for ( int i = 1; i <= count; ++i ) {
		string word;
		cin >> word;
		WordInfo wordInfo = parseWord( word, l );

		int total = countMatches( dict, l, wordInfo );
		cout << "Case #" << i << ": " << total << endl;
	}

	return 0;
}
