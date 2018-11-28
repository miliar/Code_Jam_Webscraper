#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

string whoWon(const vector<string> &board) {
	if (any_of(board.begin(), board.end(),
			[](const string &row) {
				return all_of(row.begin(), row.end(), [](char c) {return c=='T'||c=='X';});
			}))
		return "X won";

	if (any_of(board.begin(), board.end(),
			[](const string &row) {
				return all_of(row.begin(), row.end(), [](char c) {return c=='T'||c=='O';});
			}))
		return "O won";

	auto rc = [&board](int r, int c, char x) -> bool {
		return !(board[r][c] == x || board[r][c] == 'T');
	};

	auto rd = [&](char x) -> bool {
		for (int i = 0; i < 4; ++i) {
			if (rc(i, i, x)) {
				return false;
			}
		}
		return true;
	};

	if (rd('X'))
		return "X won";

	if (rd('O'))
		return "O won";

	auto ur = [&](char x) -> bool {
		for (int i = 0; i < 4; ++i) {
			if (rc(3 - i, i, x)) {
				return false;
			}
		}
		return true;
	};

	if (ur('X'))
		return "X won";
	if (ur('O'))
		return "O won";

	auto any_of_a_column = [&](int c, char x) -> bool {
		for (int i = 0; i < 4; ++i) {
			if (rc(i, c, x)) {
				return false;
			}
		}
		return true;
	};

	auto any_of_column = [&](char x)->bool {
		for (int c = 0; c < 4; ++c) {
			if (any_of_a_column(c, x)) {
				return true;
			}
		}
		return false;
	};

	if (any_of_column('X'))
		return "X won";

	if (any_of_column('O'))
		return "O won";

	if (all_of(board.begin(), board.end(), [](const string &row) {
		return none_of(row.begin(), row.end(), [](char c) {return c=='.';});
	}))
		return "Draw";

	return "Game has not completed";
}

void solve(istream &in, ostream &out) {
	int T;
	in >> T;

	for (int t = 1; t <= T; ++t) {
		vector<string> board(4);
		for (int i = 0; i < 4; ++i)
			in >> board[i];

		out << "Case #" << t << ": " << whoWon(board) << endl;
	}
}

int main() {
  solve(cin, cout);
  return 0;
}
