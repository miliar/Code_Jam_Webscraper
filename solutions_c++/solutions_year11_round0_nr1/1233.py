#include <iostream>
#include <vector>
#include <conio.h>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, ans = 0;
		int x[2] = {1, 1}, free[2] = {0, 0};
		cin >> N;

		while (N--) {
			char r;
			int p;
			cin >> r >> p;
			r = (r == 'O' ? 0 : 1);

			int d = max(abs(x[r] - p) - free[r], 0) + 1;
			free[r ? 0 : 1] += d;
			free[r] = 0;
			ans += d;
			x[r] = p;
		}

		cout << "Case #" << t << ": " << ans << endl;
	}
}