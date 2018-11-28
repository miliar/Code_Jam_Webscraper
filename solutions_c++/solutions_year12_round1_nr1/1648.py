#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	FILE *fp;
	if((fp=fopen(argv[1],"r"))==NULL) {
		printf("Cannot open file.\n");
		exit(1);
	}

	unsigned T;
	fscanf(fp, "%u%*c", &T);

	unsigned A, B, Ai, SKS, FKS;
	float X, Xi, Sol;
	for (int i = 1; i<=T; i++) {
		fscanf(fp, "%u %u%*c", &A, &B);
		X = 1;
		Sol = 1 + B + 1;
		for (Ai = 1; Ai <= A; Ai++) {
			fscanf (fp, "%f", &Xi);
			X = X * Xi;
			SKS = A - Ai + B - Ai + 1;
			FKS = SKS + B + 1;
			Sol = min (Sol, (X*SKS + (1-X)*FKS));
		}
		printf ("Case #%d: %f\n", i, Sol);
	}
	fclose(fp);
	return 0;
}