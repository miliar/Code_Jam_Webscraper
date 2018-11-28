#include<iostream>
#include<vector>

using namespace std;

int check_row( const vector<string> & m ) {
	bool finished = true;
	for (int i=0; i<4; i++) {
		int sum = 0;
		for (int j=0; j<4; j++) {
			if (m[i][j] == 'X') sum += 1;
			if (m[i][j] == 'O') sum += 10;
			if (m[i][j] == 'T') sum += 100;
			if (m[i][j] == '.') finished = false;
		}
		if (sum == 4 || sum == 103) return 1;
		if (sum == 40 || sum == 130) return 10;
	}
	if (finished) {
		return 0;
	} else {
		return -1;
	}
}

int check_col( const vector<string> & m ) {
	bool finished = true;
	for (int j=0; j<4; j++) {
		int sum = 0;
		for (int i=0; i<4; i++) {
			if (m[i][j] == 'X') sum += 1;
			if (m[i][j] == 'O') sum += 10;
			if (m[i][j] == 'T') sum += 100;
			if (m[i][j] == '.') finished = false;
		}
		if (sum == 4 || sum == 103) return 1;
		if (sum == 40 || sum == 130) return 10;
	}
	if (finished) {
		return 0;
	} else {
		return -1;
	}
}

int check_diag( const vector<string> & m ) {
	bool finished = true;
	int sum=0;
	for (int i=0; i<4; i++) {
		if (m[i][i] == 'X') sum += 1;
		if (m[i][i] == 'O') sum += 10;
		if (m[i][i] == 'T') sum += 100;
		if (m[i][i] == '.') finished = false;
		if (sum == 4 || sum == 103) return 1;
		if (sum == 40 || sum == 130) return 10;
	}
	sum = 0;
	for (int i=0; i<4; i++) {
		if (m[i][3-i] == 'X') sum += 1;
		if (m[i][3-i] == 'O') sum += 10;
		if (m[i][3-i] == 'T') sum += 100;
		if (m[i][3-i] == '.') finished = false;
		if (sum == 4 || sum == 103) return 1;
		if (sum == 40 || sum == 130) return 10;
	}
	if (finished) {
		return 0;
	} else {
		return -1;
	}
}

int main() {
	int T;
	cin >> T;
	vector<string> map;
	string str;
	for (int k=0; k<T; k++) {
		map.clear();
		for (int i=0; i<4; i++) {
			cin >> str;
			map.push_back( str );
		}
		int r_res = check_row( map );
		int c_res = check_col( map );
		int d_res = check_diag( map );
		cout << "Case #" << k+1 << ": ";
		if (r_res == 0 && c_res == 0 && d_res == 0) {
			cout << "Draw" << endl;
		} else if (r_res == 1 || c_res == 1 || d_res == 1) {
			cout << "X won" << endl;
		} else if (r_res == 10 || c_res == 10 || d_res == 10) {
			cout << "O won" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	}
	return 0;
}
