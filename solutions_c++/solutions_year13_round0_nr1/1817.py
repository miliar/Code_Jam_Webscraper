#include <iostream>
#include <string>

using namespace std;

string a[4];
bool x,o;

bool draw() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (a[i][j] == '.')
				return false;
		}
	}
	return true;
}

bool checkrow(int i, char c) {
	for (int j = 0; j < 4; j++) {
		if (!(a[i][j] == c || a[i][j] == 'T'))
			return false;
	}
	return true;
}

bool checkcol(int j, char c) {
	for (int i = 0; i < 4; i++) {
		if (!(a[i][j] == c || a[i][j] == 'T'))
			return false;
	}
	return true;
}

bool checkd1(char c) {
	for (int i = 0; i < 4; i++) {
		if (!(a[i][i] == c || a[i][i] == 'T'))
			return false;
	}
	return true;
}

bool checkd2(char c) {
	for (int i = 0; i < 4; i++) {
		if (!(a[i][3-i] == c || a[i][3-i] == 'T'))
			return false;
	}
	return true;
}

int main() {
	int cases;
	cin >> cases;
	getline(cin,a[0]);
	for (int caseno = 1; caseno <= cases; caseno ++) {
		x = false;
		o = false;
		cout << "Case #" << caseno << ": ";
		for (int i = 0; i < 4; i++)
			getline(cin, a[i]);
		for (int i = 0; i < 4 && !x && !o; i++) {
			x = checkrow(i,'X');
			o = checkrow(i,'O');
		}
		for (int i = 0; i < 4 && !x && !o; i++) {
			x = checkcol(i,'X');
			o = checkcol(i,'O');
		}
		for (int i = 0; i < 4 && !x && !o; i++) {
			x = checkd1('X');
			o = checkd1('O');
		}
		for (int i = 0; i < 4 && !x && !o; i++) {
			x = checkd2('X');
			o = checkd2('O');
		}
		if (x) {
			cout << "X won" << endl;
		} else if (o) {
			cout << "O won" << endl;
		} else if (draw()) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
		getline(cin,a[0]);
	}
}