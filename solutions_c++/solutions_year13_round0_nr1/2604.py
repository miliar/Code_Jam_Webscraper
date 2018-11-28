#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> line;

bool check_inprog() {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (line[i][j] == '.')
				return true;
	return false;
}

bool check_winner(char player) {
	for (int i = 0; i < 4; i++) {
		int cntr = 0, cntc = 0;
		for (int j = 0; j < 4; j++) {
			// 1. Check each row (4)
			if (line[i][j] == 'T' || line[i][j] == player)
				cntr++;
			// 2. Check each col (4)
			if (line[j][i] == 'T' || line[j][i] == player)
				cntc++;
			}
		if (cntr == 4 || cntc == 4)
			return true;
	}
	// 3. Check each diag (2)
	int cnte = 0, cntw = 0;
	for (int i = 0; i < 4; i++) {
		if (line[i][i] == 'T' || line[i][i] == player)
				cnte++;
		if (line[i][3-i] == 'T' || line[i][3-i] == player)
				cntw++;
	}
	if (cnte == 4 || cntw == 4)
		return true;
	return false;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		line.clear();
		for (int i = 0; i < 4; i++) {
			string tmp;
			cin >> tmp;
			line.push_back(tmp);
		}
		string res = "Draw";
		if (check_winner('X'))
			res = "X won";
		else if (check_winner('O'))
			res = "O won";
		else if (check_inprog())
			res = "Game has not completed";
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
