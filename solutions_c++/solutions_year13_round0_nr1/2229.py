#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;


char board[4][4];
ofstream out("out.txt");
void checkwin(int n) {
	bool hasempty = false;
	for (int i = 0; i < 4; i++) {
		bool failx = false, failo = false;
		for (int j = 0; j < 4; j++) {
			if (board [i][j] == '.') {
				hasempty = true;
				failo = failx = true;
			}
			if (board[i][j] == 'X') {
				failo = true;

			}
			if (board[i][j] == 'O') {
				failx = true;

			}
			if (failo and failx) break;
		}
		if (!failo) {
			out << "Case #"<<n<<": O won" << endl;
			return;
		}
		if (!failx) {
			out << "Case #"<<n<<": X won" << endl;
			return;
		}

	}

	for (int j = 0; j < 4; j++) {
		bool failx = false, failo = false;
		for (int i = 0; i < 4; i++) {
			if (board [i][j] == '.') {
				hasempty = true;
				failo = failx = true;
			}
			if (board[i][j] == 'X') {
				failo = true;

			}
			if (board[i][j] == 'O') {
				failx = true;

			}
			if (failo and failx) break;
		}
		if (!failo) {
			out << "Case #"<<n<<": O won" << endl;
			return;
		}
		if (!failx) {
			out << "Case #"<<n<<": X won" << endl;
			return;
		}

	}


	bool failx = false, failo = false;
	for (int j = 0; j < 4; j++) {
		if (board [j][j] == '.') {
			hasempty = true;
			failo = failx = true;
		}
		if (board[j][j] == 'X') {
			failo = true;

		}
		if (board[j][j] == 'O') {
			failx = true;

		}
		if (failo and failx) break;
	}
	if (!failo) {
		out << "Case #"<<n<<": O won" << endl;
		return;
	}
	if (!failx) {
		out << "Case #"<<n<<": X won" << endl;
		return;
	}


	failx = false, failo = false;
	for (int j = 0; j < 4; j++) {
		if (board [j][3-j] == '.') {
			hasempty = true;
			failo = failx = true;
		}
		if (board[j][3-j] == 'X') {
			failo = true;

		}
		if (board[j][3-j] == 'O') {
			failx = true;

		}
		if (failo and failx) break;
	}
	if (!failo) {
		out << "Case #"<<n<<": O won" << endl;
		return;
	}
	if (!failx) {
		out << "Case #"<<n<<": X won" << endl;
		return;
	}

	if (!hasempty) {
		out << "Case #"<<n<<": Draw" << endl;
		return;
	}

	out << "Case #"<<n<<": Game has not completed" << endl;

}

int main () {

	ifstream f("A-small-attempt2.in");

	int n, moves = 0;
	f >> n;
	for (int x = 0; x < n; x++) {
		moves = 0;
		for (int i = 0; i < 4 ; i ++ ) {
			for (int j = 0; j < 4; j ++) {
				char in;
				f >> in;
				board[i][j] = in;
			}
		}

		checkwin(x+1);
	}

	return 0;

}
