#include <stdio.h>
#include <ctype.h>

char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
bool flag[26] = {0};

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i, j, cas = 0;
	char str[128];
	scanf("%d\n", &T);

	while (T--) {
		printf("Case #%d: ", ++cas);
		gets(str);
		for (i = 0; str[i]; ++i) {
			if (islower(str[i]))
				str[i] = map[str[i] - 'a'];
		}
		puts(str);
	}

	/*char str[2][3][128];
	for (i = 0; i < T; ++i) {
		gets(str[0][i]);
	}
	for (i = 0; i < T; ++i) {
		gets(str[1][i]);
		for (j = 0; str[0][i][j]; ++j) {
			if (islower(str[0][i][j]))
				map[str[0][i][j] - 'a'] = str[1][i][j + 9];
		}
	}
	map['y' - 'a'] = 'a';
	map['e' - 'a'] = 'o';
	map['q' - 'a'] = 'z';
	for (i = 0; i < 26; ++i) {
		if (!map[i]) {
			printf("%c\n", i + 'a');
			j = i;
		}
		if (islower(map[i])) 
			flag[map[i] - 'a'] = true;
		//putchar(map[i]);
	}
	for (i = 0; i < 26; ++i) {
		if (!flag[i]) {
			map[j] = i + 'a';
			putchar(i + 'a');
		}
	}
	puts("");
	for (i = 0; i < 26; ++i) {
		putchar(map[i]);
	}
	puts("");*/
	return 0;
}