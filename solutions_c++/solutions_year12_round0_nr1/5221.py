#include <stdio.h>

int T;

char G[] = 
"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";

char E[] =
"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";

char M[256];
char B[1000];

void initmap()
{
	char *g = G, *e = E;

	for (; *g && *e; g++, e++) {
		if (*g >= 'a' && *g <= 'z') {
			if (!M[*g]) {
				M[*g] = *e;
			} else if (M[*g] != *e)
				printf("error %c maps %c != %c\n", *g, *e, M[*g]);
		}
	}

	for (char q = 'a'; q <= 'z'; q++)
		if (!M[q])
			printf("no mapping for %c\n", q);


}

main()
{
	initmap();

	gets(B);
	sscanf(B, "%d", &T);

	for (int i = 1; i <= T; ++i) {
		gets(B);
		for (char *c = B; *c; c++) {
			if (M[*c])
				*c = M[*c];
		}
		printf("Case #%d: %s\n", i, B);
	}

}
