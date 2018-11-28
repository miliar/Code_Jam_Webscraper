#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int n, pd, pg;

bool judge(int a, int b, int c) {
	int n = a;
	double pd = (float) b / 100;
	double pg = (float) c / 100;

	for (int i = 1; i <= n; ++i) {
		double aa = i * pd;

		if (aa == (int) aa) {
			for (int j = i; j; ++j) {
				double bb = j * pg;
				if (bb == (int) bb) {

					if ((int)aa <= (int) bb) {
						if (pg <= 1.0 - (i - (int) aa) / (double)j)
							return true;
					}
				}
				if (j >= 10000)	break;
			}
		}
	}
	return false;
}

int main() {
	int t;
	freopen("A.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf ("%d", &t);

	for (int ii = 1; ii <= t; ++ii) {
		scanf ("%d %d %d", &n, &pd, &pg);
		if (judge(n, pd, pg)) 
			printf("Case #%d: Possible\n", ii);
		else 
			printf("Case #%d: Broken\n", ii);
	}

	return 0;
}