
#include <stdio.h>

int C, N, K, B, T, c;
int X[51], V[51], R[51];
int i, ans, nt;

int main(void) {
	FILE* fin;
	FILE* fout;
	fin = fopen("B-large.in", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &C);
	for(c = 1; c <= C; c++) {
		ans = 0;
		nt = 0;
		fscanf(fin, "%d%d%d%d", &N, &K, &B, &T);
		for(i = 0; i < N; i++) fscanf(fin, "%d", &X[i]);
		for(i = 0; i < N; i++) fscanf(fin, "%d", &V[i]);
		for(i = 0; i < N; i++) {
			R[i] = (B - X[i]) / V[i];
			if((B - X[i]) % V[i]) R[i]++;
		}
		for(i = N - 1; i >=0; i--) {
			if(R[i] <= T) {
				K--;
				ans += nt;
				if(K == 0) break;
			}else {
				nt++;
			}
		}
		if(K) {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", c);
		}else {
			fprintf(fout, "Case #%d: %d\n", c, ans);
		}
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
