#include <stdio.h>

#define FN "A-large"

FILE* fid;
FILE* fout;

int main(int argc, char** argv) {
	fid = fopen(FN ".in", "r");
	fout = fopen(FN ".out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; ++cas) {
		unsigned int N, K;
		fscanf(fid, "%u %u", &N, &K);

		fprintf(fout, "Case #%d: O%s\n", cas, ((K-((1<<N)-1))&((1<<N)-1))?"FF":"N");
	}

}
