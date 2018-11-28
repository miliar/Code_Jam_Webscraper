#include <cstdio>

FILE *in, *out;

int group[2002];
int next[1002];
long long cost[1002];

int main() {
	in = fopen("C.in", "r");
	out = fopen("C.out", "w");
	int T;
	fscanf(in, "%d", &T);
	for (int t = 1; t <= T; t++) {
		int R, k, N;
		fscanf(in, "%d %d %d", &R, &k, &N);
		for (int i = 1; i <= N; i++) {
			fscanf(in, "%d", &group[i]);
			group[N + i] = group[i];
		}
		for (int i = 1; i <= N; i++) {
			int end = i;
			long long sum = 0;
			while(sum + group[end] <= k && end < i + N)
				sum += group[end++];
			cost[i] = sum;
			next[i] = (end - 1) % N + 1;
		}
		
		int start = 1;
		long long sum = 0;
		int cnt = 0;
		do {
			sum += cost[start];
			start = next[start];
			if (++cnt == R)
				break;
		} while (start != 1);

		if (cnt == R) { // no more than one cycle
			fprintf(out, "Case #%d: %lld\n", t, sum);
		} 
		else { // more than one cycle
			long long total = sum * (R / cnt);
			R %= cnt;

			if (R) {
				cnt = 0;
				do {
					total += cost[start];
					start = next[start];
				} while(++cnt != R);
			}

			fprintf(out, "Case #%d: %lld\n", t, total);
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}
