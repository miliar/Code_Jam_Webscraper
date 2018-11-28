#include <iostream>

using namespace std;

int max_board[40][40];
bool board[40][40];
bool cut[40][40];
int res[40];
int n, m;

bool check(int r1, int c1, int r2, int c2) {
	for (int i = c1+1; i <= c2; i++) {
		if (board[r1][i] == board[r1][i-1]) {
			return false;
		}
	}

	for (int i = r1+1; i <= r2; i++) {
		if (board[i][c1] == board[i-1][c1]) {
			return false;
		}
	}

	for (int i = r1+1; i <= r2; i++) {
		for (int j = c1+1; j <= c2; j++) {
			if (board[i][j] == board[i-1][j] || board[i][j] == board[i][j-1]) {
				return false;
			}
		}
	}

	return true;
}

void update_max() {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (cut[i][j]) {
				max_board[i][j] = 0;
				continue;
			}

			int max_k = max_board[i][j];
			for (int k = 0; k <= max_k; k++) {
				bool brk = false;
				for (int ii = i; ii < i+k; ii++) {
					for (int jj = j; jj < j+k; jj++) {
						if (cut[ii][jj]) {
							brk = true;
							break;
						}
					}

					if (brk)
						break;
				}

				max_board[i][j] = k;

				if (brk) {
					max_board[i][j]--;
					break;
				}
			}
		}
	}

}

int main() {
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; cs++) {
		for (int i = 0; i < 40; i++) {
			res[i] = 0;
			for (int j = 0; j < 40; j++) {
				cut[i][j] = false;
				max_board[i][j] = 0;
			}
		}

		cin >> m >> n;

		for (int i = 0; i < m; i++) {
			string s;
			cin >> s;

			int col = 0;
			for (int j = 0; j < n/4; j++) {
				char c = s[j];
				int num;
				if (c >= '0' && c <= '9') {
					num = c - '0';
				} else if (c >= 'A') {
					num = c - 'A' + 10;
				}

				for (int k = 0; k < 4; k++) {
					if (num >= 8) {
						board[i][col] = true;
					} else {
						board[i][col] = false;
					}

					col++;
					num = num << 1;
					num %= 16;
				}
			}
		}

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				int k = 0;
				while (i + k < m && j + k < n) {
					if (check(i, j, i+k, j+k)) {
						max_board[i][j] = k+1;
					} else {
						break;
					}

					k++;
				}
			}
		}

		while (true) {
			int max_k = 0, row = 0, col = 0;
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (max_k < max_board[i][j]) {
						row = i;
						col = j;
						max_k = max_board[i][j];
					}
				}
			}

			if (!max_k) {
				break;
			}

			res[max_k]++;

			for (int i = row; i < row + max_k; i++) {
				for (int j = col; j < col + max_k; j++) {
					cut[i][j] = true;
				}
			}

			update_max();
		}

		int diff = 0;
		for (int i = 0; i < 40; i++) {
			if (res[i] > 0) {
				diff++;
			}
		}

		cout << "Case #" << cs << ": " << diff << endl;
		for (int i = 39; i >= 0; i--) {
			if (res[i] > 0) {
				cout << i << " " << res[i] << endl;
			}
		}
	}
}
