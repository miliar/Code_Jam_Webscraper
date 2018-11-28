#include <cstdio>


int main() {
	FILE *fin = fopen("B-small-attempt1.in", "rt");
	FILE *fout = fopen("out.txt", "wt");

	int T;

	fscanf(fin, "%d", &T);

	for (int t = 0; t < T; ++t) {
		int l, timp, n, c;
		int A[1000] = {0};
		int C[1000] = {0};
		int I[1000] = {0};
		int normal_time = 0;
		int overhead = 0;
		int full = 0;
		int groups = 0;
		int remaining_time = 0;

		unsigned long long total = 0;

		fscanf(fin, "%d %d %d %d", &l, &timp, &n, &c);
		groups = n / c; // full groups
		for (int i = 0; i < c; ++i) {
			fscanf(fin, "%d", &A[i]);
			normal_time += A[i];
		}
		normal_time *= 2; // time for a group

		total = normal_time * groups;
		for (int i = groups * c; i < n; ++i) total += (2 * A[i % c]);

		overhead = timp / normal_time; // overhead -> no towers
		full = groups - overhead; // full groups (can have towers anywhere)
		if (timp % normal_time != 0) --full;

		remaining_time = timp % normal_time;
		bool partial_group = (remaining_time != 0) ? true : false;
		for (int i = 0; i < c; ++i) {
			C[i] = full;
			if (n % c > i) C[i]++;
			if (partial_group) {
				if (remaining_time > 2 * A[i]) {
					I[i] = 0;
					remaining_time -= 2 * A[i];
				} else {
					I[i] = A[i] - remaining_time / 2;
					remaining_time = 0;
				}
			} else {
				I[i] = 0;
			}
		}

		// Now let's start finding the maximum values from A[i] and I[i]
		// If it's from A, then put as many towers as possible
		// If it's from B, then put 1 tower
		while (l != 0) {
			int maxa, maxi, pozi, poza;
			maxa = 0; maxi = 0; pozi = 0; poza = 0;
			for (int i = 0; i < c; ++i) {
				if (A[i] > maxa) {
					maxa = A[i];
					poza = i;
				}
				if (I[i] > maxi) {
					maxi = I[i];
					pozi = i;
				}
			}
			if (maxi > maxa) {
				l--;
				total -= I[pozi];
				I[pozi] = 0;
			} else {
				if (l > C[poza]) {
					total -= A[poza] * C[poza];
					A[poza] = 0;
					l -= C[poza];
				} else {
					total -= A[poza] * l;
					A[poza] = 0;
					l = 0;
				}
			}
		}
		fprintf(fout, "Case #%d: %llu\n", t + 1, total);
	}
	fclose(fout);
	return 0;
}
	