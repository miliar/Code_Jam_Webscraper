#include <stdio.h>
#include <string.h>

char input[][200] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
char output[][200] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
};

int main() {
	char map[200];
	for (char c = 'a'; c <= 'z'; c++) {
		map[c] = '*';
	}
	map['q'] = 'z';
	map['z'] = 'q';
	for (int i = 0; i < 3; i ++) {
		for (int j = 0; input[i][j]; j++) {
			char c = input[i][j];
			char d = output[i][j];
			map[c] = d;
		}
	}
	for (char c = 'a'; c <= 'z'; c++) {
		printf("%c->%c\n", c, map[c]);
	}

	int tc;
	char line[200];
	scanf("%d\n", &tc);
	for (int t = 1; t <= tc; t++) {
		gets(line);
		printf("Case #%d: ", t);
		for (int i = 0; line[i]; i++) {
			if (line[i] >= 'a' && line[i] <='z') {
				printf("%c", map[line[i]]);
			} else {
				printf("%c", line[i]);
			}
		}
		printf("\n");
	}
	return 0;
}
