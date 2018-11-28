#include <iostream>
#include <vector>
#include <string>
using namespace std;

string solve(vector<string> board) {
	int left = 0;
	for (string& a : board) {
		for (char b : a) {
			if (b == '.')
				++left;
		}
	}

	vector<string> lines;
	for (int i = 0; i < 4; ++i) {
		string a, b;
		for (int j = 0; j < 4; ++j) {
			a += board[i][j];
			b += board[j][i];
		}
		lines.push_back(a);
		lines.push_back(b);
	}
	string a, b;
	for (int i = 0; i < 4; ++i) {
		a += board[i][i];
		b += board[i][3-i];
	}
	lines.push_back(a);
	lines.push_back(b);

	for (string line : lines) {
		bool onlyO = true, onlyX = true;
		for (char c : line) {
			if (c == '.' || c == 'X')
				onlyO = false;
			if (c == '.' || c == 'O')
				onlyX = false;
		}
		if (onlyO)
			return "O won";
		if (onlyX)
			return "X won";
	}

	return (left ? "Game has not completed" : "Draw");
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		vector<string> board(4);
		getline(cin, board[0]);
		getline(cin, board[0]);
		getline(cin, board[1]);
		getline(cin, board[2]);
		getline(cin, board[3]);
		cout << "Case #" << i+1 << ": " << solve(board) << endl;
	}
	return 0;
}
