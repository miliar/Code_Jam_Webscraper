#include <iostream>
#include <cstdio>
using namespace std;

const int _X = 1;
const int _O = 2;
char field [4][4];
char* res[4] = {"X won", "O won", "Draw", "Game has not completed"};
int test_case;

void read() {
    for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> field[i][j];
}

int check_col(int i) {
	int first = -1;
	for (int j = 0; j < 4; ++j)
		if (field[j][i] != 'T') {
			first = j;
			break;
		}

	for (int j = 0; j < 4; ++j)
		if (field[j][i] == '.' || field[j][i] != 'T' && field[first][i] != field[j][i])
			return 0;
	if (field[first][i] == 'X')
		return _X;
	return _O;
}

int check_slash_diag() {
	int first = -1;
	for (int i = 0; i < 4; ++i)
		if (field[i][i] != 'T') {
			first = i;
			break;
		}

	for (int i = 0; i < 4; ++i)
		if (field[i][i] == '.' || field[i][i] != 'T' && field[i][i] != field[first][first])
			return 0;
	if (field[first][first] == 'X')
		return _X;
	return _O;
}

int check_backslash_diag() {
	int first = -1;
	for (int i = 0; i < 4; ++i)
		if (field[i][3 - i] != 'T') {
			first = i;
			break;
		}

	for (int i = 0; i < 4; ++i)
		if (field[i][3 - i] == '.' || field[i][3 - i] != 'T' && field[i][3 - i] != field[first][3 - first])
			return 0;
	if (field[first][3 - first] == 'X')
		return _X;
	return _O;
}

int check_diag() {
	int tmp = check_slash_diag();
	if (tmp)
		return tmp;
	tmp = check_backslash_diag();
	if (tmp)
		return tmp;
}


int check_cols() {
	int tmp;
    for (int i = 0; i < 4; ++i)
	{
		tmp = check_col(i);
		if (tmp)
			return tmp;
	}
	return 0;
}

int check_row(int i) {
	int first = -1;
	for (int j = 0; j < 4; ++j)
		if (field[i][j] != 'T') {
			first = j;
			break;
		}

	for (int j = 0; j < 4; ++j)
		if (field[i][j] == '.' || field[i][j] != 'T' && field[i][first] != field[i][j])
			return 0;
	if (field[i][first] == 'X')
		return _X;
	return _O;
}

int check_rows() {
	int tmp;
    for (int i = 0; i < 4; ++i)
	{
		tmp = check_row(i);
		if (tmp)
			return tmp;
	}
	return 0;
}

int check() {
	int tmp;
	tmp = check_cols();
	if (tmp)
		if (tmp == _X)
			return 0;
		else
			return 1;
	
	tmp = check_rows();
	if (tmp)
		if (tmp == _X)
			return 0;
		else
			return 1;

	tmp = check_diag();
	if (tmp)
		if (tmp == _X)
			return 0;
		else
			return 1;


	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (field[i][j] == '.')
				return 3;
	return 2;
}

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int N;
	cin >> N;

	for (test_case = 1; test_case <= N; ++test_case) {
		read();
		int ans = check();
		printf("Case #%d: %s\n", test_case, res[ans]);
	}

	return 0;
}