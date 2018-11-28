// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

int C[501][501];
int L[501][501];

void init() {
	for (int n = 0; n <= 500; n++) {
		for (int k = 0; k <= 500; k++) {
			if (k > n)
				C[n][k] = 0;
			else if (k == n)
				C[n][k] = 1;
			else
				C[n][k] = -1;
		}
	}

	for (int n = 0; n <= 500; n++) {
		for (int k = 0; k < 500; k++) {
			if (k >= n)
				L[n][k] = 0;
			else
				L[n][k] = -1;
		}
	}

	L[2][1] = 1;
}

int bino(int n, int k) {
	if (C[n][k] != -1)
		return C[n][k];
	else {
		C[n][k] = bino(n - 1, k) * n / (n - k);
		return C[n][k];
	}
}

int l(int n, int k) {
	if (k == 0 || k >= n)
		return 0;

	if (L[n][k] != -1)
		return L[n][k];

	int s = 0;
	for (int i = 0; i <= k - 1; i++) {
		s = (s + l(k, i) * bino(n - k - 1, k - 1 - i)) % 100003;
	}

	L[n][k] = s;

	return s;
}

int ls(int n) {
	int s = 0;

	for (int k = 0; k <= n; k++) {
		s = (s + l(n, k)) % 100003;
	}

	return s;
}

int main(int argc, char* argv[])
{
	init();

	// Read input
	FILE* f = fopen("C-small-attempt2.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases;
	int n;

	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);
		fscanf(f, "%i", &n);

		fprintf(fOut, "Case #%i: %i\n", iCase + 1, ls(n + 1));
		fflush(fOut);
	}
	
	fclose(f);
	fclose(fOut);
	
	return 0;
}

