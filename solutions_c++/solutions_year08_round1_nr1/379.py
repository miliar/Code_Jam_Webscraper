#include <iostream>
#include <algorithm>

using namespace std;

int N;
int X [8], Y [8];
int T;

int main () {
	cin >> T;
	for (int xxx = 1; xxx <= T; ++xxx) {
		cin >> N;
		for (int i = 0; i < N; ++i) cin >> X [i];
		for (int i = 0; i < N; ++i) cin >> Y [i];
		sort (X, X+N);
		int res = 9000000;
		do {
			int y = 0;
			for (int i = 0; i < N; ++i)
			    y += X [i] * Y [i];
			res <?= y;
		} while (next_permutation (X, X + N));
		cout << "Case #" << xxx  << ": " << res << endl;
	}
}
