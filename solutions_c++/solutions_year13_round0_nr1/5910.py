#include <cstdio>
using namespace std;

int T;
char c;
char s[4][4];

bool win(char c) {
	int i, j;
	for (i = 0; i < 4; ++i) {
		for (j = 0; j < 4; ++j) {
			if (s[i][j] != c && s[i][j] != 'T') break;
		}
		if (j == 4) return true;
	}
	for (j = 0; j < 4; ++j) {
		for (i = 0; i < 4; ++i) {
			if (s[i][j] != c && s[i][j] != 'T') break;
		}
		if (i == 4) return true;
	}
	for (i = 0; i < 4; ++i) {
		if (s[i][i] != c && s[i][j] != 'T') break;
	}
	if (i == 4) return true;
	for (i = 0; i < 4; ++i) {
		if (s[i][3-i] != c && s[i][3-i] != 'T') break;
	}
	if (i == 4) return true;
	return false;
}

bool notcom() {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (s[i][j] == '.') return true;
		}
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ) {
				c = fgetc(stdin);
				if (c == 'X' || c == 'O' || c == '.' || c == 'T') {
					s[i][j++] = c;
				}
			}
		}
		if (win('X')) printf("Case #%d: X won\n", tc);
		else if (win('O')) printf("Case #%d: O won\n", tc);
		else if (notcom()) printf("Case #%d: Game has not completed\n", tc);
		else printf("Case #%d: Draw\n", tc);
	}
	return 0;
}
