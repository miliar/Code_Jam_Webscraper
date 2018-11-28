/**
*** Google Code Jam - Round 2
***
*** Problem:
*** Author: druidu
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

#define MAXN		40

char buf[MAXN + 10];
int C[MAXN + 1];

void solve(int X)
{
	int N, K;
	int i, j, k;

	assert(scanf("%d\n", &N) == 1);
	for (i = 1; i <= N; i++) {
		assert(fgets(buf, sizeof(buf), stdin));
		C[i] = N;
		for (j = N - 1; j >= 0 && buf[j] == '0'; j--)
			C[i]--;
	}

	K = 0;
	for (i = 1; i < N; i++) {
		if (C[i] <= i)
			continue;
		for (j = i + 1; j <= N && C[j] > i; j++) ;
		for (k = j; k > i; k--) {
			swap(C[k], C[k - 1]);
			K++;
		}
	}

	printf("Case #%d: %d\n", X, K);
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

	assert(scanf("%d", &T) == 1);
	fprintf(stderr, "T=%d\n", T);

	for (X = 1; X <= T; X++) {
		solve(X);
	}

	return 0;
}
