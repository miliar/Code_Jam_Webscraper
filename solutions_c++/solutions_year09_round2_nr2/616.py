/**
 * Round 1B, 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }



int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T;
	cin >> T; cin >> ws;

	char buf[256];

	for(int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";

		cin.getline(buf, 255);
		int n = strlen(buf);

		if( next_permutation(buf, buf+n) ) {
			cout << buf;
		} else {

			sort(buf, buf+n);

			if(buf[0] != '0') {
				cout << buf[0] << '0' << &buf[1];
			} else {
				int p = 0;
				while( buf[p] == '0' ) ++p;

				cout << buf[p];

				buf[p] = '0';
				sort(buf, buf+n);

				cout << buf;
			}
		}

		cout << "\n";
	}


	return 0;
}
