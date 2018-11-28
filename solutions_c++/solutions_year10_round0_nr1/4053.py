#include <iostream>

using namespace std;


int
main( ) {

  int t , n , k , two_to_n;


	cin >> t;

	for( int i = 0 ; i < t ; ++i ) {
	
		cin >> n >> k;

		two_to_n = 1;

		for( int j = 0 ; j < n ; ++j ) {

			two_to_n *= 2;
		}


		k -= ( two_to_n - 1 );

		if( k >= 0 ) {

			if( ( k % two_to_n ) == 0 ) {

				cout << "Case #" << i + 1 << ": ON" << endl;

			} else {

				cout << "Case #" << i + 1 << ": OFF" << endl;
			}

		} else {

			cout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}

	return 0;
}
