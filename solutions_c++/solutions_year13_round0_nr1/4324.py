#include <iostream>
#include <string>

using namespace std;

enum State {
	X_WON,
	O_WON,
	DRAW,
	IN_PROGRESS
};

void setNext(char& c, char n) {
	if(c == 'T' || n == '.') c = n;
	else if(c != '.' && n != c && n != 'T') c = '/';
}

#define checkRet(c) do { \
	if(c == 'X') return X_WON; \
	if(c == 'O') return O_WON; } while(0)

State nextStateCase() {
	string line[4];
	getline(cin, line[0]);
	char ycurr[4] = {'T', 'T', 'T', 'T'}, da = 'T', db = 'T';
	for(int y = 0; y < 4; ++y) {
		getline(cin, line[y]);
		for(int x = 0; x < 4; ++x) setNext(ycurr[x], line[y][x]);
		setNext(da, line[y][y]);
		setNext(db, line[y][3 - y]);
	}

	checkRet(da);
	checkRet(db);
	for(int y = 0; y < 4; ++y) {
		char xcurr = 'T';
		for(int x = 0; x < 4; ++x) setNext(xcurr, line[y][x]);
		checkRet(xcurr);
	}

	char end = 'T';
	for(int x = 0; x < 4; ++x) {
		checkRet(ycurr[x]);
		setNext(end, ycurr[x]);
	}
	return end == '/' ? DRAW : IN_PROGRESS;
}

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		switch(nextStateCase()) {
		case X_WON: cout << "X won"; break;
		case O_WON: cout << "O won"; break;
		case DRAW: cout << "Draw"; break;
		case IN_PROGRESS: cout << "Game has not completed"; break;
		}
		cout << endl;
	}
}
