#include <iostream>
#include <cstdio>
using namespace std;

char mmap[4][4];

char equal(char a, char b, char c, char d) {
	if (a == '.' || b == '.' || c == '.' || d == '.') return '.';
	if (a == 'X' && b != 'O' && c != 'O' && d != 'O') return 'X';
	if (a == 'O' && b != 'X' && c != 'X' && d != 'X') return 'O';
	return '.';
}

void calc() {
	char x;
	for (int i = 0; i < 4; ++ i) {
		x = equal(mmap[i][0], mmap[i][1], mmap[i][2], mmap[i][3]);
		if (x == 'X' || x == 'O') {
			printf("%c won\n", x);
			return ;
		}
		x = equal(mmap[0][i], mmap[1][i], mmap[2][i], mmap[3][i]);
		if (x == 'X' || x == 'O') {
			printf("%c won\n", x);
			return ;
		}
	}
	x = equal(mmap[0][0], mmap[1][1], mmap[2][2], mmap[3][3]);
	if (x == 'X' || x == 'O') {
		printf("%c won\n", x);
		return ;
	}

	x = equal(mmap[0][3], mmap[1][2], mmap[2][1], mmap[3][0]);
	if (x == 'X' || x == 'O') {
		printf("%c won\n", x);
		return ;
	}

	for (int i = 0; i < 4; ++ i)
		for (int j = 0; j < 4; ++ j)
			if (mmap[i][j] == '.') {
				printf("Game has not completed\n");
				return;
			}

	printf("Draw\n");
}

int main() {
	int T;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-output", "w+", stdout);
	scanf("%d", &T);
	char str[255];
	for (int i = 0; i < T; ++ i) {
		gets(str);
		for (int j = 0; j < 4; ++ j) {
			gets(str);
			for (int k = 0; k < 4; ++ k)
				mmap[j][k] = str[k];
		}

		printf("Case #%d: ", i + 1);
		calc();
	}
	return 0;
}
