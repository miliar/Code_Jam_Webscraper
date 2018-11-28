#include <stdio.h>
#include <string.h>
#include <algorithm>

#define P 16
#define N 1024
#define M 2048

using namespace std;

struct team {
	int m, i;
} T[N];

int G[M];
int p, n;

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		scanf("%d", &p);
		n = 1<<p;
		for (int i = 0; i < n; i++) {
			scanf("%d", &T[i].m);
		}
		for (int i = 0; i < n-1; i++) {
			scanf("%*d");
		}
		for (int i = 0; i < n; i++) {
			T[i].i = 2*n - 2 - i;
		}
		memset(G, 0, sizeof(G));
		for (int i = 0; i < n; i++) {
			int m = p-T[i].m;
			int atual = 0;
			for (int j = (T[i].i-1)/2; ; j = (j-1)/2, atual++) {
				if (atual >= p-m) {
					G[j] = 1;
				}
				if (j == 0) {
					break;
				}
			}
		}
		int c = 0;
		for (int i = 0; i < 2*n; i++) {
			if (G[i]) {
				c++;
			}
		}
		printf("Case #%d: %d\n", test+1, c);
	}
	return 0;
}

