#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class tictactoetomek
{
	private:
		static const int bsize = 4;

		vector<string> board;

		bool testline(int bx, int by, int dx, int dy, char player) {
			for (int m = 0; m < bsize; ++m) {
				char cc = board.at(bx + m * dx).at(by + m * dy);
				if ((cc != player) && (cc != 'T')) {
					return false;
				}
			}
			return true;
		}

		bool checkplayerwon(char player) {
			for (int f = 0; f < bsize; ++f) {
				if (testline(f, 0, 0, 1, player) || testline(0, f, 1, 0, player)) {
					return true;
				}
			}
			if (testline(0, 0, 1, 1, player) || testline(0, bsize - 1, 1, -1, player)) {
				return true;
			}
			return false;
		}

		bool findchar(char ctf) {
			for (int f = 0; f < bsize; ++f) {
				for (int g = 0; g < bsize; ++g) {
					if (board.at(f).at(g) == ctf) {
						return true;
					}
				}
			}
			return false;
		}

	public:
		void input() {
			board.resize(bsize);
			for (int f = 0; f < bsize; ++f) {
				cin >> board.at(f);
			}
		}

		string solve() {
			if (checkplayerwon('X')) {
				return "X won";
			}
			if (checkplayerwon('O')) {
				return "O won";
			}
			if (findchar('.')) {
				return "Game has not completed";
			}
			return "Draw";
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		tictactoetomek task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
