#include <cstdio>
#include <cstdlib>

int main () {
	int T;
	scanf ("%d", &T);
	for (int t = 0; t < T; t++) {
		printf ("Case #%d: ", t+1);
		int N, K;
		scanf ("%d%d", &N, &K);
		int x = (1<<N);
		if (K%x == x-1)
			printf ("ON\n");
		else
			printf ("OFF\n");
	}
	return 0;
}
