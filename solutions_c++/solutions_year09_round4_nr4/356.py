#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

using namespace std;

int nTC;
int x[1000], y[1000], R[1000];

double sqr (double v) {
	return v * v;
}



int main() {
	scanf ("%d", &nTC);
	
	for (int tc = 1; tc <= nTC; tc++) {
		double hasil;
		int N;
		
		scanf ("%d", &N);
		
		for (int i = 0; i < N; i++) {
			scanf ("%d%d%d", &x[i], &y[i], &R[i]);
		}
		
		if (N == 1) {
			hasil = R[0];
		} else if (N == 2) {
			hasil = max (R[0], R[1]);
		} else if (N == 3) {
			bool found = false;
			for (int i = 0; i < 3; i++) {
				for (int j = i + 1; j < 3; j++) {
					double tmp = sqrt (sqr (1.0 * x[i] - x[j]) + sqr (1.0 * y[i] - y[j])) + R[i] + R[j];
					int idx = 3 - i - j;
					tmp = max (tmp, 1.0 * R[idx]);
					if (!found)
						hasil = tmp;
					else
						hasil = min (hasil, tmp);
					found = true;
				}
			}
			hasil = hasil / 2.0;
		}
		
		printf ("Case #%d: %.6lf\n", tc, hasil);
	}
	
	return 0;
}
