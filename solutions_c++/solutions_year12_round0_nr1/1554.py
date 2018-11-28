#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
char s[] = {'y', 'h', 'e', 's', 'o', 'c', 'v',
			'x', 'd', 'u', 'i', 'g', 'l', 'b',
			'k', 'r', 'z', 't', 'n', 'w',
			'j', 'p', 'f', 'm', 'a', 'q'};

char line[101];
int main()
{
	int T;
	scanf("%d\n", &T);
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		gets(line);
		int len = strlen(line);
		for (int i=0; i<len; i++) {
			if (line[i] != ' ') {
				line[i] = s[line[i]-'a'];
			}
			putchar(line[i]);
		}
		puts("");
	}

	return 0;
}