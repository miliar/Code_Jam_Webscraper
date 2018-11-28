#include <cstdio>
#include <algorithm>
using namespace std;

int t, n;
int main() {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("out.txt", "w");

	fscanf(fin, "%d", &t);
	for (int i = 0; i < t; i++) {
		fscanf(fin, "%d", &n);
		int sum = 0, mask = 0, mini = 10000000;
		for (int j = 0; j < n; j++) {
			int a;
			fscanf(fin, "%d", &a);
			sum += a;
			mask ^= a;
			mini = min(mini, a);
		}
		if (mask == 0) {
			fprintf(fout, "Case #%d: %d\n", i+1, sum-mini);
		}
		else fprintf(fout, "Case #%d: NO\n", i+1);
	}

	return 0;
}
