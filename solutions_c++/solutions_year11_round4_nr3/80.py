#include <cstdio>
#include <cmath>
#include <cassert>

namespace Solve
{
	const int PRIME_RANGE = 1000005,
		  NPRIME_MAX = PRIME_RANGE / 10;
	typedef long long int Bignum_t;
	int prime[NPRIME_MAX], nprime;
	void init_prime();

	Bignum_t work(Bignum_t n);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	init_prime();
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		Bignum_t n;
		fscanf(fin, "%lld", &n);
		fprintf(fout, "Case #%d: %lld\n", casenu, work(n));
	}
}

Solve::Bignum_t Solve::work(Bignum_t n)
{
	if (n == 1)
		return 0;
	int ans = 1;
	for (int i = 0; i < nprime; i ++)
	{
		int l = 0, p = prime[i];
		for (Bignum_t j = n; j >= p; j /= p, l ++);
		if (l == 1)
			return ans;
		ans += l - 1;
	}
	return ans;
}

void Solve::init_prime()
{
	static bool is_comp[PRIME_RANGE];
	int imax = sqrt((double)PRIME_RANGE);
	for (int i = 2; i < PRIME_RANGE; i ++)
		if (!is_comp[i])
		{
			prime[nprime ++] = i;
			assert(nprime < NPRIME_MAX);
			if (i <= imax)
				for (int j = i * i; j < PRIME_RANGE; j += i)
					is_comp[j] = true;
		}
}

int main()
{
	Solve::solve(stdin, stdout);
}

