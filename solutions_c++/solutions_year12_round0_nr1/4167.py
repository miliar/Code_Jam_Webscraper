/**
 * Code Jam 2012 Problem A
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

char g2e[128];
bool hit_e[128];

char googlerese[3][128] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char english[3][128] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

char line[1024];

int main()
{
	for (int i=0, k; i<3; ++i)
		for (k=0; googlerese[i][k]; ++k) {
			g2e[googlerese[i][k]] = english[i][k];
			hit_e[english[i][k]] = 1;
		}
	g2e['q'] = 'z';
	g2e['z'] = 'q';

	int kase, serial=1;

	gets(line);
	kase = atoi(line);

//	for (int i='a'; i<='z'; ++i)
//		putchar(i);
//	puts("");
//	for (int i='a'; i<='z'; ++i)
//		putchar(g2e[i]);
//	puts("");

	while (kase--) {
		gets(line);
		printf("Case #%d: ", serial++);
		for (int i=0; line[i]; ++i)
			putchar(g2e[line[i]]);

		puts("");
	}

	return 0;
}
