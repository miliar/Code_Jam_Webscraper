#include <vector>
#include <algorithm>

#include <cstdio>

using namespace std;

#define MAXP 1000000

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

const int maxp[7] = {1, 10, 100, 1000, 10000, 100000, 1000000};

typedef long long llint;

int modinv(int a, int p)
{
	int x = a % p;
	int y = p;
	int i = 1;
	int j = 0;
	while (y != 0)
	{
		int z = x % y;
		int k = (int)((i + (llint)(p - x / y) * j) % p);
		x = y;
		y = z;
		i = j;
		j = k;
	}
	return i;
}

int main()
{
	int T;
	scanf("%d", &T);
	vector<bool> isPrime(MAXP + 1, true);
	isPrime[0] = isPrime[1] = false;
	for (int i = 2; i * i <= MAXP; ++i)
	{
		if (!isPrime[i])
			continue;
		for (int j = i * 2; j <= MAXP; j += i)
			isPrime[j] = false;
	}
	vector<int> primes;
	for (int i = 2; i <= MAXP; ++i)
	{
		if (isPrime[i])
			primes.push_back(i);
	}
	for (int idxCase = 0; idxCase < T; ++idxCase)
	{
		int D, K;
		scanf("%d%d", &D, &K);
		vector<int> x(K);
		for (int i = 0; i < K; ++i)
			scanf("%d", &x[i]);
		int maxx = 0;
		ITERATE (it, x)
			maxx = max(maxx, *it);
		bool ambiguous = false;
		int ans = -1;
		if (K == 1)
			ambiguous = true;
		else if (x[0] == x[1])
			ans = x[0];
		else if (K == 2)
			ambiguous = true;
		else
		{
			ITERATE (it, primes)
			{
				int p = *it;
				if (p > maxp[D])
					break;
				if (p <= maxx)
					continue;
				int a = (int)(((llint)((x[2] - x[1] + p) % p) * modinv((x[1] - x[0] + p) % p, p)) % p);
				int b = (int)((x[1] + (llint)(p - a) * x[0]) % p);
				// printf(" %d %d %d\n", p, a, b);
				bool found = true;
				for (int i = 1; i < K - 1; ++i)
				{
					if (x[i + 1] != (int)(((llint)a * x[i] + b) % p))
					{
						found = false;
						break;
					}
				}
				if (found)
				{
					int ans1 = (int)(((llint)a * x[K - 1] + b) % p);
					if (ans < 0)
						ans = ans1;
					else if (ans != ans1)
					{
						ambiguous = true;
						break;
					}
				}
			}
		}
    	printf("Case #%d: ", idxCase + 1);
		if (ambiguous)
			puts("I don't know.");
		else
			printf("%d\n", ans);
	}
	return 0;
}
