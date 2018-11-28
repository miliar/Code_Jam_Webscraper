// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

char comp[1000001];
int primes[400000];

long long modexp(long long a, int e, long long p) {
	if (e == 0)
		return 1;
	long long t = modexp(a, e/2, p);
	t = (t * t) % p;
	if (e & 1)
		t = (t * a) % p;
	return t;
}

int v[100];

int main() {
	int tc;
	scanf("%d", &tc);
	int l = 0;
	for (int p=2; p<1000000; ++p)
		if (!comp[p]) {
			if (p < 1000)
				for (int j=p*p; j<1000000; j+=p)
					comp[j] = 1;
			primes[l++] = p;
		}
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int d, k;
		scanf("%d %d", &d, &k);
		int maxv = 0;
		for (int i=0; i<k; ++i) {
			scanf("%d", &v[i]);
			assert(v[i] >= 0);
			maxv = max(maxv, v[i]);
		}
		if (k == 2) {
			if (v[0] == v[1])
				printf("%d\n", v[0]);
			else
				puts("I don't know.");
			continue;
		}
		int N = 1;
		for (int i=0; i<d; ++i)
			N *= 10;
		int next = -1;
		for (int i=0; i<l && primes[i] <= N; ++i) {
			int p = primes[i];
			if (p <= maxv)
				continue;
			long long a = -1, b;
			bool valid = true;
			for (int i=1; i+1<k; ++i) {
				int d2 = ((v[i] - v[i-1]) % p + p) % p;
				int d1 = ((v[i+1] - v[i]) % p + p) % p;
				if (!d2) {
					if (d1) {
						valid = false;
						break;
					}
				}
				long long ta = (modexp(d2, p-2, p) * d1) % p;
				if (a < 0)
					a = ta;
				else if (ta != a) {
					valid = false;
					break;
				}
				b = ((v[i] - v[i-1] * a) % p + p) % p;
			}
			if (!valid || a == -1)
				continue;
	//		printf("p = %d, a = %lld\n", p, a);
			int tnext = (((long long)v[k-1]) * a + b) % p;
			if (next < 0)
				next = tnext;
			else if (tnext != next) {
	//			printf("next = %d tnext = %d\n", next, tnext);
				next = -1;
				break;
			}
		}
		if (next >= 0)
			printf("%d\n", next);
		else
			puts("I don't know.");
	}
	return 0;
}
