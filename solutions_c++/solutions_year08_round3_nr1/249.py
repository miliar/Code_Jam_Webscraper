#include <stdio.h>
#include <algorithm>

using namespace std;

int t, T;

int P, K, L;
int i, k;
__int64 f[1000];
__int64 sum[1000];
int n[1000];

int main() {

	//FILE *in = fopen("A-small.in", "rt");
	//FILE *out = fopen("A-small.out", "wt");

	FILE *in = fopen("A-large.in", "rt");
	FILE *out = fopen("A-large.out", "wt");

	fscanf(in, "%d", &T);

	for (t = 1; t <= T; t++) {

		fscanf(in, "%d %d %d" ,&P, &K, &L);

		for (i = 0; i < L; i++)
			fscanf(in, "%I64d", &f[i]);

		sort(f, f+L);

		for (i = 0; i < K; i++) {
			sum[i] = 0;
			n[i] = 0;
		}

        k = 0;
		for (i = L-1; i >= 0; i--) {
			sum[k] += f[i] * (n[k] + 1);
			n[k]++;
			k++; if (k == K) k = 0;
		}

		__int64 cnt = 0;
		for (i = 0; i < K; i++)
			cnt += sum[i];

		fprintf(out, "Case #%d: %I64d\n", t, cnt);
	}

	fclose(in);
	fclose(out);

	return 0;
}