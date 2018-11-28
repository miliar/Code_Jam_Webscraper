#include <iostream>
#include <string>
using namespace std;

int case_number;
char board[16];
int case_result;
const string res[4] = {"X won", "O won", "Draw", "Game has not completed"};

bool row(char c, int i) {
	int c_count, t_count;
	c_count = t_count = 0;
	for (int j = i*4; j < (i+1)*4; j++) {
		if (board[j] == c) c_count++;
		if (board[j] == 'T') t_count++;
	}
	return (c_count == 4) || (c_count == 3 && t_count == 1);
}

bool col(char c, int i) {
	int c_count, t_count;
	c_count = t_count = 0;
	for (int j = i; j < 16; j+=4) {
		if (board[j] == c) c_count++;
		if (board[j] == 'T') t_count++;
	}
	return (c_count == 4) || (c_count == 3 && t_count == 1);
}

bool dia(char c, bool anti) {
	int c_count, t_count;
	c_count = t_count = 0;
	int k;
	for (int j = 0; j < 4; j++) {
		k = anti?(3-j):j;
		if (board[k+4*j] == c) c_count++;
		if (board[k+4*j] == 'T') t_count++;
	}
	return (c_count == 4) || (c_count == 3 && t_count == 1);
}

bool won(char c) {
	return row(c, 0)||row(c, 1)||row(c, 2)||row(c, 3)
		|| col(c, 0)||col(c, 1)||col(c, 2)||col(c, 3)
		|| dia(c, false) || dia(c, true);
}

bool x_won() {
	return won('X');
}

bool o_won() {
	return won('O');
}

bool complete() {
	for (int i = 0; i < 16; i++) {
		if (board[i] == '.') return false;	
	}
	return true;
}

void print() {
	cout << "Case #" << (case_number+1) << ": " << res[case_result] << endl;
}

void read() {
	for (int i = 0; i < 16; i++) {
		cin >> board[i];	
	}
}

void solve() {
	case_result = -1;
	if (x_won()) {
		case_result = 0;
		return;
	}
	if (o_won()) {
		case_result = 1;
		return;
	}
	if (complete()) {
		case_result = 2;
		return;
	}
	case_result = 3;
}

void main() {
	int n;
	cin >> n;
	for (case_number = 0; case_number < n; case_number++) {
		read();
		solve();
		print();
	}
}