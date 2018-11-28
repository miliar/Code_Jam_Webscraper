#include <cstdio>
#include <vector>

const long MaxP = 1000001;
bool notprime[MaxP];
long prime[MaxP], primeN;

void calcPrime()
{
	for (long i = 3; i * i < MaxP; i += 2)
		for (long k = i * i; k < MaxP; k += i)
			notprime[k] = true;
	prime[primeN ++] = 2;
	for (long i = 3; i < MaxP; i += 2)
		if (!notprime[i]) prime[primeN ++] = i;
}

long solve()
{
	long n, result = 0;
	scanf("%ld", &n);
	for (long i = 0; i < primeN && prime[i] * prime[i] <= n; ++ i) {
		long pow = 0, product = prime[i];
		while (product * prime[i] <= n) {
			++ pow;
			product *= prime[i];
		}
		result += pow;
	}
	return n > 1 ? result + 1 : 0;
}

int main()
{
	calcPrime();
	long testCases;
	scanf("%ld", &testCases);
	for (long t = 1; t <= testCases; ++ t)
		printf("Case #%ld: %ld\n", t, solve());
	return 0;
}
