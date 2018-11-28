////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2011
// Qualificatino Round - C. 
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
2
5
1 2 3 4 5
3
3 5 6
 
Output 
Case #1: NO
Case #2: 11
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

#define MAX_CANDIES		1000

int calcSplit( int const* numbers, int count, int addSum = 0, int xorSumA = 0, int xorSumB = 0, int countA = 0, int countB = 0 )
{
	if ( count > 0 ) {
		int last = numbers[ count - 1 ];
		int a = calcSplit( numbers, count - 1, addSum + last, xorSumA ^ last, xorSumB, countA + 1, countB );
		int b = calcSplit( numbers, count - 1, addSum, xorSumA, xorSumB ^ last, countA, countB + 1 );
		return max( a, b );
	}
	else {
		return ( xorSumA == xorSumB && countA > 0 && countB > 0 ) ? addSum : 0;
	}
}

int main( int argc, char *argv[] )
{
	int numbers[ MAX_CANDIES ];

	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n;

		cin >> n;
		for ( int j = 0; j < n; ++j )
			cin >> numbers[ j ];

		int nResult = calcSplit( numbers, n );
		if ( nResult > 0 )
			cout << "Case #" << i << ": " << nResult << endl;
		else
			cout << "Case #" << i << ": NO" << endl;
	}

	return 0;
}
