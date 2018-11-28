#include<stdio.h>
char s[5][5];
bool OO(char c) {
	if (c == 'O' || c == 'T')
		return true;
	return false;
}
bool XX(char c) {
	if (c == 'X' || c == 'T')
		return true;
	return false;
}
int main() {
	int T, cas = 0;
	int o, x, p, i, j;
	scanf("%d", &T);
	while (T--) {
		cas++;
		p = 1;
		for (i = 0; i < 4; ++i) {
			scanf("%s", s[i]);
			for (j = 0; j < 4; ++j)
				if (s[i][j] == '.')
					p = 0;
		}
		o = x = 0;
		for (i = 0; i < 4; ++i) {
			if (OO(s[i][0]) && OO(s[i][1]) && OO(s[i][2]) && OO(s[i][3]))
				o = 1;
			if (XX(s[i][0]) && XX(s[i][1]) && XX(s[i][2]) && XX(s[i][3]))
				x = 1;
			if (OO(s[0][i]) && OO(s[1][i]) && OO(s[2][i]) && OO(s[3][i]))
				o = 1;
			if (XX(s[0][i]) && XX(s[1][i]) && XX(s[2][i]) && XX(s[3][i]))
				x = 1;
		}
		if (OO(s[0][0]) && OO(s[1][1]) && OO(s[2][2]) && OO(s[3][3]))
			o = 1;
		if (XX(s[0][0]) && XX(s[1][1]) && XX(s[2][2]) && XX(s[3][3]))
			x = 1;
		if (OO(s[3][0]) && OO(s[2][1]) && OO(s[1][2]) && OO(s[0][3]))
			o = 1;
		if (XX(s[3][0]) && XX(s[2][1]) && XX(s[1][2]) && XX(s[0][3]))
			x = 1;
		printf("Case #%d: ", cas);
		if (x == o && p == 0)
			printf("Game has not completed\n");
		else if (x == o)
			printf("Draw\n");
		else if (x)
			printf("X won\n");
		else if (o)
			printf("O won\n");
	}
}
