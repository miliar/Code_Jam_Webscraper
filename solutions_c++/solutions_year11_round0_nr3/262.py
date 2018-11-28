#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");
#define cin fin
#define cout fout

int t, n, test = 1;
int main() {
	for( cin >> t; t--; ) {
		int xor = 0, sum = 0, mn = 1000000000;
		cin >> n;
		for( int i = 0; i < n; i++ ) {
			int a;
			cin >> a;
			sum += a;
			mn = min( mn, a );
			xor ^= a;
		}
		cout << "Case #" << test++ << ": ";
		if( xor == 0 )
			cout << sum - mn << endl;
		else
			cout << "NO" << endl;

	}
	return 0;
}