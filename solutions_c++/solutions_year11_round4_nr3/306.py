#include <cstdio>

using namespace std;

bool isP[1000005];
const int N1 = 1000000;

int P[1000000]; int Pn;

void solve(long long N) {
	if (N == 1) { printf("0\n"); return; }

	long long ans = 0;
	for (int i = 0; i < Pn; i++) {
		long long a = 0;
		for (int j = N; j; ) {
			long long k = j / P[i];
			a ++;
			j = k;
		}
		a --;

		if (a) ans += a - 1;
	}

	printf("%lld\n", ans + 1);
}

void calcP() {
	for (int i = 1; i <= N1; i++) isP[i] = true;

	isP[1] = false;
	for (int i = 2; i <= N1; i++)
		if (isP[i]) {
			for (int j = i + i; j <= N1; j += i) isP[j] = false;
		}

	Pn = 0;
	for (int i = 2; i <= N1; i++)
		if (isP[i])
			P[Pn++] = i;
}

int main() {
	calcP();

	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		long long N; scanf("%lld", &N);
		printf("Case #%d: ", i);
		solve(N);
	}

	return 0;
}
