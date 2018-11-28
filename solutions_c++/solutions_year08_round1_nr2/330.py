#include <iostream>
#include <algorithm>

using namespace std;

class MaximumWeightedMatching;

int N, M;
int T;
int C;
int P [100][10];
int U [100];
int main () {
	cin >> C;
	for (int xxx = 1; xxx <= C; ++xxx) {
		cin >> N >> M;
		memset (P, 0, sizeof (P));
		memset (U, 0, sizeof (U));
		for (int i = 0; i < M; ++i) {
			cin >> T;
			U [i] = -1;
			for (int j = 0; j < T; ++j) {
				int t, m;
				cin >> t >> m;
				--t;
				if (m == 0) P [i][t] = 1;
				else U [i] = t;
			}
		}

		int res = N + 1;
		int resM = -1;
		for (int m = 0; m < (1 << N); ++m) {
			int cnt = 0;
			for (int j = 0; j < N; ++j) if (m & (1 << j)) ++cnt;
			int ok = 1;
			for (int i = 0; i < M && ok; ++i) {
				int doneI = 0;
				for (int j = 0; j < N && !doneI; ++j)
				    if ((P [i][j] && ((m & (1 << j)) == 0))
					|| (U [i] == j && (m & (1 << j)))) doneI = 1;
				if (!doneI) ok = 0;
			}
			if (ok) {
				if (res > cnt) {
					res = cnt;
					resM = m;
				}
			}
		}
		if (res == N + 1)
			cout << "Case #" << xxx  << ": IMPOSSIBLE" << endl;
		else {
			cout << "Case #" << xxx  << ":";
			for (int i = 0; i < N; ++i)
			    if (resM & (1 << i)) cout << " 1";
			    else cout << " 0";
			cout << endl;
		}
	}
}

