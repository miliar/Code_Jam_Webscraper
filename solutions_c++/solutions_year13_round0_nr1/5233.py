#include <iostream>
#include <string>
#include <vector>

using std::vector;

int main() {
	std::istream &in = std::cin;
	std::ostream &out = std::cout;

	int t = 0;
	in >> t;

	int ST = 'T' - '.',
	    SX = 'X' - '.',
		SO = 'O' - '.';

	int mat[4][4];
	
	for (int _ = 0; _ < t; ++_) {
		bool end = true;
		for (size_t i = 0; i < 4; ++i) {
			for (size_t j = 0; j < 4; ++j) {
				char ch;
				in >> ch;
				if (ch == '.') end = false;
				mat[i][j] = ch - '.';
			}
		}

		bool first_won = false,
		     second_won = false;

		for (size_t i = 0; i < 4; ++i) {
			int no_x = 0,
			    no_o = 0,
			    no_t = 0;
			for (size_t j = 0; j < 4; ++j) {
				if (mat[i][j] == ST) ++no_t;
				if (mat[i][j] == SO) ++no_o;
				if (mat[i][j] == SX) ++no_x;
			}

			if (no_x == 4 || no_x == 3 && no_t == 1) {
				first_won = true;
				break;
			} else if (no_o == 4 || no_o == 3 && no_t == 1) {
				second_won = true;
				break;
			}
		}

		for (size_t i = 0; i < 4; ++i) {
			int no_x = 0,
			    no_o = 0,
			    no_t = 0;
			for (size_t j = 0; j < 4; ++j) {
				if (mat[j][i] == ST) ++no_t;
				if (mat[j][i] == SO) ++no_o;
				if (mat[j][i] == SX) ++no_x;
			}

			if (no_x == 4 || no_x == 3 && no_t == 1) {
				first_won = true;
				break;
			} else if (no_o == 4 || no_o == 3 && no_t == 1) {
				second_won = true;
				break;
			}
		}

		{
			int no_x = 0,
			    no_o = 0,
			    no_t = 0;
			for (size_t i = 0; i < 4; ++i) {
				if (mat[i][i] == ST) ++no_t;
				if (mat[i][i] == SO) ++no_o;
				if (mat[i][i] == SX) ++no_x;
			}

			if (no_x == 4 || no_x == 3 && no_t == 1) {
				first_won = true;
			} else if (no_o == 4 || no_o == 3 && no_t == 1) {
				second_won = true;
			}
		}

		{
			int no_x = 0,
			    no_o = 0,
			    no_t = 0;
			for (size_t i = 0; i < 4; ++i) {
				if (mat[i][3-i] == ST) ++no_t;
				if (mat[i][3-i] == SO) ++no_o;
				if (mat[i][3-i] == SX) ++no_x;
			}

			if (no_x == 4 || no_x == 3 && no_t == 1) {
				first_won = true;
			} else if (no_o == 4 || no_o == 3 && no_t == 1) {
				second_won = true;
			}
		}

		out << "Case #" << (_+1) << ": ";
		if (first_won) {
			out << "X won";
		}

		if (second_won) {
			out << "O won";
		}

		if (!first_won && !second_won) {
			out << (end ? "Draw" : "Game has not completed");
		}
		out << "\n";
	}
	return 0;
}
