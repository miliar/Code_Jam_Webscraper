// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <float.h>
// #include "bigint-2010.04.30/BigIntegerLibrary.hh"
#include "ttmath-0.9.2/ttmath/ttmath.h"

using namespace std;

typedef ttmath::Big<2,2> Big;

Big factorial[1001];
Big derangment[1001];
Big average[1001];

void compute_factorial() {
	factorial[0] = 1;
	for (int i = 1; i <= 1000; i++) {
		factorial[i] = factorial[i - 1] * i;
	}
}

void compute_derangment() {
	derangment[0] = 1;
	derangment[1] = 0;
	
	for (int i = 2; i <= 1000; i++) {
		derangment[i] = (derangment[i - 1] + derangment[i - 2]) * (i - 1);
	}
}

void compute_average() {
	average[0] = 0;
	average[1] = -100000000;	// Never used
	average[2] = 2;

	for (int k = 3; k <= 1000; k++) {
		Big sum = 1;
		Big one = 1;
		for (int m = 1; m <= k - 2; m++) {
			sum = sum + derangment[k - m] / (factorial[m] * factorial[k - m]) * average[k - m];
		}

		average[k] = sum / (one - derangment[k] / factorial[k]);

		// printf("%0.6lf", average[k]);
	}
}


int main(int argc, char* argv[])
{
	compute_factorial();
	compute_derangment();
	compute_average();

	for (int i = 0; i < 10; i += 1) {
		printf("%lf, %lf, %lf\n", factorial[i].ToDouble(), derangment[i].ToDouble(), average[i].ToDouble());
	}

	// Read input
	FILE* f = fopen("D-large.in", "r");
	FILE* fOut = fopen("D-output.txt", "w");

	int i, j;
	
	unsigned int nCases, N;

	int perm[1001];
	bool used[1001];
	int nUsed;
	vector<int> groups;

	fscanf(f, "%i", &nCases);
	for (unsigned int iCase = 0; iCase < nCases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);

		groups.clear();
		nUsed = 0;

		fscanf(f, "%i", &N);

		for (i = 1; i <= N; i++) {
			fscanf(f, "%i", &perm[i]);
			used[i] = false;
		}

		// Find permutation group
		
		while (nUsed < N) {
			int k = 0;
			
			for (int j = 1; j <= N; j++)
				if (!used[j]) {
					k = j; break;
				}

			if (k == 0)
				break;

			int c = 0;
			do {
				c++;

				used[k] = true;
				int l = perm[k];
				k = l;
				nUsed++;
			}
			while (!used[k]);

			groups.push_back(c);
		}

		// Add
		double sum = 0;
		for (vector<int>::iterator i = groups.begin(); i != groups.end(); i++) {
			int n = *i;
			if (n > 1) {
				double f = average[n].ToDouble();
				sum += f;
			}
		}
		
		fprintf(fOut, "Case #%i: %1.6lf\n", iCase + 1, sum);
		fflush(fOut);
	}
	
	fclose(f);
	fclose(fOut);

	getchar();
	
	return 0;
}

