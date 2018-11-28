// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("B-large.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases;
	fscanf(f, "%i", &nCases);
	
	for (unsigned int i = 0; i < nCases; i++) {
		printf("Processing case %i\n", i + 1);

		 int N, S, p;
		fscanf(f, "%i %i %i", &N, &S, &p);

		 int C = 0;

		for (int j = 0; j < N; j++) {
			int m;
			fscanf(f, "%i", &m);

			if (p == 0) {
				C++;
			}
			else if (p == 1) {
				if (m >= 1) {
					C++;
				}
				else { // m = 0

				}
			}
			else {
				if (m >= 3 * p - 2) {
					C++;
				}
				else if (m >= 3 * p - 4) {
					if (S > 0) {
						C++;
						S--;
					}
				}
				else {
				}
			}
		}

		fprintf(fOut, "Case #%i: %i\n", i + 1, C);

		fflush(fOut);
	}

	fclose(f);
	fclose(fOut);

	return 0;
}

