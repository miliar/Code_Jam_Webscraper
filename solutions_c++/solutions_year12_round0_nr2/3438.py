#include <stdio.h>

int min(int a, int b) 
{
	if (a > b)
		return b;
	else 
		return a;
}

int main () {
    FILE *fin  = fopen ("B-large.in", "r");
    FILE *fout = fopen ("test.out", "w");
    
	int cmu, T, n, s, p, t, i, j, m, a;

	fscanf(fin, "%d", &cmu);
	for (T = 1; T <= cmu; T++) {
		fscanf(fin, "%d%d%d", &n, &s, &p);
		j = p * 3;
		m = 0; a = 0;
		for (i = 0; i < n; i++) {
			fscanf(fin, "%d", &t);
			if (t < j - 4) continue;
			if (t >= j - 2) {
				a += 1; continue;
			}
			if ((t == j - 4) && (t >= 2)) {
				m += 1; continue;
			}
			if ((t == j - 3) && (t >= 3)) {
				m += 1; continue;
			}
		}
		fprintf(fout, "Case #%d: %d\n", T, a + min(m, s));
	}

    return 0;
}