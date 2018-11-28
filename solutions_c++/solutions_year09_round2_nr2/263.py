/**
*** Google Code Jam - Round 1B
***
*** Problem: B10
*** Author: druidu
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <algorithm>

using namespace std;

#define MAXDIGITS		20

void solve(int X)
{
	char orig[MAXDIGITS + 10];
	char num[MAXDIGITS + 10], *p, ch;
	int s, i, j;

	scanf("%s", num);
	strcpy(orig, num);
	s = strlen(num);

	for (i = 0; i < s - 1; i++)
		if (num[i] < num[i + 1])
			break;
	if (i == s - 1) {
		// decending digits
		// add one zero to digits and sort ascending
		num[s++] = '0';
		num[s] = '\0';
		sort(num, num + s);
		// first digit can't be zero, shift first non-zero digit
		for (p = num; *p == '0'; p++) ;
		assert(*p != '\0');
		*num = *p;
		*p = '0';
	} else {
		// general case
		for (i = s - 1; i > 0; i--)
			if (num[i] > num[i - 1])
				break;
		assert(i > 0);
		i--;
		for (j = s - 1; j > i; j--)
			if (num[j] > num[i])
				break;
		assert(j > i);
		ch = num[i];
		num[i] = num[j];
		num[j] = ch;
		sort(num + i + 1, num + s);
	}

	printf("Case #%d: %s\n", X, num);

#if 0
	fprintf(stderr, "#%d: '%s' => '%s'\n", X, orig, num);
#endif
}

int main(int argc, char **argv)
{
	int N, X;

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	scanf("%d", &N);
	fprintf(stderr, "N=%d\n", N);

	for (X = 1; X <= N; X++) {
		solve(X);
	}

	return 0;
}
