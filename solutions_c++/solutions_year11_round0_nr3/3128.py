#include <iostream>
#include <algorithm>
using namespace std;

int Sum( int a, int b ) {
	int ba[30], bb[30];
	int ap = 0, bp = 0;
	memset( ba, 0, sizeof ba );
	memset( bb, 0, sizeof bb );
	while( a > 0 ) {
		ba[ap++] = a % 2;
		a /= 2;
	}
	while( b > 0 ) {
		bb[bp++] = b % 2;
		b /= 2;
	}
	for( int i=0; i<15; i++ ) ba[i] = ( ba[i] + bb[i] ) % 2;

	int ret = 0;
	for( int i=14; i>=0; i-- ) {
		ret *= 2;
		ret += ba[i];
	}
	return ret;
}

int main() {
	freopen( "C_small.in", "r", stdin );
	freopen( "C_small.out", "w", stdout );

	int TC;
	cin >> TC;

	for( int TCC=1; TCC<=TC; TCC++ ) {
		int N, bag[15];
		cin >> N;
		int sum = 0;
		for( int i=0; i<N; i++ ) cin >> bag[i];
		
		int ret = -987654321;
		for( int i=0; i<(1<<N); i++ ) {
			int sean = 0;
			int b_sean = 0;
			int ptrk = 0;
			int b_ptrk = 0;
			for( int j=0; j<N; j++ ) {
				if( (i>>j) & 1 ) {
					sean += bag[j];
					b_sean = Sum( b_sean, bag[j] );
				}
				else {
					ptrk += bag[j];
					b_ptrk = Sum( b_ptrk, bag[j] );
				}
			}

			if( b_sean == 0 || b_ptrk == 0 ) continue;
			if( b_sean == b_ptrk ) ret = max( ret, sean );
		}
		

		cout << "Case #" << TCC << ": ";
		if( ret != -987654321 ) cout << ret << endl;
		else cout << "NO" << endl;
	}
}