/**
 * Round 2, 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }

LL mat[40];

LL solve(int N) {
	LL swaps = 0;

	while(true) {

		int i;
		for(i = 0; i < N; ++i) {
			LL r = mat[i];
			if( r>>(i+1) )
				break;
		}

		if( i == N )
			break;

		for(int j = i+1; j < N; ++j) {
			LL r = mat[j];
			if( r>>(i+1) == 0 ) {

				for(int k = j; k >= i+1; --k) {
					swap( mat[k], mat[k-1] );
					swaps++;
				}

				break;
			}
		}
	}

	return swaps;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);



	int T; cin >> T;
	for(int tc = 1; tc < T+1; ++tc) {
		int N; cin >> N;

		for(int i = 0; i < N; ++i) {
			string s; cin >> s;

			mat[i] = 0;

			for(int j = 0; j < N; ++j) {
				if( s[j] == '1' )
					mat[i] |= 1LL<<j;
			}
		}

		LL ans = solve(N);

		cout << "Case #" << tc << ": ";
		cout << ans << '\n';
	}


	return 0;
}
