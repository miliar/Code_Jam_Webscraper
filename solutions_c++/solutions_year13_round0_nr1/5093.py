#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int num_tests;
	cin >> num_tests;

	for (int test_id = 1; test_id <= num_tests; test_id++) {
		int tx = -1, ty = -1;
		char board[5][5];
		for (int i = 0; i < 4; i++) {
			cin >> board[i];
			for (int j = 0; j < 4; j++)
				if (board[i][j] == 'T') {
					tx = i;
					ty = j;
				}
		}
		int win = -1;
		for (int t = 0; t < 2; t++) {
			char now = ((t == 0)? 'X': 'O');
			if (tx >= 0)
				board[tx][ty] = now;
			int d1 = 0, d2 = 0;
			for (int i = 0; i < 4; i++) {
				int cnt_x = 0, cnt_y = 0;
				for (int j = 0; j < 4; j++) {
					cnt_x += ((board[i][j] == now)? 1: 0);
					cnt_y += ((board[j][i] == now)? 1: 0);
				}
				d1 += ((board[i][i] == now)? 1: 0);
				d2 += ((board[i][3 - i] == now)? 1: 0);
				if (cnt_x == 4 || cnt_y == 4) {
					win = t;
					break;
				}
			}
			if (d1 == 4 || d2 == 4) {
				win = t;
				break;
			}
		}
		cout << "Case #" << test_id << ": ";
		if (win >= 0)
			cout << ((win == 0)? 'X': 'O') << " " << "won" << endl;
		else {
			bool em = false;
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					if (board[i][j] == '.')
						em = true;
			if (em)
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}
	}
	return 0;
}
