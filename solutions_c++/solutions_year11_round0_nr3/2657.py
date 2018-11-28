#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

int N;
ll candy[1024];

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		cin >> N;

		ll xorz = 0;
		ll sumz = 0;

		ll minz = 100000000;

		for (int i = 0; i < N; ++i) {
			cin >> candy[i];

			xorz ^= candy[i];
			sumz += candy[i];

			minz = min(minz, candy[i]);
		}

		cout << "Case #" << tt << ": ";

		if (xorz != 0) {
			cout << "NO";
		} else {
			ll ans = sumz - minz;
			cout << ans;
		}

		cout << endl;
	}
	return 0;
}

