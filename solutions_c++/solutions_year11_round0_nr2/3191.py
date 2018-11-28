#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int t, c, d, n;
char comb[150][150];
bool oppose[150][150];
char q[150];
int s, e;
int main() {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B.out", "w");

	fscanf(fin, "%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		memset(comb, 0, sizeof(comb));
		memset(oppose, 0, sizeof(oppose));
		s = e = 0;

		fscanf(fin, "%d", &c);
		for (int i = 0; i < c; i++) {
			char a, b, x;
			fscanf(fin, " %c%c%c", &a, &b, &x);
			comb[a][b] = comb[b][a] = x;
		}
		fscanf(fin, "%d", &d);
		for (int i = 0; i < d; i++) {
			char a, b, x;
			fscanf(fin, " %c%c", &a, &b);
			oppose[a][b] = oppose[b][a] = true;
		}
		fscanf(fin, "%d ", &n);
		for (int i = 0; i < n; i++) {
			char x;
			fscanf(fin, "%c", &x);
			q[e++] = x;
			while (s+1 < e && comb[q[e-1]][q[e-2]] > 0) {
				q[e-2] = comb[q[e-1]][q[e-2]];
				e--;
			}
			for (int j = s; j < e-1; j++)
				if (oppose[q[j]][q[e-1]]) e = s;
		}
		fprintf(fout, "Case #%d: [", cas);
		if (s < e) {
			fprintf(fout, "%c", q[s]);
			for (int i = s+1; i < e; i++)
				fprintf(fout, ", %c", q[i]);
		}
		fprintf(fout, "]\n");
	}

	return 0;
}
