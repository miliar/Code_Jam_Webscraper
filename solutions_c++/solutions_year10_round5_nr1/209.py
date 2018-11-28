#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define CODE A-small-attempt1

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXP 1000000

typedef vector<int> vi;

bool isPrime[MAXP];
vi primes;

void sieve() {
	fill(isPrime, isPrime + MAXP, true);
	isPrime[0] = isPrime[1] = false;
	for (int i = 2; i < MAXP; ++i) if (isPrime[i]) {
		primes.push_back(i);
		for (int j = 2 * i; j < MAXP; j += i)
			isPrime[j] = false;
	}
}

int mod(long long a, int p) {
	a %= p;
	if (a < 0)
		a += p;
	return a;
}

int solve() {
	int d, kn;
	scanf("%d %d", &d, &kn);
	int k[11];
	for (int i = 0; i < kn; ++i) {
		scanf("%d", &k[i]);
	}
	if (kn == 1)
		return -1;
	int dd = 1;
	for (int i = 0; i < d; ++i)
		dd *= 10;
	int res = -1;
	for (int i = 0; i < (int)primes.size() && primes[i] <= dd; ++i) {
		int p = primes[i];
		bool gg = true;
		for (int j = 0; j < kn && gg; ++j)
			if (k[j] >= p)
				gg = false;
		if (!gg)
			continue;
		for (int a = 0; a < p; ++a) {
			int b = mod(k[1] - (long long) a * k[0], p);
			bool g = true;
			for (int i = 2; i < kn && g; ++i) {
				if (mod((long long) k[i-1] * a + b, p) != k[i])
					g = false;
			}
			if (g) {
				int n = mod((long long) k[kn-1] * a + b, p);
				if (res < 0)
					res = n;
				else if (res != n)
					return -1;
			}
		}
	}
	return res;
}

int main() {
	sieve();
	//printf("%d\n", primes.size());
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: ", i);
		int r = solve();
		if (r < 0)
			printf("I don't know.\n");
		else
			printf("%d\n", r);
	}
	return 0;
}
