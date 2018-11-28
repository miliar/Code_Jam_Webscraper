////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam 2010
// Round 1 - Problem B.
//
// Author : Kang, Jin-Kook, 2010.05.22
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
2
5
6

Output 
Case #1: 5
Case #2: 8
*/

//ifstream fin("input.txt");
//#define cin fin

#define MAX_NUM		500
#define MOD			100003
int arr[ MAX_NUM + 1 ][ MAX_NUM + 1 ];
int com[ MAX_NUM + 1 ][ MAX_NUM + 1 ];

inline int _getCount( int num, int rank )
{
	if ( rank == 1 ) return 1;
	if ( arr[ num ][ rank ] >= 0 ) return arr[ num ][ rank ];

	int sum = 0;
	for ( int i = 1; i <= rank - 1; ++i ) {
		long long local = _getCount( rank, i );
		int combi = com[ num - rank - 1][ rank - i - 1 ];

		local = ( local * combi ) % MOD;
		sum = ( sum + local ) % MOD;
	}

	return sum;
}

void initialize( vector< int >& counts )
{
	for ( int i = 0; i < MAX_NUM + 1; ++i ) {
		for ( int j = 0; j < MAX_NUM + 1; ++j ) {
			arr[ i ][ j ] = -1;
		}
	}
	for ( int i = 0; i < MAX_NUM + 1; ++i ) {
		for ( int j = 0; j < MAX_NUM + 1; ++j ) {
			com[ i ][ j ] = 0;
		}
	}

	// combination
	com[ 0 ][ 0 ] = 1;
	for ( int i = 1; i <= 256; ++i ) {
		com[ i ][ 0 ] = 1;
		for ( int j = 1; j <= i; ++j ) {
			com[ i ][ j ] = ( com[ i - 1 ][ j ] + com[ i - 1 ][ j - 1 ] ) % MOD;
			//cout << i << ", " << j << " : " << com[ i ][ j ] << endl;
		}
	}

	// gogo
	counts.resize( MAX_NUM + 1 );
	for ( int i = 2; i < 500; ++i ) {
		int sum = 0;
		for ( int rank = 1; rank < i; ++rank ) {
			arr[ i ][ rank ] = _getCount( i, rank );
			sum = ( sum + arr[ i ][ rank ] ) % MOD;
		}
		counts[ i ] = sum;
	}
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	vector< int > counts;
	initialize( counts );

	for ( int i = 1; i <= count; ++i ) {
		int n;
		cin >> n;

		int result = counts[ n ];
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
