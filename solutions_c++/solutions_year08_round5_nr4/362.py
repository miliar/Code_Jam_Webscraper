#include <iostream>
#include <cstdlib>

using namespace std;


const int MAX_H = 200, MOD = 10007;
int H, W;
long long dp[MAX_H][MAX_H];
int rock[MAX_H][MAX_H];


long long memo(int r, int c) {
	if (r > H || c > W || rock[r][c]) return 0;
	
	if (r == H && c == W) return 1;

	long long &rf = dp[r][c];
	if (rf != -1) return rf;

	rf = memo(r + 2, c + 1) + memo(r + 1, c + 2);
	rf %= MOD;

	return rf;
}


int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int R;
		cin >> H >> W >> R;
		
		memset(rock, 0, sizeof(rock));
		for (int i = 0; i < R; i++) {
			int r, c;
			cin >> r >> c;

			rock[r][c] = 1;
		}

		memset(dp, -1, sizeof(dp));
		long long ret = memo(1, 1);

		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}

