#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> Vc;
typedef vector<Vc > Mc;

void printWinner(int ca, char player) {
	cout << "Case #"<< ca << ": " << player << " won" << endl;
}

void checkWin(Mc &m, int ca, bool uncomplete) {
	for(int i = 0; i < 4; ++i) {
		if(m[i][0] != '.') {
			char player = m[i][0];
			bool end = false;
			for(int j = 1; j < 4 and not end; ++j) {
				if(m[i][j] != player and player == 'T') player = m[i][j];
				else if(m[i][j] != player and m[i][j] != 'T') end = true;
			}
			if(not end) {
				printWinner(ca,player);
				return;
			}
		}
	}
	for(int i = 0; i < 4; ++i) {
		if(m[0][i] != '.') {
			char player = m[0][i];
			bool end = false;
			for(int j = 1; j < 4 and not end; ++j) {
				if(m[j][i] != player and player == 'T') player = m[j][i];
				else if(m[j][i] != player and m[j][i] != 'T') end = true;
			}
			if(not end) {
				printWinner(ca,player);
				return;
			}
		}
	}
	char player = m[0][0];
	if(player != '.') {
		bool end = false;
		for(int i = 1; i < 4;++i) {
			if(m[i][i] != player and player == 'T') player = m[i][i];
			else if(m[i][i] != player and m[i][i] != 'T') end = true;
		}
		if(not end) {
			printWinner(ca,player);
			return;
		}
	}
	player = m[0][3];
	if(player != '.') {
		bool end = false;
		for(int i = 1; i < 4;++i) {
			if(m[i][3-i] != player and player == 'T') player = m[i][3-i];
			else if(m[i][3-i] != player and m[i][3-i] != 'T') end = true;
		}
		if(not end) {
			printWinner(ca,player);
			return;
		}
	}
	if(uncomplete) {
		cout << "Case #" << ca << ": Game has not completed" << endl;
	} else {
		cout << "Case #" << ca << ": Draw" << endl;
	}
}

int main() {
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i) {
		Mc m(4,Vc(4));
		bool uncomplete = false;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				cin >> m[j][k];
				if(m[j][k] == '.') uncomplete = true;
			}
		}
		checkWin(m,i+1,uncomplete);
	}
}