#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>

int main() {
	FILE *fin = fopen("C-small-attempt0.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t, n, c, ans, sum, min;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		ans = 0;
		sum = 0;
		min = 9999999;
		fscanf(fin, "%d", &n);
		for (int j = 0; j < n; ++j) {
			fscanf(fin, "%d", &c);
			ans ^= c;
			sum += c;
			if (min > c) min = c;
		}
		if (ans == 0) fprintf(fout, "%d\n", sum - min);
		else fprintf(fout, "NO\n");
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
