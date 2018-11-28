#include <iostream.h>
#include <math.h>
#include "primes.h"	// primes.h is too big to be uploaded, but is just a vector Primes[pL] with a list of all primes less than 1000001, obtained from http://primes.utm.edu/lists/small/millions/ (first million)

void PrintVec (int *Vec, int C)
{
	int j;
	for (j = 0; j < C; j++) {
		cout << Vec[j] << ' ';
	}
	cout << "\n";
}

main()
{
	int ix, C;
	long long A, B, P;
	int pp, L;
	int i, j, k, m;
	int Y;
	int Sets[1001], Inter[1001];
	int Set, Set2;

	cin >> C;

	for (ix = 1; ix <= C; ix++) {
		cin >> A >> B >> P;
		L = B-A+1;
		for (i = 0; i < L; i++) {
			Sets[i] = 1;
			Inter[i] = i;
		}

		for (i = 0; i < pL; i++) {
			pp = Primes[i];
			if (pp >= P && pp < L) {
				for (j = 0; j < L && (A+j)%pp; j++);
				if (j < L-pp) {
					Set = Inter[j];
					for (k = j+pp; k < L; k += pp) {
						Set2 = Inter[k];
						for (m = 0; m < L; m++) {
							if (Set2 == Inter[m]) {
								Inter[m] = Set;
								Sets[m] = 0;
							}
						}
					}
				}
			}
		}

		cout << "Case #" << ix << ": ";
		Y = 0;
		for (i = 0; i < L; i++)
			if (Sets[i]) Y++;
		cout << Y << "\n";
	}
}
