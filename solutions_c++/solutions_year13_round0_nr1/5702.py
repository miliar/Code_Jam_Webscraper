#include<cstdio>
#define MAXN 4
char str[MAXN][MAXN];
bool draw() {
	int i, j;
	for (i = 0; i < MAXN; i++) {
		for (j = 0; j < MAXN; j++) {
			if (str[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}
bool won(char ch) {
	int i, j;
	int a, b;
	for (i = 0; i < MAXN; i++) {
		a = b = 0;
		for (j = 0; j < MAXN; j++) {
			if (str[i][j] == ch) {
				a++;
			} else if (str[i][j] != 'T'
					&& str[i][j]
							!= '.') {
				b++;
			}
		}
		if (a >= 3 && b == 0) {
			return true;
		}
	}
	for (i = 0; i < MAXN; i++) {
		a = b = 0;
		for (j = 0; j < MAXN; j++) {
			if (str[j][i] == ch) {
				a++;
			} else if (str[j][i] != 'T'
					&& str[j][i]
							!= '.') {
				b++;
			}
		}
		if (a >= 3 && b == 0) {
			return true;
		}
	}
	a = b = 0;
	for (i = j = 0; i < MAXN; i++, j++) {
		if (str[i][i] == ch) {
			a++;
		} else if (str[i][j] != 'T' && str[i][j] != '.') {
			b++;
		}
	}
	if (a >= 3 && b == 0) {
		return true;
	}
	a = b = 0;
	for (i = 0, j = MAXN - 1; i < MAXN; i++, j--) {
		if (str[i][j] == ch) {
			a++;
		} else if (str[i][j] != 'T' && str[i][j] != '.') {
			b++;
		}
	}
	if (a >= 3 && b == 0) {
		return true;
	}
	return false;
}
int main() {
	int T, ca = 1;
	int i, j;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	while (T--) {
		for (i = 0; i < MAXN; i++) {
			for (j = 0; j < MAXN; j++) {
				scanf(" %c", &str[i][j]);
			}
		}
		printf("Case #%d: ", ca++);
		if (won('X')) {
			puts("X won");
		} else if (won('O')) {
			puts("O won");
		} else if (draw()) {
			puts("Draw");
		} else {
			puts("Game has not completed");
		}
	}
	return 0;
}
