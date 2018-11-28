/*
 * GCJ 2011 qualifying
 */
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
#include <iomanip>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T; cin >> T;
	for(int t = 1; t <= T; ++t) {
		int N; cin >> N;

		vi a(N);
		int xs = 0;
		int sm = 0;

		for(int i = 0; i < N; ++i) {
			cin >> a[i];
			xs ^= a[i];
			sm += a[i];
		}

		if( xs != 0 ) {
			cout << "Case #" << t << ": NO\n";
		} else {
			int ans = sm - *min_element(a.begin(), a.end());
			cout << "Case #" << t << ": " << ans << "\n";
		}
	}



	return 0;
}
