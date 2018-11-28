// Recycled.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

struct Pair {
	int n;
	int m;

	Pair( int a, int b ) {
		n = a;
		m = b;
	}
};
int main() {
	int test_cases;

	cin >> test_cases;

	for( int i = 0; i < test_cases; i++ ) {
		vector<string> arr;
		string a;
		string b;
		string m;
		int ia, ib;

		cin >> ia >> ib;

		for( int j = ia; j <= ib; j++ ) {
			// If less then 10 have no recycled pairs
			if( j >= 10 ) {
				m = static_cast<ostringstream*>( &(ostringstream() << j ) )->str();

				// Loop through for the length of j
				for( int k = 0; k < (int)m.length(); k++  )  {

					// Move the back to the front
					m = m[ m.size()-1 ] + m;
					// Remove the back
					m = m.substr( 0, m.size()-1 );
					int new_m = atoi( m.c_str() );
					
					// If the new num is > n but < b add to list
					if( new_m > j && new_m <= ib  ) {

						string temp = static_cast<ostringstream*>( &(ostringstream() << j ) )->str();
						arr.push_back( temp+m );
					}
					
				}
			}
		}
		// Assure there are no duplicates
		sort( arr.begin(), arr.end() );
		arr.erase( unique( arr.begin(), arr.end() ), arr.end() );
		cout << "Case #" << i+1 << ": " << arr.size() << endl;
	}
}

