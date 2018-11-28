#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
	int len, i, j, k, n, p, q, pos[105], best[105][105];
	
	FILE* in = fopen("bribe.in", "r");
	FILE* out = fopen("bribe.out", "w");
	fscanf(in, "%d", &n);
	for (i = 0; i < n; i++) {
		fscanf(in, "%d %d", &p, &q);
		pos[0] = 0;
		for (j = 1; j <= q; j++) fscanf(in, "%d", &pos[j]);
		
		pos[++q] = p+1;
		pos[q+1] = p+1;
		for (j = 0; j <= q; j++) {
			best[j][0] = 0;
			best[j][1] = 0;
			for (k = 2; k <= q; k++) best[j][k] = INT_MAX;
		}
		
		for (len = 2; len <= q; len++) {
			for (j = 0; j+len <= q; j++) {
				for (k = j+1; k < j+len; k++) {
					best[j][len] = min(best[j][len], best[j][k-j] + best[k][len-(k-j)]);
				}
				best[j][len] += pos[j+len] - pos[j] - 2;
			}
		}
		fprintf(out, "Case #%d: %d\n", (i+1), best[0][q]);
	}
	fclose(in);
	fclose(out);
	return 0;
}

