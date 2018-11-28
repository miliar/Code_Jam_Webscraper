#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int H, W, R, r[10], c[10], res[100][100];
bool rock[100][100];

void read_data () {
	memset (res, 0, sizeof (res));
	memset (rock, 0, sizeof (rock));

	cin >> H >> W >> R;
	for (int i = 0; i < R; ++i) { cin >> r[i] >> c[i]; rock[r[i]-1][c[i]-1] = true; }
}

void solve () {
	res[0][0] = 1;

	for (int i = 0; i < H; ++i)
		for (int j = 0; j < W; ++j) {
			if ((i == 0 && j == 0) || rock[i][j]) continue;
			if (i >= 2 && j >= 1) res[i][j] = (res[i][j] + res[i-2][j-1]) % 10007;
			if (i >= 1 && j >= 2) res[i][j] = (res[i][j] + res[i-1][j-2]) % 10007;
		}

	cout << res[H-1][W-1] << endl;
}

int main () {
	freopen ("D-small-attempt0.in", "r", stdin);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t+1 << ": ";

		read_data ();
		solve ();
	}

	return 0;
}
