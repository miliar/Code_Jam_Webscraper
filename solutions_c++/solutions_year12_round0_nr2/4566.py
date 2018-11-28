#include <iostream>
#include <cstdio>

using namespace std;

void solve() {
	int N, S, p;
	cin >> N >> S >> p;
	
	int res = 0;
	for (int i = 0; i < N; ++i) {
		int t;
		cin >> t;
		if (t >= p + 2*max(0, p - 1)) {
			res++;
		} else {
			if (S > 0 && t >= p + 2*max(0, p - 2)) {
				S--;
				res++;
			}
		}
	}
	
	static int testID;
	cout << "Case #" << ++testID << ": " << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t--)
		solve();
	return 0;
}