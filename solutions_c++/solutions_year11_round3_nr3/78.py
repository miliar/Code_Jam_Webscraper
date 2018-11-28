#include <stdio.h>
#include <algorithm>

FILE* fid;
FILE* fout;

long long a[10001];

using namespace std;

void solve() {
	int N;
	long long L, H;

	fscanf(fid, "%d %lld %lld ", &N, &L, &H);

	for (int i=0; i < N; i++) {
		fscanf(fid, "%lld", a+i);
	}


	long long x = L;

	for (;;) {

		int dirty = 0;

		for (int i=0; i < N; i++) {
			if (x > a[i]) {
				if (x % a[i] != 0) {
					dirty = 1;

					x = x - (x % a[i]) + a[i];

					if (x > H) {
						fprintf(fout, "NO\n");
						return;
					}
				}
			}
		}

		if (dirty) continue;

		for (int i=0; i < N; i++) {
			if (x < a[i]) {

				if (a[i] % x != 0) {
					dirty = 1;

					long long best = a[i];

					for (long long j = 1; j * j <= a[i]; j++) {

						if (a[i] % j) continue;

						if (j > x) {
							best = j;
							break;
						}

						if (a[i]/j > x) {
							best = a[i]/j;
						}
					}

					x = best;

					if (x > H) {
						fprintf(fout, "NO\n");
						return;
					}

				}

			}

		}

		if (dirty) continue;

		break;
	}

	fprintf(fout, "%lld\n", x);
	return;
}

int main(int argc, char** argv) {
	fid = fopen("C-small-attempt1.in", "r");
	fout = fopen("C.out", "w");

	int T = -1;

	fscanf(fid, "%d\n", &T);

	for (int cas=1; cas <= T ;cas++) {
		fprintf(fout, "Case #%d: ", cas);
		solve();

	}
}