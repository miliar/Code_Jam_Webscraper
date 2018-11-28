#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

void InitFiles() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

bool Ok(char test, char c) {
	return test == 'T' || test == c;
}

bool Wins(string* field, char c) {
	for (int i = 0; i < 4; ++i) {
		if (Ok(field[i][0], c) && Ok(field[i][1], c) && Ok(field[i][2], c) && Ok(field[i][3], c)) {
			return true;
		}
		if (Ok(field[0][i], c) && Ok(field[1][i], c) && Ok(field[2][i], c) && Ok(field[3][i], c)) {
			return true;
		}
	}
	if (Ok(field[0][0], c) && Ok(field[1][1], c) && Ok(field[2][2], c) && Ok(field[3][3], c)) {
		return true;
	}
	if (Ok(field[0][3], c) && Ok(field[1][2], c) && Ok(field[2][1], c) && Ok(field[3][0], c)) {
		return true;
	}
	return false;
}

bool HasEmpty(string* field) {
	for (size_t i = 0; i < 4; ++i) {
		for (size_t j = 0; j < 4; ++j) {
			if (field[i][j] == '.') {
				return true;
			}
		}
	}
	return false;
}

string Solve() {
	string field[5];
	for (int i = 0; i < 5; ++i) {
		getline(cin, field[i], '\n');
	}
	if (Wins(field, 'X')) {
		return "X won";
	}
	if (Wins(field, 'O')) {
		return "O won";
	}
	if (HasEmpty(field)) {
		return "Game has not completed";
	}
	return "Draw";
}

int main()
{
	InitFiles();

	char buf[100];
	int t;
	gets(buf);
	t = atoi(buf);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %s\n", i + 1, Solve().c_str());
	}
	return 0;
}