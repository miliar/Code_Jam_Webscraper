#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

ifstream fin( "C-large.in" );
ofstream fout( "C-large.out" );

#define cin fin
#define cout fout

#define MAX 2000000

int dig[20], ptr = 0;
int num[10];

int main() {
	int t;
	cin >> t;
	for( int T = 0; T < t; T++ ) {
		int a, b;
		cin >> a >> b;
		int res = 0;
		for( int i = a; i <= b; i++ ) {
			ptr = 0;
			int val = i;
			while( val ) {
				dig[ptr++] = val % 10;
				val /= 10;
			}
			reverse( dig, dig + ptr );
			for( int j = 0; j < ptr; j++ )	dig[j + ptr] = dig[j];
			int nptr = 0;
			for( int j = 1; j < ptr; j++ ) {
				if( dig[j] == 0 )	continue;
				val = 0;
				for( int k = 0; k < ptr; k++ ) {
					val = 10 * val + dig[(j + k)];
				}
				if( val <= i )	continue;
				if( val <= b )	num[nptr++] = val;
			}
			sort( num, num + nptr );
			res += unique( num, num + nptr ) - num;
		}
		cout << "Case #" << T + 1 << ": " << res << endl;
	}
	return 0;
}
