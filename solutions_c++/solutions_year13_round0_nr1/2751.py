#include <iostream>
#include <string>
using namespace std;

struct Input {
	char x[4][4];
	bool hasT, full;
	int tr, tc;
	string solve();
	bool won(char player);
	void prep() {
		full = true;
		hasT = false;
		int r,c;
		for (r=0;r<4;r++) {
			for (c=0;c<4;c++) {
				if (x[r][c] == 'T') {
					hasT = true;
					tr = r;
					tc = c;
				}
				if (x[r][c] == '.') {
					full = false;
				}
			}
		}
	}
	void print() {
		int r,c;
		for (r=0;r<4;r++) {
			for (c=0;c<4;c++) {
				cout << x[r][c];
			}
			cout << endl;
		}
	}	
  static Input read() {
		Input input;
		string line;
		for (int i = 0; i < 4; i++) {
			getline(cin, line);
			strncpy(input.x[i], line.c_str(), 4);
		}
		getline(cin, line);
		input.prep();
//		input.print();
		return input;
	}
};

bool Input::won(char player) {
	if (hasT)
		x[tr][tc] = player;

	int r,c;
	// row
	for (r=0; r<4;r++) {
		for (c=0; c<4;c++) {
			if (x[r][c] != player)
				break;
		}
		if (c==4) {
			return true;
		}
	}
	// col
	for (c=0; c<4;c++) {
	  for (r=0; r<4;r++) {
			if (x[r][c] != player)
				break;
		}
		if (r==4) {
			return true;
		}
	}
	// diagonal
	for (r=0; r<4;r++) {
		if (x[r][r] != player)
			break;
	}
	if (r==4)
		return true;
	for (r=0; r<4;r++) {
		if (x[r][3-r] != player)
			break;
	}
	if (r==4)
		return true;
	return false;
}

string Input::solve() {
	if (won('X')) 
			return "X won";
	if (won('O'))
			return "O won";
	if (full)
		return "Draw";
	return "Game has not completed";
}

void solve(int t, Input input) {
	cout << "Case #" << t << ": " << input.solve() << endl;
}

int main() {
	int T;
	string line;
	cin >> T;
	getline(cin, line);
	for (int i=1; i<=T; i++) {
		solve(i, Input::read());
	}
	return 0;
}
