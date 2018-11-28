// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("C-small-attempt0.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases;
	fscanf(f, "%i", &nCases);
	
	for (unsigned int i = 0; i < nCases; i++) {
		printf("Processing case %i\n", i + 1);

		double A, B;
		fscanf(f, "%lf %lf", &A, &B);

		int k = (int)floor(log10(A)) + 1;
		int C = 0;

		for (int n = 1; n <= k - 1; n++) {
			int m = k - n;

			int m10 = (int)pow(10.0, m);
			int n10 = (int)pow(10.0, n);

			// if (m >= n) {
				int AA = A / m10 - 2;
				int BB = B / m10 + 2;

				for (int a = AA; a <= BB; a++) {
					int l1 = (int) ceil(A - a *  m10);
					int l2 = (int) floor((double) a * (m10 - 1) / (n10 - 1)) + 1;
					int u = (int) floor((B - a) / n10);
					int l = l1;
					if (l2 > l1)
						l = l2;

					if (u >= l) {
						// printf("a = %i => b = [%i, %i]\n", a, l, u);
						C += (u - l + 1);
					}
				}
			/*
			}
			else {
				int AA = A / n10 - 2;
				int BB = B / n10 + 2;

				for (int b = AA; b <= BB; b++) {
					int l = (int) ceil((A - b) / m10);
					int u1 = (int) ceil((double)b * (n10 - 1) / (m10 - 1)) - 1;
					int u2 = (int) floor(B - b * n10);
					int u = u1;
					if (u2 < u1)
						u = u2;

					if (u >= l) {
						// printf("b = %i => a = [%i, %i]\n", b, l, u);
						C += (u - l + 1);
					}
				}
			}
			*/
		}
		
		fprintf(fOut, "Case #%i: %i\n", i + 1, C);

		fflush(fOut);
	}

	printf("DONE!");

	getchar();

	fclose(f);
	fclose(fOut);

	return 0;
}

