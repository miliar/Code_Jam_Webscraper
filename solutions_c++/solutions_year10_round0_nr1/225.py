#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for( int i = 0; i < t; i++ ) {
		int n,m;
		cin >> n >> m;
		cout << "Case #" << (i+1) << ": ";
		if( (1<<n)-1 == m % (1<<n) ) {
			cout << "ON" << endl;
		} else {
			cout << "OFF" << endl;
		}
	}
	return 0;
}

