#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>

using namespace std;

#define INFINITO 2000000000
#define QMAX 128

int p, q;
int Q[QMAX];
int M[QMAX];

int make() {
	int out = INFINITO;
	for (int i = 0; i < q; i++) {
		if (!M[i]) {
			M[i] = 1;
			int tmp = 0;
			for (int j = Q[i]-1; j >= 1; j--) {
				int ok = 1;
				for (int k = i-1; k >= 0; k--) {
					if (Q[k] == j && M[k]) {
						ok = 0;
						j = 0;
						k = 0;
					}
				}
				if (ok) {
					tmp++;
				}
			}
			for (int j = Q[i]+1; j <= p; j++) {
				int ok = 1;
				for (int k = i+1; k < q; k++) {
					if (Q[k] == j && M[k]) {
						ok = 0;
						j = p+1;
						k = q+1;
					}
				}
				if (ok) {
					tmp++;
				}
			}
			tmp+= make();
			out = min(out, tmp);
			M[i] = 0;
		}
	}
	if (out == INFINITO)
		return 0;
	return out;
}

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		scanf("%d %d", &p, &q);
		for (int i = 0; i < q; i++) {
			M[i] = 0;
			scanf("%d", &Q[i]);
		}
		sort(Q, Q+q);
		printf("Case #%d: %d\n", test+1, make());
	}
	return 0;
}

