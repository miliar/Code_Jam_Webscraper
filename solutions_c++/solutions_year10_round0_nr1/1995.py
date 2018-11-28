#include <stdlib.h>
#include <stdio.h>

const char inFileName[] = "A-large.in";
const char outFileName[] = "A-large.out";

int T, n, k;

int main() {
	
	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int i = 0; i < T; i++) {
		fscanf(inFile, "%d%d", &n, &k);
		if ((k + 1) % (1 << n) == 0)
			fprintf(outFile, "Case #%d: ON\n", i + 1);
		else
			fprintf(outFile, "Case #%d: OFF\n", i + 1);
	}	
	
	fclose(inFile);
	fclose(outFile);
	return 0;
}
