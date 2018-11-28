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
3 2 6
8 2 5 2 4 9
3 9 26
1 1 1 100 100 1 1 1 1 1 1 1 1 1 1 1 1 10 11 11 11 11 1 1 1 100
 
Output 
Case #1: 47
Case #2: 397
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
		int p, k, l;
		cin >> p >> k >> l;

		if ( p * k < l ) cout << "Case #" << i << ": Impossible" << endl;

		vector< int > freq;
		freq.resize( l );
		for ( int j = 0; j < l; ++j ) {
			cin >> freq[ j ];
		}

		sort( freq.begin(), freq.end() );

		long long total = 0;
		long long order = 1, tmp = k;
		for ( int j = l - 1; j >= 0; --j ) {
			total += ( long long ) freq[ j ] * order;
			
			if ( --tmp == 0 ) {
				tmp = k;
				order++;
			}
		}

		cout << "Case #" << i << ": " << total << endl;
	}

	return 0;
}
