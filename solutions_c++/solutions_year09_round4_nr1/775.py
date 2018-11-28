#include <cstdio>

int main(void) {
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output-la.txt", "w");
	int T;
	fscanf(in, "%d", &T);
	for (int t = 0; t < T; t++) {
		int N;
		int res=0;
		int matr[42][42];
		int rows[42];
		char buf[45];
		fscanf(in, "%d", &N);
		fgets(buf, 45, in);
		printf("N=%d\n", N);
		for (int i = 0; i < N; i++) {
			fgets(buf, 45, in);
			printf("readen=%s", buf);
			rows[i] = -1;
			for (int j = 0; j < N; j++) {
				matr[i][j] = buf[j] - '0';
				if (matr[i][j])
					rows[i] = j;
				printf("%d ", matr[i][j]);
			}
			printf(" - %d\n", rows[i]);
		}
		for (int i = 0; i < N; i++) {
			if (rows[i] > i) {
				for (int i2 = i; i2 < N; i2++)
					if (rows[i2] <= i) {
						res += i2-i;
						for (int j = i2 - 1; j >= i; j--) {
							int t = rows[j];
							rows[j]=rows[j+1];
							rows[j+1]=t;
						}
						break;
					}
			}
		}
		fprintf(out, "Case #%d: %d\n", t+1, res);
	}
	fclose(in);
	fclose(out);
}
