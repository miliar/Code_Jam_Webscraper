#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

////////////////////////////////////////////////////////////////////////////////////
//
/*
Input
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

Output
Case #1: -25
Case #2: 6
*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int vectorCount, val;
		cin >> vectorCount;

		vector< int > v1;
		for ( int j = 0; j < vectorCount; ++j ) {
			cin >> val;
			v1.push_back( val );
		}

		vector< int > v2;
		for ( int j = 0; j < vectorCount; ++j ) {
			cin >> val;
			v2.push_back( val );
		}

		sort( v1.begin(), v1.end() );
		sort( v2.begin(), v2.end() );

		int s1 = 0, s2 = 0;
		for ( int j = 0; j < vectorCount; ++j ) {
			s1 += ( v1[ j ] * v2[ vectorCount - j - 1 ] );
			s2 += ( v2[ j ] * v1[ vectorCount - j - 1 ] );
		}

		int small = ( s1 < s2 ) ? s1 : s2;

		cout << "Case #" << i << ": " << small << endl;
	}

	return 0;
}
