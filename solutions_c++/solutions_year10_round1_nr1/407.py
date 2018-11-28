#include <iostream>
#include <fstream>

using namespace std;

int dirX[8] = {1, 1, 1, 0, -1, -1, -1, 0};
int dirY[8] = {1, 0, -1, -1, -1, 0, 1, 1};

bool isSpace(int x, int y, int dx, int dy, int n, int K);
bool haveWin(int x, int y, int dx, int dy, int n, int K, char c);
bool isInSize(int x, int y, int n);

char board[51][51];

int main() {
	ofstream out("a.out");
	int T;
	cin >> T;
	for (int nth = 1; nth <= T; nth++) {
		int n, K;
		cin >> n >> K;
		//char board[n][n];
		for (int i =0 ; i< n; i++) {
			for (int j =0 ; j < n; j++) {
				board[i][j] = '.';
			}
		}
		for (int i = n-1; i >= 0; i--) {
			string str;
			cin >> str;
			int j = n-1;
			for (int k = n-1; k >= 0; k--) {
				if (str[k] != '.') {
					board[j][i] = str[k];
					j--;
				}
			}
		}
		bool win[2];
		win[0] = false;
		win[1] = false;
		// 다 떨궜고..
		for (int i = 0 ; i< n; i++) {
			for (int j = 0 ; j < n; j++) {
				char c = board[i][j];
				if (c == '.') continue;
				bool isRed = (c == 'R');
				if (isRed && win[0]) continue;
				if (!isRed && win[1]) continue;
				// 주변에 dir[k]방향으로 K개의 공간이 있는지 보고
				// 있다면 그 방향으로 검사해봄.
				for (int k = 0; k < 8; k++) {
					if (/*isSpace(i, j, di, dj, n, K)
							&&*/ haveWin(i, j, dirX[k], dirY[k], n, K, c)) {
						if (isRed) win[0] = true;
						else 	   win[1] = true;
					}
				}
			}
		}
		out << "Case #" << nth << ": ";
		if (win[0] && win[1]) out << "Both";
		else if (win[0]) out << "Red";
		else if (win[1]) out << "Blue";
		else out << "Neither";
		out << endl;
	}
}
bool isSpace(int x, int y, int dx, int dy, int n, int K) {
	/*
	for (int i = 0; i < K; i++) {
		int x2 = x + dx * i;
		int y2 = y + dy * i;
		if (!isInSize(x2, y2)) return false;
	}
	return true;
	*/
}

bool haveWin(int x, int y, int dx, int dy, int n, int K, char c) {
	for (int i = 0; i < K; i++) {
		int x2 = x + dx * i;
		int y2 = y + dy * i;
		if (!isInSize(x2, y2, n)) return false;
		if (board[x2][y2] != c) return false;
	}
	return true;
}

bool isInSize(int x, int y, int n) {
	return x >= 0 && y >= 0 && x < n && y < n;
}
