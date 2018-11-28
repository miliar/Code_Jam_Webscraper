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
5 5 0 0 5
1
2
1
2
3
6 2 2 1000000000 6
1
2

Output
Case #1: 15
Case #2: 13


n, m, X, Y and Z

for i = 0 to n-1
  print A[i mod m]
  A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z

*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

unsigned long long countSeq( vector< unsigned long long >& seq )
{
	vector< unsigned long long > arr;
	int seqCnt = ( int ) seq.size();

	arr.resize( seqCnt );
	for ( int i = 0; i < seqCnt; ++i )
		arr[ i ] = 1;

	unsigned long long count = seqCnt;

	for ( int order = 0; order < seqCnt; ++order ) {
		bool hit = false;

		for ( int i = 0; i < seqCnt; ++i ) {
			unsigned long long me = seq[ i ];
			unsigned long long tot = 0;
			for ( int j = i + 1; j < seqCnt; ++j ) {
				if ( me < seq[ j ] ) tot = ( tot + arr[ j ] ) % 1000000007ULL;
			}
			arr[ i ] = tot;
			count = ( count + tot ) % 1000000007ULL;
			if ( tot > 0 ) hit = true;
		}

		if ( !hit )
			break;
	}

	return count;
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;

		vector< unsigned long long > arr;
		arr.resize( m );

		for ( int j = 0; j < m; ++j ) {
			cin >> arr[ j ];
		}

		vector< unsigned long long > seq;
		for ( int j = 0; j < n; ++j ) {
			seq.push_back( arr[ j % m ] );
			arr[ j % m ] = ( ( unsigned long long ) X * arr[ j % m ] + ( unsigned long long ) Y * ( j + 1 ) ) % Z;
		}

		unsigned long long res = countSeq( seq );
		unsigned modded = res % 1000000007ULL;
		cout << "Case #" << i << ": " << modded << endl;
	}

	return 0;
}
