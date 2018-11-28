#include <stdio.h>

#define FN "C-large"

FILE* fid;
FILE* fout;


int off[1000001];

static inline int maxx(int v, int w) {
	if (v>w) return v;
	return w;
}

static inline int minn(int v, int w) {
	if (v<w) return v;
	return w;
}

int main(int argc, char** argv) {
	fid = fopen(FN ".in", "r");
	fout = fopen(FN ".out", "w");


	off[0] = 0;
	off[1] = 1;
	off[2] = 2;

	int dlim = 3;
	for (int i=2; i <= 1000000; i++) {
		// we know off[i]

		for ( ; dlim < off[i]+i && dlim <= 1000000; ++dlim) {
			off[dlim] = i;
		}
	}

	//for (int i=0; i < 100; i++) {
		//printf("%d %d\n", i ,off[i]);
	//}


	int T;
	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; ++cas) {
		int A1, A2, B1, B2;
		fscanf(fid, "%d %d %d %d", &A1, &A2, &B1, &B2);

		long long sumlose = 0;

		for (int i=A1; i <= A2; i++) {
			int lowbound = maxx(B1,off[i]);
			int highbound = minn(B2,off[i]+i-1);

			sumlose += (long long)maxx(highbound - lowbound + 1, 0);
		}

		fprintf(fout, "Case #%d: %lld\n",cas, (long long)(A2-A1+1) * (long long)(B2-B1+1) - sumlose);
	}

}
