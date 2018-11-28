#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

const int MaxN = 1000;

int n;
int a[MaxN];


int main() {
	FILE *f = fopen("C.in", "r");
	FILE *fout = fopen("C.out", "w");

	int test; fscanf(f, "%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		fscanf(f, "%d", &n);
		int tot = 0;
		int mina = 1000001;
		int sum = 0;
		for (int i = 0; i < n; i++){
			fscanf(f, "%d", &a[i]);
			tot ^= a[i];
			if (a[i] < mina) mina = a[i];
			sum += a[i];
		}

		if (tot != 0) fprintf(fout, "Case #%d: NO\n", tt);
		else {
			fprintf(fout, "Case #%d: %d\n", tt, sum - mina);
		}
	}

	fclose(f);
	fclose(fout);

	return 0;
}

