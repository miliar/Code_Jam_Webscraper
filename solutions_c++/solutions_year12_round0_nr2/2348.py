#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

#define MAX_LINE 1024

#define RN(v) \
({ \
	char line[MAX_LINE]; \
	RL(line); \
	sscanf(line, "%d", &v); \
})

#define RNN(v, n, line) \
({ \
	int i; \
	char *s = line; \
	char *e; \
	for (i = 0; i < n; i++) { \
		v[i] = strtol(s, &e, 10); \
		s = e; \
	} \
	i; \
})

#define RL(line) \
({ \
	int size = -1; \
	if (fgets(line, sizeof(line), stdin)) {; \
		size = strlen(line) - 1; \
		line[size] = 0; \
	} \
	size; \
})

// triplet, 3 scores
// tree judges 0~10
// 1점차 not
// 2점차 sup.
// 2점초과 미발생
// suprising 2명이면서... 8이상의 점수가 있는 사람 수!

// 평균점수가 p이상이면 good!
// 평균점수가 p미만이고... S???
int
foo(int N, int S, int p, int *G)
{
	int x = 0;

	for (int i = 0; i < N; i++) {
		int avg = G[i] / 3;
		int mod = G[i] % 3;

//printf("G=%d, avg=%d, mod=%d, S=%d, p=%d, x=%d\n", G[i], avg, mod, S, p, x);
		if (avg >= p) {
			x++;
			continue;
		}

		int n = p - avg;
		if (n == 1) {
			if (mod > 0) {
				x++;
			}
			else if (S > 0) {
				if (avg > 0) {
					S--;
					x++;
				}
			}
		}
		else if (n == 2) {
			if (mod > 1) {
				if (S > 0) {
					S--;
					x++;
				}
			}
		}
	}

	return x;
}

int
main(int argc, char *argv[])
{
	char buff[MAX_LINE];

	int T; // # of test cases
	RN(T);

	// # of googlers(N), # of sup.(S), (p)

	for (int i = 0; i < T; i++) {
		RL(buff);
		char *s, *e;
		int N, S, p;

		s = buff;
		N = strtol(s, &e, 10);
		S = strtol(e, &s, 10);
		p = strtol(s, &e, 10);
		// e...
		int G[N];
		RNN(G, N, e);

		int x;
		x = foo(N, S, p, G);
		printf("Case #%d: %d\n", i + 1, x);
/*
		printf("%d, %d, %d\n", N, S, p);
		for (int j = 0; j < N; j++) {
			printf("%d ", G[j]);
		}
		printf("\n");
*/
	}
	return 0;
}

