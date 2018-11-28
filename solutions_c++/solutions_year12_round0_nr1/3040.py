// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("A-small-attempt1.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	unsigned int nCases;
	fscanf(f, "%i", &nCases);
		fgetc(f);

	char* map = "ynficwlbkuomxsevzpdrjgthaq";
	
	for (unsigned int i = 0; i < nCases; i++) {
		printf("Processing case %i\n", i + 1);


		fprintf(fOut, "Case #%i: ", i + 1);

ME:
		char s[256];
		fgets(s, 256, f);

		if (strlen(s) == 0)
			goto ME;

		for (int k = 0; k < strlen(s); k++) {
			char c = ' ';
			if (s[k] == ' ') {
				c = ' ';
			}
			else {
				for (int j = 0; j < strlen(map); j++) {
					if (map[j] == s[k]) {
						c = (char) ('a' + (char)j);
					}
				}
			}

			fputc(c, fOut);
		}

		fprintf(fOut, "\n");
		
		fflush(fOut);
	}

	// getchar();

	fclose(f);
	fclose(fOut);

	return 0;
}

