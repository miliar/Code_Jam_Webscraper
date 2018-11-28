
#include <stdio.h>

long long T, t, N;
long long a[501][500];
long long c[501][501];

void cal() {
	int h;
	long long i, j, n, r;
	for(i = 0; i <= 500; i++) {
		for(j = 0; j <= 500; j++) {
			if(j == 0 || j == i) c[i][j] = 1;
			else c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 100003;
		}
	}
	for(n = 2; n <= 500; n++) {
		for(r = 1; r < n; r++) {
			if(r < 3 || r == n - 1) a[n][r] = 1;
			else {
				for(i = 1; i < r; i++) {
					if(n - r - 1 < r - i - 1) h = 0;
					else h = c[n - r - 1][r - i - 1];
					a[n][r] += (a[r][i] * h) % 100003;
				}
			}
		}
	}
}

int main(void) {
	long long i, ans;
	FILE* fin;
	FILE* fout;
	fin = fopen("C-small-attempt2.in", "r");
	fout = fopen("output.txt", "w");

	cal();
	fscanf(fin, "%I64d", &T);
	for(t = 1; t <= T; t++) {
		ans = 0;
		fscanf(fin, "%I64d", &N);
		for(i = 1; i < N; i++) ans = (ans + a[N][i]) % 100003;
		fprintf(fout, "Case #%I64d: %I64d\n", t, ans);
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
