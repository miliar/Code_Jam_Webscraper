////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2009
// Qualificatino Round - C. 
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
  
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam 

*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

#define WELCOME		"welcome to code jam"
#define MOD			10000
#define MAX_LENGTH	500

int countSubSequences( const string& text, const string& target )
{
	int len = target.size();
	vector< int > table;
	table.resize( len );

	for ( int i = 0; i < len; ++i ) {
		table[ i ] = 0;
	}

	for ( int i = 0, size = text.size(); i < size; ++i ) {
		char c = text[ i ];
		for ( int index = 0; index < len; ++index ) {
			if ( c == target[ index ] ) {
				int curValue = table[ index ];
				if ( index == 0 ) {
					table[ 0 ] = ( curValue + 1 ) % MOD;
				}
				else {
					table[ index ] = ( curValue + table[ index - 1 ] ) % MOD;
				}
			}
		}
	}
	
	return table[ len - 1 ];
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	char buf[ MAX_LENGTH + 1 ];
	cin.getline( buf, MAX_LENGTH + 1 );

	for ( int i = 1; i <= count; ++i ) {
		string text;
		cin.getline( buf, MAX_LENGTH + 1 );
		text = buf;

		int total = countSubSequences( text, string( WELCOME ) );
		printf( "Case #%d: %04d\n", i, total );
	}

	return 0;
}
