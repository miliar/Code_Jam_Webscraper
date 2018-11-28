#include <stdio.h>
#include <algorithm>

FILE* fid;
FILE* fout;

long long a[1000001];

using namespace std;

long long solve() {
	int L, N, C;
	long long t;

	fscanf(fid, "%d %lld %d %d", &L, &t, &N, &C);

	t /= 2LL;

	long long ans = 0;

	for (int i=0; i < C; i++) {
		fscanf(fid, "%lld", &(a[i]));
		ans += a[i];
	}

	for (int i=C; i < N; i++) {
		a[i] = a[i-C];
		ans += a[i];
	}

	ans *= 2;

		//for (int i=0; i < N; i++) {
		//	printf("%lld ", a[i]);
		//}
		//printf(" --> %lld\n", ans);


	long long *sstart, *send;

	send = &(a[N]);
	sstart = send;

	for (int i=0; i < N; i++) {
		t -= a[i];

		if (t < 0) {
			//we've overshot.

			a[i] = -t;

			sstart = &(a[i]);

			break;
		}
	}




	if (sstart != send) {
/*
		for (int i=0; i < N; i++) {
			printf("%s%lld ", (&(a[i]) == sstart)?"[":"", a[i]);
		}
		printf("\n");



		for (int i=0; i < N; i++) {
			printf("%s%lld ", (&(a[i]) == sstart)?"[":"", a[i]);
		}
		printf("\n");*/

		sort(sstart, send);

		int count = send - sstart;

		for (int i=0; i < L && i < count; i++) {
			ans -= send[-i-1];
		}

	}

	return ans;
}

int main(int argc, char** argv) {
	fid = fopen("B-large.in", "r");
	fout = fopen("B.out", "w");

	int T = -1;

	fscanf(fid, "%d\n", &T);

	for (int cas=1; cas <= T ;cas++) {
		fprintf(fout, "Case #%d: %lld\n", cas, solve());

	}
}