#include <iostream>
#include <string>

using namespace std;

char board[4][4];
std::string blah; // for the empty line

void read_board() {
	std::string line;
	for (int i=0; i<4; ++i) {
		cin >> line;
		for (int j=0; j<4; ++j) {
			board[i][j] = line[j];
		}
	}
}

void print_board() {
	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			cout << board[i][j];
		}
                cout << "\n";
	}

}

void eval_board(int sample) {
	// check rows
	for (int i=0; i<4; ++i) {
		bool xwon = true;
		bool owon = true;
		for (int j=0; j<4; ++j) {
			if (board[i][j] == 'X') {
				owon = false;
			} else if (board[i][j] == 'O') {
				xwon = false;
			} else if (board[i][j] == '.') {
				xwon=false;
				owon=false;
			}
		}
		if (xwon) {
			cout<<"Case #"<<sample<<": X won\n";
			return;
		}
		if (owon) {
			cout<<"Case #"<<sample<<": O won\n";
			return;
		}
	}
	// check columns
	for (int i=0; i<4; ++i) {
		bool xwon = true;
		bool owon = true;
		for (int j=0; j<4; ++j) {
			if (board[j][i] == 'X') {
				owon = false;
			} else if (board[j][i] == 'O') {
				xwon = false;
			} else if (board[j][i] == '.') {
				xwon=false;
				owon=false;
			}
		}
		if (xwon) {
			cout<<"Case #"<<sample<<": X won\n";
			return;
		}
		if (owon) {
			cout<<"Case #"<<sample<<": O won\n";
			return;
		}
	}

	// check diag1
	bool xwon = true;
	bool owon = true;
	for (int i=0; i<4; ++i) {
		if (board[i][i] == 'X') {
			owon = false;
		} else if (board[i][i] == 'O') {
			xwon = false;
		} else if (board[i][i] == '.') {
			xwon=false;
			owon=false;
		}
	}
	if (xwon) {
		cout<<"Case #"<<sample<<": X won\n";
		return;
	}
	if (owon) {
		cout<<"Case #"<<sample<<": O won\n";
		return;
	}

	// check diag2
	xwon = true;
	owon = true;
	for (int i=0; i<4; ++i) {
		if (board[i][3-i] == 'X') {
			owon = false;
		} else if (board[i][3-i] == 'O') {
			xwon = false;
		} else if (board[i][3-i] == '.') {
			xwon=false;
			owon=false;
		}
	}
	if (xwon) {
		cout<<"Case #"<<sample<<": X won\n";
		return;
	}
	if (owon) {
		cout<<"Case #"<<sample<<": O won\n";
		return;
	}

	// check end
	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			if (board[i][j] == '.') {
				cout << "Case #"<<sample<<": Game has not completed\n";
				return;
			}
		}
	}

	cout << "Case #"<<sample<<": Draw\n";

}

int main() {
	int N;
	cin >> N;

	for (int sample=0; sample < N; ++sample) {
		read_board();
		eval_board(sample+1);
	}
}


