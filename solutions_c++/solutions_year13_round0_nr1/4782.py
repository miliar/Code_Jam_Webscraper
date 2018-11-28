#include <stdio.h>

char mat[4][5];

bool gao(char c) {
	int i, j;
	// row
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (mat[i][j] != c && mat[i][j] != 'T')
				break;
		}
		if (j == 4)
			return true;
	}
	// column
	for (j = 0; j < 4; j++) {
		for (i = 0; i < 4; i++) {
			if (mat[i][j] != c && mat[i][j] != 'T')
				break;
		}
		if (i == 4)
			return true;
	}
	// diagonal
	for (i = 0; i < 4; i++) {
		if (mat[i][i] != c && mat[i][i] != 'T')
			break;
	}
	if (i == 4)
		return true;
	for (i = 0; i < 4; i++) {
		if (mat[i][3 - i] != c && mat[i][3 - i] != 'T')
			break;
	}
	if (i == 4)
		return true;
	// false
	return false;
}

bool full() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (mat[i][j] == '.')
				return false;
		}
	}
	return true;
}

int gao() {
	if (gao('X'))
		return 1;
	else if (gao('O'))
		return 2;
	else if (full())
		return 3;
	else 
		return 4;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int  T; scanf("%d", &T);
	int index = 1;
	while (T--) {
		for (int i = 0; i < 4; i++)
			scanf("%s", mat[i]);
		int status = gao();
		if (status == 1)
			printf("Case #%d: X won\n", index++);
		else if (status == 2)
			printf("Case #%d: O won\n", index++);
		else if (status == 3)
			printf("Case #%d: Draw\n", index++);
		else 
			printf("Case #%d: Game has not completed\n", index++);
	}
	return 0;
}