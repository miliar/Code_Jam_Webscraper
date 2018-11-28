#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define DEBUG 0
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

int main () {
	int nCases, iCase = 0;
	cin >> nCases;

	while (iCase < nCases) {
		int nCandy;
		cin >> nCandy;

		int val[nCandy];
		unsigned long long sum = 0;
		int min = -1;
		int xorSum = 0;
		for (int i = 0; i < nCandy; i++) {
			cin >> val[i];
			if (min == -1 ||
				min > val[i]) {
				min = val[i];
			}
			sum += val[i];
			xorSum ^= val[i];
		}

		printf ("Case #%d: ", ++iCase);
		if (xorSum != 0) {
			printf ("NO\n");
		} else {
			printf ("%llu\n", sum - min);
		}
	}

	return 0;
}
