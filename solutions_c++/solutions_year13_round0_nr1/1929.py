#include <iostream>
#include <vector>

using namespace std;

typedef vector<char> vc;
typedef vector<vc> vcc;

bool won(vcc &tab, int i, int j, char c) {
	//horizontal
	if (j == 0) {
		if (tab[i][j+1] == c && tab[i][j+2] == c && tab[i][j+3] == c) return true;
	}
	//vertical
	if (i == 0) {
		if (tab[i+1][j] == c && tab[i+2][j] == c && tab[i+3][j] == c) return true;
	}
	//diagonal 1
	if (i == 0 && j == 0) {
		if (tab[i+1][j+1] == c && tab[i+2][j+2] == c && tab[i+3][j+3] == c) return true;
	}
	//diagonal 2
	if (i == 0 && j == 3) {
		if (tab[i+1][j-1] == c && tab[i+2][j-2] == c && tab[i+3][j-3] == c) return true;
	}

	return false;
}

void check(vcc &tab, bool &xwon, bool &owon, bool &complete) {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			char c = tab[i][j];
			if (c == '.') complete = false;
			else if (c == 'X') {
				xwon = xwon ? : won(tab, i, j, 'X');
			} else if (c == 'O') {
				owon = owon ? : won(tab, i, j, 'O');
			}
		}
	}
}

int main() {
	int t;
	cin >> t;

	for (int tt = 0; tt < t; ++tt) {
		vcc tab(4, vc(4));
		vcc tab2(4, vc(4));
		for (int i = 0; i < 4; ++i)	{
			for (int j = 0; j < 4; ++j) {
				char c;
				cin >> c;
				if (c == 'T') {
					tab[i][j] = 'X';
					tab2[i][j] = 'O';
				} else {
					tab[i][j] = tab2[i][j] = c;
				}
			}
		}
		bool xwon = false;
		bool owon = false;
		bool complete = true;

		cout << "Case #" << tt+1 << ": "; 

		check(tab, xwon, owon, complete);
		check(tab2, xwon, owon, complete);
		
		if (xwon) cout << "X won";
		else if (owon) cout << "O won";
		else if (complete) cout << "Draw";
		else cout << "Game has not completed";
		cout << endl;
	}
}