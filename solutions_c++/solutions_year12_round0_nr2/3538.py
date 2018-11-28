/**
 * GCJ 2012, Q, B
 */
#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;
template<typename T> inline int sz(const T& x) { return (int)x.size(); }


int main() {
	int T; cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		int n, s, p;
		cin >> n >> s >> p;

		vi sc(n);
		for(int i = 0; i < n; ++i)
			cin >> sc[i];

		int res = 0;

		for(int i = 0; i < n; ++i) {
			int m = sc[i]/3;
			m += (sc[i] % 3) ? 1 : 0;

			if( m >= p ) {
				++res;
			} else if( s > 0 && sc[i] >= max(2, 3*p-4) ) {
				++res;
				--s;
			}
		}

		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}
