#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

string Rotate(vector <string> board, int N, int K)
{
	vector <string> rotated(N, string(N, '.'));
	for (int y = 0; y < N; y++) {
		int rx = N - 1;
		for (int x = N - 1; x >= 0; x--) {
			if (board[y][x] != '.') {
				rotated[rx][N - y - 1] = board[y][x];
				rx--;
			}
		}
	}
	int flag = 0;
	int dx[] = {0, 1, 1, 1};
	int dy[] = {1, 0, 1,-1}; 
	for (int d = 0; d < 4; d++) {
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				char c = rotated[y][x];
				for (int k = 0; k < K; k++) {
					int px = x + dx[d] * k;
					int py = y + dy[d] * k;
					if (px < 0 || px >= N || py < 0 || py >= N || rotated[py][px] != c) {
						c = 'N';
					}
				}
				if (c == 'R') {
					flag |= 1;
				} else if (c == 'B') {
					flag |= 2;
				}
			}
		}
	}
	char ret[][10] = {"Neither", "Red", "Blue", "Both"};
	return ret[flag];
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N, K;
		cin >> N >> K;
		vector <string> board(N);
		for (int i = 0; i < N; i++) {
			cin >> board[i];
		}

		string ret = Rotate(board, N, K);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
