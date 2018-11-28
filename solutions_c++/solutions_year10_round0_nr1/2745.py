#include <stdio.h>

int pow2(int n) {
	int a = 1;
	while(n--) a *= 2;
	return a;
}

int main(void) {
	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt", "w");

	int T;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++) {
		int N, K, tmp;
		fscanf(fin, "%d%d", &N, &K);
		tmp = pow2(N);
		fprintf(fout, "Case #%d: O", t);
		if(K % tmp == tmp - 1) fprintf(fout, "N");
		else fprintf(fout, "FF");
		fprintf(fout, "\n");
	}

	fclose(fout);
	fclose(fin);
	return 0;
}