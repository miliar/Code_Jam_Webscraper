// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>



int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("A-large.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases, N, K;
	fscanf(f, "%i", &nCases);
	for (unsigned int i = 0; i < nCases; i++) {
		fscanf(f, "%i %i", &N, &K);

		while (K > 0 && N > 0) {
			if ((K & 0x01) == 0x00)
				break;

			K = K >> 1;
			N--;
		}

		fprintf(fOut, "Case #%i: %s\n", i + 1, N == 0 ? "ON" : "OFF");
		fflush(fOut);
	}

	fclose(f);
	fclose(fOut);

	return 0;
}

