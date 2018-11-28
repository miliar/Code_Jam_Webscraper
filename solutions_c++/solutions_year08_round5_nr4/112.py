#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	int H, W, R;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		printf("Case #%d: ", cn);
		cin >> H >> W >> R;

		vector <vector <int> > table(H, vector <int> (W, 0));
		table[0][0] = 1;

		for (int i = 0; i < R; ++i) {
			int x, y;
			cin >> x >> y;
			table[x - 1][y - 1] = -1;
		}

		for (int i = 1; i < H; ++i) {
			for (int j = 1; j < W; ++j) {
				if (table[i][j] == -1) continue;
				int r1 = 0, r2 = 0;
				if (i >= 2) r1 >?= table[i - 2][j - 1];
				if (j >= 2) r2 >?= table[i - 1][j - 2];
				table[i][j] = (r1 + r2) % 10007;
			}
		}
		cout << table[H - 1][W - 1] << endl;
	}
}

