#include <stdio.h>
#define abs(x) ((x) > 0) ? (x) : -(x)

int main() {
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N;
		char R[100];
		int P[100];

		int result = 0;

		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf(" %c %d", &R[i], &P[i]);
		}

		int oq=0, bq=0;
		int op=1, bp=1;

		for (int i = 0; i < N; i++) {
			int *cur, *other, *cur_p, *other_p;
			if (R[i] == 'O') {
				cur = &oq;
				cur_p = &op;
				other = &bq;
				other_p = &bp;
			} else {
				cur = &bq;
				cur_p = &bp;
				other = &oq;
				other_p = &op;
			}

			int pdelta = abs(*cur_p - P[i]);

			if (*cur + pdelta < *other) {
				*cur = *other + 1;
			} else {
				*cur += pdelta + 1;
			}

			*cur_p = P[i];
		}

		result = oq > bq ? oq : bq;

		printf("Case #%d: %d\n", t, result);
	}

	return 0;
}
