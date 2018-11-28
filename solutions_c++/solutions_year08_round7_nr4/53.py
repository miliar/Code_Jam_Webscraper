#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;


int R, C;
int kr, kc;
int dp[16][16][1 << 17];
char grid[5][5];


inline int ok(int r, int c) {
	if (r >= 0 && r < R && c >= 0 && c < C && grid[r][c] != '#')
		return 1;
	return 0;
}


int win(int r, int c, int state) {
	
	// cout << "r: " << r << " c: " << c << " state: " << state << endl;
	
	int pos = r * C + c;

	if (dp[r][c][state] != -1) return dp[r][c][state];

	int &rf = dp[r][c][state];

	for (int nr = r - 1; nr <= r + 1; nr++) {
		for (int nc = c - 1; nc <= c + 1; nc++) if (nr != r || nc != c) {
			int np = nr * C + nc;
			if (ok(nr, nc) && (state & (1 << np)) == 0) {
				if (!win(nr, nc, state | (1 << pos)))
					return rf = 1;
			}
		}
	}

	return rf = 0;
}


int solve() {
	memset(dp, -1, sizeof(dp));
	return win(kr, kc, 0);
}

int main() {
	int N;
	cin >> N;

	for (int t = 1; t <= N; t++) {
		cin >> R >> C;

		for (int i = 0; i < R; i++) {
			string lin;
			cin >> lin;

			for (int j = 0; j < C; j++) {
				grid[i][j] = lin[j];

				if (grid[i][j] == 'K') {
					kr = i;
					kc = j;
				}
			}
		}

		int ret = solve();
		
		string winner;
		if (ret == 1) winner = "A";
		else		  winner = "B";

		cout << "Case #" << t << ": " << winner << endl;
	}

	return 0;
}





