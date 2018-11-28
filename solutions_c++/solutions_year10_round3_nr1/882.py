////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam 2010
// Round ? - Problem A.
//
// Author : Kang, Jin-Kook, 2010.05.23
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
 
*/

//ifstream fin("input.txt");
//#define cin fin

struct Pair
{
	int x;
	int y;
};

typedef vector< Pair >	PairVec;

inline bool cross( Pair& a, Pair& b )
{
	return ( ( a.x - b.x ) * ( a.y - b.y ) ) < 0;
}

int calcXPoints( PairVec& vecPair )
{
	int size = vecPair.size();
	int count = 0;

	for ( int i = 0; i < size; ++i ) {
		for ( int j = 0; j < i; ++j ) {
			if ( cross( vecPair[ i ], vecPair[ j ] ) )
				++count;
		}
	}

	return count;
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n;
		cin >> n;

		PairVec vecPair;
		vecPair.resize( n );
		for ( int j = 0; j < n; ++j ) {
			Pair& pair = vecPair[ j ];
			cin >> pair.x >> pair.y;
		}

		int nCross = calcXPoints( vecPair );

		cout << "Case #" << i << ": " << nCross << endl;
	}

	return 0;
}
