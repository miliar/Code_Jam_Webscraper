#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>


int main() {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t, n, s, p;
	int k, score, above, surabove;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		fscanf(fin, "%d%d%d", &n, &s, &p);
		above = 0;
		surabove = 0;
		for (int j = 0; j < n; ++j) {
			fscanf(fin, "%d", &score);
			k = score / 3;
			switch (score % 3) {
			case 0:
				if (k >= p) ++above;
				else if (k + 1 >= p && k - 1 >= 0) ++surabove;
				break;
			case 1:
				if (k + 1 >= p) ++above;
				break;
			case 2:
				if (k + 1 >= p) ++above;
				else if (k + 2 >= p) ++surabove;
				break;
			}
		}
		if (surabove > s) surabove = s;
		fprintf(fout, "%d\n", above + surabove);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
