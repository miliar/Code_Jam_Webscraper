////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2011
// Qualificatino Round - B. 
//
// Author : Kang, Jin-Kook, 2011.05.07
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
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
 	
Output 
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin


std::map< char, std::map< char, char > > combines;
std::map< char, std::map< char, bool > > opposites;

string calcList( string const& strn, int const& n )
{
	string result;

	for ( int i = 0; i < n; ++i ) {
		char now = strn[ i ];
		int len = result.length();

		char last = ( len > 0 ) ? result[ len - 1 ] : 0;
		if ( last && combines[ now ][ last ] ) {
			result.pop_back();
			result += combines[ now ][ last ];
		}
		else {
			bool bClear = false;
			for ( int j = 0; j < len; ++j ) {
				if ( opposites[ now ][ result[ j ] ] ) {
					bClear = true;
					break;
				}
			}
			if ( bClear )
				result.clear();
			else
				result += now;
		}
	}

	return result;
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int c, d, n;
		string strc, strd, strn;

		combines.clear();
		opposites.clear();
		for ( char j = 'A'; j <= 'Z'; ++j ) {
			for ( char k = 'A'; k <= 'Z'; ++k ) {
				combines[ j ][ k ] = 0;
				opposites[ j ][ k ] = false;
			}
		}

		cin >> c;
		for ( int j = 0; j < c; ++j ) {
			cin >> strc;
			combines[ strc[ 0 ] ][ strc[ 1 ] ] = strc[ 2 ];
			combines[ strc[ 1 ] ][ strc[ 0 ] ] = strc[ 2 ];
		}

		cin >> d;
		for ( int j = 0; j < d; ++j ) {
			cin >> strd;
			opposites[ strd[ 0 ] ][ strd[ 1 ] ] = true;
			opposites[ strd[ 1 ] ][ strd[ 0 ] ] = true;
		}

		cin >> n >> strn;

		string result = calcList( strn, n );
		string output = "[";
		size_t len = result.length();
		bool bFirst = true;
		for ( size_t j = 0; j < len; ++j ) {
			if ( !bFirst ) output += ", ";
			bFirst = false;
			output += result[ j ];
		}
		output += "]";
		cout << "Case #" << i << ": " << output << endl;
	}

	return 0;
}
