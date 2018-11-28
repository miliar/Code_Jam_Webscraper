#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static int E[] = {
		0,
		10,
		100,
		1000,
		10000,
		100000,
		1000000
};

int func(int A, int B)
{
	int y = 0;
	int n;
	int e0;
	int e1;
	int m;

	for(n = A; n <= B; n++) {
		int v = 0;
		int w[7];
		for(e0 = 1; e0 < 6; e0++) {
			int n0;
			int n1;

			n0 = n / E[e0];
			n1 = n % E[e0];
			for(e1 = 1; e1 < 6; e1++) {
				if(n0 < E[e1]) {
					m = n1 * E[e1] + n0;
					break;
				}
			}
			if((A <= n) && (n < m) && (m <= B)) {
				int x;
				for(x = 0; x < v; x++) {
					if(w[x] == m) {
						break;
					}
				}
				if(x == v) {
					w[v] = m;
					v++;
					y++;
				}
			}
		}
	}
	return y;
}


int main(int argc, char *argv[])
{
	char line[256];
	char *s;
	int t = -1;
	int n = 0;

	while((s = fgets(line, sizeof(line), stdin)) != NULL) {
		int A;
		int B;
		int y;

		if(t < 0) {
			t = atoi(line);
			continue;
		}

		sscanf(line, "%d %d", &A, &B);

		y = func(A, B);
		n++;

		printf("Case #%d: %d\n", n, y);

		if(n >= t) {
			break;
		}
	}

	return 0;
}
