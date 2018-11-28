/**
*** Google Code Jam - Round 1A
***
*** Author: druidu
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAXNUMBER	50000000
#define MAXBASE		10
#define HAPPY		9999999

int happy[MAXNUMBER][9];

int ishappy(int n, int base)
{
	int sum, digit, i;

	if (n == 1)
		return 1;
	if (happy[n][base-2])
		return happy[n][base-2] == HAPPY || happy[happy[n][base-2]][base-2] == HAPPY ? 1 : 0;

	i = n;
	while (!happy[i][base-2] && i != 1) {
		happy[i][base-2] = n;
		sum = 0;
		while (i) {
			digit = i % base;
			i /= base;
			sum += digit * digit;
		}
		i = sum;
	}

	if (i == 1 || happy[i][base-2] == HAPPY || happy[happy[i][base-2]][base-2] == HAPPY) {
		happy[n][base-2] = HAPPY;
		return 1;
	} else {
		return 0;
	}
}

void solve(int X)
{
	char buf[100], *p;
	int bases[MAXBASE], nbases, i, j;

	nbases = 0;
	gets(buf);
	p = strtok(buf, " ");
	while (p) {
		bases[nbases++] = atoi(p);
		p = strtok(NULL, " ");
	}

	for (i = 2; ; i++) {
		for (j = 0; j < nbases; j++)
			if (!ishappy(i, bases[j]))
				break;
		if (j == nbases)
			break;
	}

	printf("Case #%d: %d\n", X, i);
}

int main(int argc, char **argv)
{
	int T, X;

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	scanf("%d\n", &T);
	fprintf(stderr, "T=%d\n", T);

	for (X = 1; X <= T; X++) {
		solve(X);
	}

	return 0;
}
