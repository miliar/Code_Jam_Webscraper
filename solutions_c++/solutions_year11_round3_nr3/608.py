#include <stdio.h>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX_PLAYERS (10002)

long long freqs[MAX_PLAYERS];

int gcd(long long a, long long b) {
	return b ? gcd(b, a % b) : a;
}

int main() {
	int ntc, tc;
	long long i, j;
	long long k, m, n;
	long long L, N, H;
	scanf("%d", &ntc);
	for (tc = 1; tc <= ntc; tc++) {
		scanf("%lld %lld %lld", &N, &L, &H);
		freqs[0] = 1;
		for (i = 1; i <= N; i++) {
			scanf("%lld", &freqs[i]);
		}
		sort(freqs, freqs+N);

		bool found = false;
		for (i = L; !found && i <= H; i++) {
			found = true;
			for (j = 0; found && j <= N; j++) {
				if (i % freqs[j] != 0 && freqs[j] % i != 0) {
					found = false;
					break;
				}
			}
			if (found) break;
		}
		if (found) printf("Case #%d: %lld\n", tc, i);
		else printf("Case #%d: NO\n", tc);
		fflush(stdout);
		continue;
		/*for (i = 0; i < N; i++) {
			if (freqs[i+1] <= L) continue;
			if (freqs[i] > H) break;
			if (L <= freqs[i] && freqs[i+1] <= H) {
				for (
			}
			if (freqs[i] < L) {
			}
		}*/


	}
	return 0;
}

