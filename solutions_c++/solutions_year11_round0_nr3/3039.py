// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>

void minmax(int x, int y, int* max, int* min) {
	if (x > y) {
		*max = x;
		*min = y;
	}
	else {
		*max = y;
		*min = x;
	}
}

int main(int argc, char* argv[])
{
	// Read input
	FILE* f = fopen("C-large.in", "r");
	FILE* fOut = fopen("C-output.txt", "w");

	unsigned values[1001];
	int prev_S1[257];
	int prev_S2[257];
	int S1[257];
	int S2[257];

	int cases;
	fscanf(f, "%i", &cases);
	for (unsigned int iCase = 0; iCase < cases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);

		int N;
		fscanf(f, "%i", &N);

		for (int i = 1; i <= N; i++) {
			fscanf(f, "%u", &values[i]);
		}
/*
		for (int d = 0; d <= 255; d++) {
			prev_S1[d] = -1;
			prev_S2[d] = -1;
		}

		int v1 = values[1];

		prev_S1[v1] = v1;
		prev_S2[v1] = 0;

		for (int i = 2; i <= N; i++) {
			int v = values[i];

			for (int d = 0; d <= 255; d++) {
				S1[d] = -1;
				S2[d] = -1;
			}

			int ps1, ps2, s1, s2, m, M, dx;
			for (int d = 0; d <= 255; d++) {
				ps1 = prev_S1[d];
				ps2 = prev_S2[d];

				if (ps1 == -1 && ps2 == -1)
					continue;

				if (ps1 == -1 || ps2 == -1) {
					int sdfasdfs12 = 0;
				}

				for (int b = 0; b <= 1; b++) {
					s1 = ps1 + b * v;
					s2 = ps2 + (1 - b) * v;

					dx = d ^ v;

					if (dx < 0) {
						int dasfsa = 0;
					}

					printf("dx = %i\n", dx);
					minmax(s1, s2, &M, &m);

					if (S1[dx] < M) {
						S1[dx] = M;
						S2[dx] = m;
					}
				}
			}

			int kxxx = 10000;
			for (int d = 0; d <= 255; d++) {
				prev_S1[d] = S1[d];
				prev_S2[d] = S2[d];
			}

			int dds = 3;
		}

		if (S1[0] == -1)
			fprintf(fOut, "Case #%i: NO\n", iCase + 1);
		else
			fprintf(fOut, "Case #%i: %i\n", iCase + 1, S1[0]);
*/

		int bsum = 0;
		unsigned int sum = 0;
		for (int i = 1; i <= N; i++) {
			bsum = bsum ^ (values[i]);
			sum = sum + values[i];
		} 

		unsigned int min = 100000000;
		for (int i = 1; i <= N; i++) {
			if (values[i] < min)
				min = values[i];
		}

		if (bsum != 0)
			fprintf(fOut, "Case #%i: NO\n", iCase + 1);
		else
			fprintf(fOut, "Case #%i: %u\n", iCase + 1, sum - min);

		fflush(fOut);
	}
	
	fclose(f);
	fclose(fOut);
	
	return 0;
}


