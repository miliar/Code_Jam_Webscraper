// gcj2010.cpp : Defines the entry point for the console application.
//

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>

#include <math.h>
__int64 x;

using namespace std;

vector<__int64> nums;

void primes() {
	double s = pow(10.0, 4);
	double x;
	for (__int64 i = 2; i <= s; i+=2) {
		if ((i % 1000000000) == 0)
			printf("%I64u\n", nums.size());
	
		x = sqrt((double)i);

		bool flag = false;
		for (vector<__int64>::iterator f = nums.begin(); f != nums.end(); f++) {
			__int64 k = *f;

			if (k > x) {
				flag = true;
				break;
			}

			
			if ((i % k) == 0) {
				flag = true;
				break;
			}
		}

		if (!flag)
			nums.push_back(i);
	}

	int mmm = nums.size();
	for (vector<__int64>::iterator f = nums.begin(); f != nums.end(); f++) {
		printf("%I64u ", f);
	}
}

int main(int argc, char* argv[])
{
	int k = sizeof(x);
	// primes();
	// Read input
	FILE* f = fopen("C-small-attempt1.in", "r");
	FILE* fOut = fopen("output.txt", "w");

	int cases;
	fscanf(f, "%i", &cases);
	int N, L ,H;
	int freqs[10000];

	for (unsigned int iCase = 0; iCase < cases; iCase++) {
		printf("Processing case #%i\n", iCase + 1);

		fscanf(f, "%i %i %i", &N, &L, &H);
		for (int j = 0; j < N; j++) {
			fscanf(f, "%i", &freqs[j]);
		}

		int answ = -1;
		for (int k = L; k <= H; k++) {
			bool ok = true;
			for (int x = 0; x < N; x++) {
				int f = freqs[x];
				if (!(((k % f) == 0) || ((f % k) == 0))) {
					ok = false;
					break;
				}
			}

			if (!ok) {
				continue;
			}
			else {
				answ = k;
				break;
			}
		}

		if (answ != -1)
			fprintf(fOut, "Case #%i: %u\n", iCase + 1, answ);
		else
			fprintf(fOut, "Case #%i: NO\n", iCase + 1);

		fflush(fOut);
	}
	
	fclose(f);
	fclose(fOut);

	getchar();
	
	return 0;
}


