#include <iostream>

using namespace std;

int main () {
	int caseno = 1;
	int cases;
	cin >> cases;
	for ( int caseno = 1; caseno <= cases; caseno ++ ) {
		long long N,K;
		cin >> N >> K;

		long long pattern = ( 1<< N) -1;
		long long on = ((K & pattern) == pattern);

		cout << "Case #" << caseno;
		if ( on ) 
			cout << ": ON" << endl;
		else
			cout << ": OFF" << endl; 



	}
	return 0;

};