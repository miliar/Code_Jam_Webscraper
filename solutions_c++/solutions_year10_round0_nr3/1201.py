// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("C-small-attempt1.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	int i, j;
	
	unsigned int nCases, R, k, N;

	int g[1000];
	int* s[1000];
	for (i = 0; i < 1000; i++)
		s[i] = new int[1000];

	int t[1000];
	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		fscanf(f, "%i %i %i", &R, &k, &N);

		for (i = 0; i < N; i++) {
			fscanf(f, "%i", &g[i]);
		}

		// Initialize s
		for (i = 0; i < N; i++) {
			s[i][i] = g[i];
		}

		for (i = 0; i < N; i++) {
			for (j = i + 1; j < N; j++) {
				s[i][j] = s[i][j - 1] + g[j];
			}
		}

		for (i = 0; i < N; i++) {
			for (j = 0; j < i; j++) {
				s[i][j] = s[i][N - 1] + s[0][j];
			}
		}
		
		// Init t
		for (i = 0; i < N; i++) {
			int ppl = 0;
			for (j = i; j < i + N; j++) {
				ppl += g[j % N];
				if (ppl > k) {
					break;
				}
			}

			t[i] = (j - 1) % N ;
		}

		// Loop
		int money = 0;
		int x = 0;
		for (i = 0; i < R; i++) {
			money = money + s[x][t[x]];
			x = (t[x] + 1) % N;
		}
		
		fprintf(fOut, "Case #%i: %i\n", iCase + 1, money);
		fflush(fOut);
	}
	
	fclose(f);
	fclose(fOut);
	
	return 0;
}

