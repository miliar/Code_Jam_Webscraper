#include <stdio.h>
#include <string.h>

char s[5][5];

int main() {
	int T;
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		int dot = 0;
		for (int i = 0; i < 4; i++) {
			scanf("%s", s[i]);
			for (int j = 0; j < 4; j++)
				if (s[i][j] == '.')
					dot = 1;
		}
		int flag = 0;
		for (int i = 0; i < 4; i++) {
			int a = 0, b = 0;
			for (int j = 0; j < 4; j++) {
				if (s[i][j] == 'X' || s[i][j] == 'T') {
					a++;
				} 
				if (s[i][j] == 'O' || s[i][j] == 'T') {
					b++;
				}
			}
			if (a == 4)
				flag = 1;
			if (b == 4)
				flag = -1;
		}
		for (int i = 0; i < 4; i++) {
			int a = 0, b = 0;
			for (int j = 0; j < 4; j++) {
				if (s[j][i] == 'X' || s[j][i] == 'T') {
					a++;
				} 
				if (s[j][i] == 'O' || s[j][i] == 'T') {
					b++;
				}
			}
			if (a == 4)
				flag = 1;
			if (b == 4)
				flag = -1;
		}
		int a = 0, b = 0;
		for (int i = 0; i < 4; i++) {
			int j = i;
			if (s[j][i] == 'X' || s[j][i] == 'T') {
				a++;
			}
			if (s[j][i] == 'O' || s[j][i] == 'T') {
				b++;
			}
		}
		if (a == 4)
			flag = 1;
		if (b == 4)
			flag = -1;
		a = 0;
		b = 0;
		for (int i = 0; i < 4; i++) {
			int j = 3 - i;
			if (s[j][i] == 'X' || s[j][i] == 'T') {
				a++;
			}
			if (s[j][i] == 'O' || s[j][i] == 'T') {
				b++;
			}
		}
		if (a == 4)
			flag = 1;
		if (b == 4)
			flag = -1;
		if (flag == 1) {
			printf("Case #%d: X won\n", re);
		} else if (flag == -1) {
			printf("Case #%d: O won\n", re);
		} else {
			if (dot == 0) {
				printf("Case #%d: Draw\n", re);
			} else {
				printf("Case #%d: Game has not completed\n", re);
			}
		}
	}
}
