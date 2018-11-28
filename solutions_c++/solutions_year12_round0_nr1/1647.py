#include <stdio.h>
#include <string.h>
int mapping[26];
char s[1024];
char org[3][1024] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char tra[3][1024] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

void preprocess() {
	int i, j;
	memset(mapping, -1, sizeof(mapping));
	for (i=0;i<3;++i) {
		for (j=0;org[i][j];++j) {
			if (org[i][j] != ' ') {
				mapping[org[i][j]-'a'] = tra[i][j] - 'a';
			}
		}
	}
	mapping['q' - 'a'] = 'z' - 'a';
	mapping['z' - 'a'] = 'q' - 'a';
}

int main() {
	preprocess();
	int t, i, j, ca = 0;
	char s[1024];
	scanf("%d", &t);
	gets(s);
	while (t--) {
		gets(s);
		printf("Case #%d: ", ++ca);
		for (i=0;s[i];++i) {
			if (s[i] == ' ') printf(" ");
			else printf("%c", mapping[s[i]-'a']+ 'a');
		}
		puts("");
	}
	return 0;
}