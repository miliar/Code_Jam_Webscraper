// run in parallel on 8 cores - added one parameter 'from' to correctly print case number
// program to split input into 8 files
/*
#include <stdio.h>
#include <string.h>

int main() {
	int cores = 8, t, i;
	scanf("%d%*c", &t);
	for (i = 0; i < t; i++) {
		FILE *fout;
		char s[100];
		sprintf(s, "Bsmall_part%d.in", i/ (t / cores + 1));
		if ((i-1) / (t / cores + 1) != i / (t / cores + 1) || i == 0) {
			fout = fopen(s, "wt");
			fprintf(fout, "%d\n", i);
		} else fout = fopen(s, "at");

		fgets(s, 100, stdin);
		fprintf(fout, "%s", s);
		fclose(fout);
	}
	return 0;
}
*/ 
#include <stdio.h>
#include <algorithm>
using namespace std;

int i, j, t, tt, n, k, r;
int g[1001];
int z[1001], p[1001]; // kolko zarobim a o kolko sa posuniem, ked zacnem z toho miesta

int main() {
	int from;
	scanf("%d", &from);
	for (int tt = 1; scanf("%d", &n) == 1; tt++) {
		printf("Case #%d: ", tt + from);
		
		for (i = 0; i < n; i++) scanf("%d", &g[i]);
		k = g[i]; for (i = 1; i < n; i++) if (k < g[i]) k = g[i];
		int m = 0;
		int res = -1;
		for (j = 0; j <= k; j++) {
			r = __gcd(g[0]+j, g[1] + j);
			for (i = 2; i < n; i++) r = __gcd(r, g[2] + j);
			if (r > m) {
				res = j;
				m = r;
			}
		}
		printf("%d\n", res);
		fprintf(stderr, "%d\n", res);
	}
	return 0;
}
