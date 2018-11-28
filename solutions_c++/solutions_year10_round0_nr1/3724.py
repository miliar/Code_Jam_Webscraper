#include <stdio.h>

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int N, K, T, t, n;
	scanf ("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf ("%d %d", &N, &K);
		n = (1 << N);
		K %= n;
		if (K == (n-1)) printf ("Case #%d: ON\n", t);
		else printf ("Case #%d: OFF\n", t);
	}
	return 0;
}

