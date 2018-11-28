#include <stdlib.h>
#include <stdio.h>
#include <memory.h>

const char inFileName[] = "C-large.in";
const char outFileName[] = "C-large.out";

const int MaxN = 510;
const int MOD = 100003;

int n, T, sol;
long long binom[MaxN][MaxN];
int d[MaxN][MaxN];

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	memset(binom, 0, sizeof(binom));
	for (int i = 0; i <= MaxN; i++)
		binom[i][0] = 1;
	for (int i = 1; i <= MaxN; i++)
		for (int j = 1; j <= i; j++)
			binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % MOD;



	fscanf(inFile, "%d", &T);
	for (int i = 0; i < T; i++) {
		fscanf(inFile, "%d", &n);

		memset(d, 0, sizeof(d));
		for (int i = 2; i <= n; i++) d[i][1] = 1;

		for (int i = 3; i <= n; i++)
			for (int j = 1; j < i; j++)
				for (int k = 1; k < j; k++)
					d[i][j] = (d[i][j] + d[j][k] * binom[i - j - 1][j - k - 1]) % MOD;

		sol = 0;
		for (int i = 1; i < n; i++)
			sol = (sol + d[n][i]) % MOD;
		fprintf(outFile, "Case #%d: %d\n", i + 1, sol);
	}

	fclose(inFile);
	fclose(outFile);

	return 0;
}
