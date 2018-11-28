#include <cstdio>

int lines[10][4] = {
	{0, 1, 2, 3},
	{4, 5, 6, 7},
	{8, 9, 10, 11},
	{12, 13, 14, 15},
	{0, 4, 8, 12},
	{1, 5, 9, 13},
	{2, 6, 10, 14},
	{3, 7, 11, 15},
	{0, 5, 10, 15},
	{3, 6, 9, 12}
};

int T, t;
char s[17];
bool f;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		for (int i = 0; i < 4; ++i)
			scanf("%s", s + 4*i);
		printf("Case #%d: ", r);
		f = 0;
		for (int i = 0; i < 10 && !f; ++i) {
			f = 1;
			for (int j = 0; j < 4; ++j) {
				t = lines[i][j];
				if (s[t] == 'X' || s[t] == '.')
					f = 0;
			}
		}
		if (f) {
			puts("O won");
			continue;
		}
		for (int i = 0; i < 10 && !f; ++i) {
			f = 1;
			for (int j = 0; j < 4; ++j) {
				t = lines[i][j];
				if (s[t] == 'O' || s[t] == '.')
					f = 0;
			}
		}
		if (f) {
			puts("X won");
			continue;
		}
		for (int i = 0; i < 16; ++i)
			if (s[i] == '.')
				f = 1;
		if (f)
			puts("Game has not completed");
		else
			puts("Draw");
	}
	return 0;
}
