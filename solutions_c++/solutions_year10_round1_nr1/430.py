#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

#define line_length 8192
char board[100][100];
int T, K, N;

void displayBoard() {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c)
			cout << board[r][c];
		cout << endl;
	}
}

bool connect(int r0, int c0, char ch) {
	int r, c;
	// horizontal
	if (c0+K <= N) {
		for (c = c0+K-1; c >= c0; --c)
			if (board[r0][c] != ch)
				break;
		if (c < c0)
			return true;
	}
	// vertical
	if (r0+K <= N) {
		for (r = r0+K-1; r >= r0; --r)
			if (board[r][c0] != ch)
				break;
		if (r < r0)
			return true;
	}
	// diagonal
	if (r0+K <= N && c0+K <= N) {
		// forward slash
		for (r = r0+K-1, c = c0+K-1; r >= r0; --r, --c)
			if (board[r][c] != ch)
				break;
		if (r < r0)
			return true;
		// back slash
		for (r = r0+K-1, c = c0; r >= r0; --r, ++c)
			if (board[r][c] != ch)
				break;
		if (r < r0)
			return true;
	}
	return false;
}

int main() {
	string line;
	getline(cin, line);
	stringstream(line) >> T;
	for (int case_num = 1; case_num <= T; ++case_num) {
		getline(cin, line);
		stringstream(line) >> N >> K;
		for (int r = 0; r < N; ++r)
			for (int c = 0; c < N; ++c)
				board[r][c] = '.';
		for (int r = 0; r < N; ++r) {
			getline(cin, line);
			for (int c = 0; c < N; ++c)
				board[c][N-1-r] = line[c];
		}
		//displayBoard(); cout << endl;
		for (int c = 0; c < N; ++c) {
			for (int r = N-1; r >= 0; --r) {
				if (board[r][c] == '.')
					continue;
				for (int seek = r+1; ; ++seek) {
					if (seek == N || board[seek][c] != '.') {
						if (seek != r+1) {
							board[seek-1][c] = board[r][c];
							board[r][c] = '.';
						}
						break;
					}
				}
			}
		}
		//displayBoard(); cout << endl;
		bool connectRed = false, connectBlue = false;
		for (int r = 0; r < N && !(connectRed && connectBlue); ++r)
			for (int c = 0; c < N && !(connectRed && connectBlue); ++c) {
				if (!connectRed && connect(r, c, 'R'))
					connectRed = true;
				if (!connectBlue && connect(r, c, 'B'))
					connectBlue = true;
			}
		string result = "Neither";
		if (connectRed && connectBlue)
			result = "Both";
		else if (connectRed)
			result = "Red";
		else if (connectBlue)
			result = "Blue";
		cout << "Case #" << case_num << ": " << result << endl;
	}
}
