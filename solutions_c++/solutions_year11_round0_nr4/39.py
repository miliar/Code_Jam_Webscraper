#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	FILE *f = fopen("D.in", "r");
	FILE *fout = fopen("D.out", "w");

	int test; fscanf(f, "%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		int n; fscanf(f, "%d", &n);
		int order = 0;
		for (int i = 1; i <= n; i++) {
			int a; fscanf(f, "%d", &a);
			if (a != i) order++;
		}

		fprintf(fout, "Case #%d: %d\n",tt, order);
	}

	fclose(f);
	fclose(fout);

	return 0;
}
