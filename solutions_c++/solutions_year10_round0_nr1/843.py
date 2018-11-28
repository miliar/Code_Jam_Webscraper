#include <cstdio>


FILE *in, *out;

int main() {
	in = fopen("A-small.in", "r");
	out = fopen("A-small.out", "w");
	int T;
	fscanf(in, "%d", &T);
	for (int i = 1; i <= T; i++) {
		int n, k;
		fscanf(in, "%d %d", &n, &k);
		k++;
		fprintf(out, "Case #%d: ", i);
		if (k % (1 << n))
			fprintf(out, "OFF\n");
		else
			fprintf(out, "ON\n");
	}
	fclose(in);
	fclose(out);
	return 0;
}
