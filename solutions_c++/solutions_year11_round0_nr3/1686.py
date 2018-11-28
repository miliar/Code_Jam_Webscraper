#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

FILE* fid;
FILE* fout;

int main(int argc, char** argv) {

	fid = fopen("C-large.in", "r");
	fout = fopen("C.out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int i = 1; i <= T; i++) {

		int N;

		fscanf(fid, "%d", &N);

		int smallest = 1000001;
		int sum = 0;
		int xorsum = 0;

		for (int j = 0; j < N; j++) {
			int val;

			fscanf(fid, "%d", &val);

			smallest = min(smallest, val);
			sum += val;
			xorsum ^= val;
		}


		if (xorsum) {
			fprintf(fout, "Case #%d: NO\n", i);
		} else {
			fprintf(fout, "Case #%d: %d\n", i, sum - smallest);
		}


	}

	return 0;
}