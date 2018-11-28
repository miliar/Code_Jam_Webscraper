#include <cstdio>
#include <cstdlib>

using namespace std;

#define IN_FILE "A-large.in"
#define OUT_FILE "A-large.out"

int main() {
	FILE *fpIn = fopen(IN_FILE, "r");
	if (fpIn == NULL) {
		printf("Failed to call fopen()\n");
		return -1;
	}
	FILE *fpOut = fopen(OUT_FILE, "w");
	if (fpIn == NULL) {
		printf("Failed to call fopen()\n");
		return -1;
	}

	int T;
	fscanf(fpIn, "%d", &T);
	// dbg
	printf("T = %d\n", T);
	// dbg end
	
	for (int cnt1 = 0; cnt1 < T; cnt1++) {
		unsigned long long N, K;
		fscanf(fpIn, "%llu %llu", &N, &K);
		// dbg
		printf("N = %llu, K = %llu\n", N, K);
		// dbg end
		unsigned long long 	mi = 1;
		for (int i = 0; i < N; i++)
			mi = mi * 2;
		unsigned long long res = K % mi;
		// dbg
		printf("mi = %llu, res = %llu\n", mi, res);
		// dbg end
		if (res == (mi-1))
			fprintf(fpOut, "Case #%d: ON\n", cnt1+1);
		else
			fprintf(fpOut, "Case #%d: OFF\n", cnt1+1);
	}

	fclose(fpIn);
	fclose(fpIn);

	return 0;
}