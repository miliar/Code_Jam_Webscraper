#include <iostream>
#include <NTL/ZZ.h>

NTL_CLIENT

using namespace std;

int main() {
	int cases;
	
	cin >> cases;
	for( int c = 1; c <= cases; ++c ) {
		int n;
		cin >> n;
		ZZ a = to_ZZ("1");
		ZZ b = to_ZZ("3");
		ZZ a2, b2;
		for( int i = 0; i < n-1; ++i ) {
			a2 = 3*a+b;
			b2 = 5*a+3*b;
			a = a2;
			b = b2;
		}
		ZZ res = b  + SqrRoot( a * a * 5 );
		res = res % 1000;
		cout << "Case #" << c << ": ";
		printf( "%03d\n", to_int(res) );
	}
	return 0;
}
