#include <stdio.h>
#include <string.h>

char a[3][200] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char b[3][200] = {"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};

char m[30];

int main()
{
	for (int i = 0; i < 3; i++) {
		int len = strlen(a[i]);

		for (int j = 0; j < len; j++)
			if (a[i][j] != ' ')
				m[a[i][j] - 'a'] = b[i][j];
	}
	m['q' - 'a'] = 'z';
	m['z' - 'a'] = 'q';

	//freopen ("/home/nirvanan/code jam/A-small-attempt3.in", "r", stdin);
	//freopen ("/home/nirvanan/code jam/out.txt", "w", stdout);
	int t, tt = 1;
	char c;
	scanf("%d", &t);
	
	while ((scanf("%c", &c)) != EOF) {
		if (c == '\n') {
			printf("\n");
			if (tt <= t)
				printf("Case #%d: ", tt++);
		}
		else if (c != ' ')
			printf("%c", m[c - 'a']);
		else
			printf(" ");
	}
	
	return 0;
}
