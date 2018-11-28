#include <stdio.h>

int main (void) {
	int T, c, A, B, i, count, k, n, m;
	int pot10[] = {1,10,100,1000,10000,100000,1000000,10000000};
	scanf ("%d", &T);
	for (c = 1; c <= T; c++) {
		scanf ("%d%d", &A, &B);
		count = 0;
		if (A < 10)	A = 12;
		for (n = A; n < B; n++) {
			for (i = 1; i < 7 && n >= pot10[i]; i++);
			for (k = 1; k < i; k++) {
				m = (n%pot10[k])*pot10[i-k]+n/pot10[k];
				if (m <= B && m > n)	count++;
			}
		}
		printf ("Case #%d: %d\n", c, count);
	}
	return 0;
}
