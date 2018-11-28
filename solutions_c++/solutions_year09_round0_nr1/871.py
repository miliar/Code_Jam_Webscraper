#include <stdio.h>

#define MAXL		15
#define MAXD		5000
#define MAXN		500
#define NLETTERS	26
#define MAXPATTERN	(NLETTERS * (NLETTERS + 2))

char words[MAXD][MAXL + 1];

void getpattern(char *buf, unsigned int *pattern)
{
	char *p;

	for (p = buf; *p; p++, pattern++) {
		if (*p == '(') {
			*pattern = 0;
			while (*++p != ')')
				*pattern |= 1 << (*p - 'a');
		} else {
			*pattern = 1 << (*p - 'a');
		}
	}
}

int matchpattern(char *word, unsigned int *pattern)
{
	char *p;

	for (p = word; *p; p++, pattern++)
		if (!(*pattern & (1 << (*p - 'a'))))
			return 0;

	return 1;
}

int main(int argc, char **argv)
{
	int L, D, N;
	int X, K, i;
	char buf[MAXPATTERN + 10];
	unsigned int pattern[MAXL];

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	scanf("%d %d %d", &L, &D, &N);
	fprintf(stderr, "L=%d D=%d N=%d\n", L, D, N);
	for (i = 0; i < D; i++)
		scanf("%s", words[i]);

	for (X = 1; X <= N; X++) {
		scanf("%s", buf);
		getpattern(buf, pattern);
		K = 0;
		for (i = 0; i < D; i++)
			if (matchpattern(words[i], pattern))
				K++;
		printf("Case #%d: %d\n", X, K);
	}

	return 0;
}
