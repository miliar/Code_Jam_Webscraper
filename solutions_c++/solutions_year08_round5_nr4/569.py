#include <iostream>
using namespace std;

bool rock[101][101];
int numPoss[101][101];

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int H, W, R;
		cin >> H >> W >> R;
		for (int j = 0; j < H; j++)
			for (int k = 0; k < W; k++) {
				rock[j][k] = false;
				numPoss[j][k] = 0;
			}
		numPoss[0][0] = 1;
		for (int j = 0; j < R; j++) {
			int r, c;
			cin >> r >> c;
			rock[r-1][c-1] = true;
		}
		for (int j = 0; j < H; j++)
			for (int k = 0; k < W; k++) {
				if (rock[j][k]) continue;
				numPoss[j][k] %= 10007;
				numPoss[j+2][k+1] += numPoss[j][k];
				numPoss[j+1][k+2] += numPoss[j][k];
			}
		cout << "Case #" << i+1 << ": " << numPoss[H-1][W-1] << endl;
	}
}
