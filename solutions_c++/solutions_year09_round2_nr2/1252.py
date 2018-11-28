////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam 2009
// Round 1 - Problem B.
//
// Author : Kang, Jin-Kook, 2009.09.12
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
3
115
1051
6233
*/

//ifstream fin("input.txt");
//#define cin fin

string calcNextNum( string num )
{
	if ( num.size() == 1 ) return num + "0";

	vector< int > digits;

	int nStart = -1, prev = 10;
	for ( int i = 0; i < num.size(); ++i ) {
		int n = num[ i ] - '0';
		digits.push_back( n );

		if ( prev >= n ) {
			if ( nStart < 0 ) nStart = i - 1;
		}
		else {
			nStart = -1;
		}

		prev = n;
	}

	string result;
	if ( nStart == 0 ) {
		int nNext = 10;
		for ( int i = 0; i < digits.size(); ++i ) {
			if ( digits[ i ] < nNext && digits[ i ] > 0 ) {
				nNext = digits[ i ];
			}
		}

		vector< int > temp;
		for ( int i = 0; i < digits.size(); ++i ) {
			if ( digits[ i ] == nNext ) {
				nNext = -1;
				result += ( digits[ i ] + '0' );
				result += '0';
			}
			else {
				temp.push_back( digits[ i ] );
			}
		}

		sort( temp.begin(), temp.end() );

		for ( int i = 0; i < temp.size(); ++i ) {
			result += ( temp[ i ] + '0' );
		}
	}
	else {
		if ( nStart < 0 ) nStart = digits.size() - 1;

		for ( int i = 0; i < nStart - 1; ++i ) {
			result += ( digits[ i ] + '0' );
		}

		int nNext = 10;
		for ( int i = nStart - 1; i < digits.size(); ++i ) {
			if ( digits[ i ] < nNext && digits[ i ] > digits[ nStart - 1 ] ) {
				nNext = digits[ i ];
			}
		}

		vector< int > temp;
		for ( int i = nStart - 1; i < digits.size(); ++i ) {
			if ( digits[ i ] == nNext ) {
				nNext = -1;
				result += ( digits[ i ] + '0' );
			}
			else {
				temp.push_back( digits[ i ] );
			}
		}

		sort( temp.begin(), temp.end() );

		for ( int i = 0; i < temp.size(); ++i ) {
			result += ( temp[ i ] + '0' );
		}
	}

	return result;
}

/*
int minimum = INT_MAX;
void _findNum( vector< int >& digits, int n, int cur = 0, int d = 0 )
{
	if ( d == digits.size() ) {
		if ( cur > n && cur < minimum ) {
			minimum = cur;
			return;
		}
	}

	int result = 0;
	for ( int i = 0; i < digits.size(); ++ i ) {
		int a = digits[ i ];
		if ( a == -1 ) continue;
		digits[ i ] = -1;

		_findNum( digits, n, cur * 10 + a, d + 1 );

		digits[ i ] = a;
	}
}

int calcNextNum( int num )
{
	vector< int > digits;
	int n = num;

	while ( n > 0 ) {
		digits.push_back( n % 10 );
		n /= 10;
	}

	bool bLast = true;
	for ( int i = 0; i < ( int ) digits.size() - 1; ++i ) {
		if ( digits[ i ] > digits[ i + 1 ] ) {
			bLast = false;
			break;
		}
	}

	vector< int > a = digits;
	int result = 0;
	if ( bLast ) a.push_back( 0 );

	minimum = INT_MAX;
	_findNum( a, num );
	result = minimum;

	return result;
}
*/

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		string n;
		cin >> n;

		string result = calcNextNum( n );
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
