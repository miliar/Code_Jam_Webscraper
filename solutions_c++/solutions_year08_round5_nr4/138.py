#include <iostream>
#include <string>
using namespace std;

const int MOD = 10007;

int N, R, H, W, r, c;
int tab[100][100];
bool rock[100][100];

int main() {
	cin >> N;
	for (int tcs = 1; tcs <= N; tcs++) {
		cin >> H >> W >> R;
		memset(rock, 0, sizeof(rock));
		for (int i = 0; i < R; i++) {
			cin >> r >> c;
			r--; c--;
			rock[r][c] = true;
		}
		for (int i = H-1; i >= 0; i--) {
			for (int j = W-1; j >= 0; j--) {
				if (i == H-1 && j == W-1) {
					tab[i][j] = 1;
					continue;
				}
				tab[i][j] = 0;
				if (rock[i][j]) continue;
				if (i < H-2 && j < W-1) tab[i][j] += tab[i+2][j+1];
				if (i < H-1 && j < W-2) tab[i][j] += tab[i+1][j+2];
				tab[i][j] %= MOD;
			}
		}
		cout << "Case #" << tcs << ": " << tab[0][0] << endl;
	}
	return 0;
}
