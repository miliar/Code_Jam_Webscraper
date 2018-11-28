#include <cstdio>
#include <cstring>
int nr, nc, b[105][105], h[105][105], n;
int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

int solve(int r, int c) {
	int d, minr = r, minc = c, tr, tc;
	
	if (b[r][c] > 0) return b[r][c];
	
	for (d = 0; d < 4; d++) {
		tr = r + dr[d];
		tc = c + dc[d];
		if (tr < nr && tr >= 0 && tc < nc && tc >= 0 && h[tr][tc] < h[minr][minc]) {
			minr = tr;
			minc = tc;
		}
	}
	if (minr == r && minc == c) return (b[r][c] = ++n);
	else return (b[r][c] = solve(minr, minc));
}

int main() {
	int r, c, t, nt;
	FILE* in = fopen("water.in", "r");
	FILE* out = fopen("water.out", "w");
	fscanf(in, "%d", &nt);
	for (t = 0; t < nt; t++) {
		n = 0;
		memset(b, 0, sizeof(b));
		fprintf(out, "Case #%d:\n", (t+1));
		fscanf(in, "%d %d", &nr, &nc);
		for (r = 0; r < nr; r++) for (c = 0; c < nc; c++) fscanf(in, "%d", &h[r][c]);
		for (r = 0; r < nr; r++) {
			for (c = 0; c < nc; c++) {
				solve(r, c);
				fprintf(out, c ? " %c" : "%c", b[r][c] + 'a' - 1);
			}
			fprintf(out, "\n");
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}
