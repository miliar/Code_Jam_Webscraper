#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

#include <vector>
#include <algorithm>
#include <complex>
#include <assert.h>
#include <queue>

using namespace std;


int main (void)
{
	int T, N, S, p, t, not_s, count_s;
	int i;

	scanf ("%d", &T);
	for (i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);
		scanf ("%d %d %d", &N, &S, &p);
		not_s = 0;
		count_s = 0;
		for (int j = 0; j < N; j++) {
			scanf ("%d", &t);
			if (t == 0) {
				if (p == 0) { not_s++; }
				continue;
			} else if (t == 1) {
				if (p <= 1) { not_s++; }
				continue;
			}
			if (t > (p-1)*3) { not_s++; }
			else if (t >= (p-1)*3-1) { count_s++; }
//			printf ("%d, %d:%d\n", t, not_s, count_s);
		}
		if (count_s > S) { count_s = S; }
		printf ("%d\n", not_s + count_s);
	}

	return 0;
}
