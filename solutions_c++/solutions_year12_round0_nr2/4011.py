/*
 * Dancing.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Jason Wu
 */

#include "Dancing.h"

void QR2012::Dancing::solve() {
	int T, S, p, N;
	int t[100];

	scanf("%d", &T);

	for (int c = 1; c <= T; c++) {
		scanf("%d %d %d", &N, &S, &p);
		REP(i, N) scanf("%d", t+i);

		int a = 0;

		REP(i, N) {
			int best = t[i] / 3;
			if (t[i] % 3 != 0) ++best;
			if (best >= p) {
				++a;
				continue;
			}

			if (best == 0) continue;

			if (S && (t[i]%3) != 1 && best+1 == p) {
				++a;
				--S;
			}
		}

		printf("Case #%d: %d\n", c, a);
	}
}
