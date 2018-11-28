#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int main() {
	 long long t;
	scanf("%lld\n", &t);
	for ( long long tt = 1; tt <= t; ++tt) {
		 long long n, d;
		scanf("%lld %lld\n", &n, &d);

		 long long pos[n], vend[n];
		for ( long long i = 0; i < n; ++i) {
			scanf("%lld %lld\n", &pos[i], &vend[i]);
		}

		 long long max = 0;

		for ( long long a = 0; a < n; ++a) {
			for ( long long b = a; b < n; ++b) {
				 long long allvend = 0;
				for ( long long i = a; i <= b; ++i) {
					allvend += vend[i];
				}
				 long long spread = pos[b] - pos[a];
				 long long need = (allvend-1) * d;
				 long long miss = need-spread;
				if (miss > max) max = miss;
			}
		}

		printf("Case #%lld: %lld", tt, max/2);
		if (max%2 == 1) printf(".5");
		else printf(".0");
		printf("\n");
	}
}
