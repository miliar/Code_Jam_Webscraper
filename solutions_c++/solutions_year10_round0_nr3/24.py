#include <stdio.h>
#include <stdlib.h>

#define FN "C-large"

FILE* fid;
FILE* fout;



int g[1000];

int adv[1000];
int prof[1000];


long long solve() {
//	int N, K;
//			fscanf(fid, "%d %d", &N, &K);

	//printf("\n\n");

	int R, k, N;
	fscanf(fid, "%d %d %d", &R, &k, &N);

	long long sum = 0;

	for (int i=0; i < N; i++) {
		fscanf(fid, "%d", g+i);
		//printf("g: %d\n", g[i]);
		sum += (long long)g[i];
	}

	// sort-of-special case
	if (sum < (long long)k) return (long long)R * sum;

	// precalc
	for (int i=0; i < N; i++) {
		int pprof = 0;
		for (int padv = 0; ; padv++) {
			if (padv > N) {
				printf("BAAAAD\n");
				//exit(0);
			}

			int npprof = pprof + g[(i+padv)%N];

			//printf("  %d > %d ?\n", npprof, k);

			if (npprof > k) {
				adv[i] = padv;
				prof[i] = pprof;

				//printf("%d: +%d  $%d\n", g[i], adv[i], prof[i]);
				break;
			}

			pprof = npprof;
		}
	}

	// etc
	sum = 0;
	int pos = 0;

	for (int i=0; i < R; i++) {
		//printf("++%d\n", prof[pos]);
		sum += (long long)prof[pos];
		pos = (pos + adv[pos]) % N;
	}

	return sum;
}


int main(int argc, char** argv) {
	fid = fopen(FN ".in", "r");
	fout = fopen(FN ".out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int cas = 1; cas <= T; ++cas) {

		fprintf(fout, "Case #%d: %lld\n", cas, solve());
	}

}

