#include <stdlib.h>
#include <stdio.h>

const char inFileName[] = "C-large.in";
const char outFileName[] = "C-large.out";

int T, n, c, x, sum, min;

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++) {

		fscanf(inFile, "%d", &n);
		sum = 0; x = 0; min = 1000000000;
		for (int i = 0; i < n; i++) {
			fscanf(inFile, "%d", &c);
			sum += c;
			x ^= c;
			if (c < min) min = c;
		}

		if (x == 0)
			fprintf(outFile, "Case #%d: %d\n", t + 1, sum - min);
		else
			fprintf(outFile, "Case #%d: NO\n", t + 1);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
