/**
*** Google Code Jam - Round 2
***
*** Problem: C
*** Author: druidu
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

#define MAXN	100
#define MAXK	25
#define NTRIES	100000

int prices[MAXN][MAXK];
int cross[MAXN][MAXN];
int color[MAXN];
int idx[MAXN];

int testcross(int *p1, int *p2, int K)
{
	int i, sign, sign2;

	for (i = 0; i < K; i++)
		if (p1[i] == p2[i])
			return 1;

	sign = p1[0] < p2[0] ? 1 : 0;
	for (i = 1; i < K; i++) {
		sign2 = p1[i] < p2[i] ? 1 : 0;
		if (sign2 != sign)
			return 1;
	}

	return 0;
}

void solve(int X)
{
	int N, K;
	int i, j, k, ii, jj, kk, tt, ncolors, mincolors;

	assert(scanf("%d %d", &N, &K) == 2);
	for (i = 0; i < N; i++)
		for (j = 0; j < K; j++)
			assert(scanf("%d", &prices[i][j]) == 1);

	memset(cross, 0, sizeof(cross));
	for (i = 0; i < N; i++)
		cross[i][i] = 1;

	for (i = 0; i < N - 1; i++)
		for (j = i + 1; j < N; j++)
			if (testcross(prices[i], prices[j], K))
				cross[i][j] = cross[j][i] = 1;

	for (i = 0; i < N; i++) {
		cross[i][i] = 1;
		idx[i] = i;
	}

			/*
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++)
			fprintf(stderr, "%d ", cross[i][j]);
		fprintf(stderr, "\n");
	}
	//*/

	mincolors = N;
	for (tt = NTRIES; tt; tt--) {
		memset(color, 0, sizeof(color));
		ncolors = 0;
		for (ii = 0; ii < N; ii++) {
			i = idx[ii];
			if (!color[i]) {
				color[i] = ++ncolors;
				for (jj = ii + 1; jj < N; jj++) {
					j = idx[jj];
					for (kk = ii; kk < jj; kk++) {
						k = idx[kk];
						if (color[k] == color[i] && cross[k][j])
							break;
					}
					if (kk == jj)
						color[j] = color[i];
				}
			}
		}
		if (mincolors > ncolors)
			mincolors = ncolors;
		random_shuffle(idx, idx + N);
	}

	printf("Case #%d: %d\n", X, mincolors);
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

	assert(scanf("%d", &N) == 1);
	fprintf(stderr, "N=%d\n", N);

	for (X = 1; X <= N; X++) {
		solve(X);
	}

	return 0;
}
