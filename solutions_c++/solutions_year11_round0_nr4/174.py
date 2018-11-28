#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>

int n, a[1000], b[1000];

int cmp(const void *a, const void *b) {
	return *(int *) a - *(int *) b;
}

int main() {
	FILE *fin = fopen("in.txt", "r");
	FILE *fout = fopen("out.txt", "w");
	int t, ans;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		fscanf(fin, "%d", &n);
		for (int j = 0; j < n; ++j) {
			fscanf(fin, "%d", a + j);
			b[j] = a[j];
		}
		qsort(b, n, sizeof (int), cmp);
		ans = 0;
		for (int j = 0; j < n; ++j)
			if (a[j] != b[j]) ++ans;
		fprintf(fout, "%d\n", ans);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
