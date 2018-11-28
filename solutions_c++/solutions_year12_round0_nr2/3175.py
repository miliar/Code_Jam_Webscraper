#include <stdio.h>

int min (int a, int b) {
	return a<b?a:b;
}

int main (void) {
	int T, c, N, S, p, t, cert, poss;
	int i, k;
	scanf ("%d", &T);
	for (c = 1; c <= T; c++) {
		scanf ("%d%d%d", &N, &S, &p);
		cert = poss = 0;
		for (i = 0; i < N; i++)	{
			scanf ("%d", &t);
			k = t%3;
			if (k == 0)	{
				if (t/3 >= p)	cert++;
				else if ((t-3) >= 0 && ((t-3)/3+2) >= p)	poss++;
			} else if (k == 1) {
				if (((t-1)/3+1) >= p)	cert++;
				else if ((t-4) >= 0 && ((t-4)/3+2) >= p)	poss++;
			} else {
				if (((t-2)/3+1) >= p)	cert++;
				else if (((t-2)/3+2) >= p)	poss++;
			}
		}
		printf ("Case #%d: %d\n", c, cert+min(poss, S));
	}
	return 0;
}
