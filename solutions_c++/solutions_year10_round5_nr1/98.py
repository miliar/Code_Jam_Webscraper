/*
 * $File: a.cpp
 * $Date: Sat Jun 12 22:32:33 2010 +0800
 */

#include <cstdio>
#include <cassert>

namespace Solve
{
	const int PRIME_MAX = 1000005, NPRIME_MAX = 1000000,
		  SEQLEN_MAX = 15;
	typedef long long int Bignum;
	int prime[NPRIME_MAX], nprime;
	void init_prime(int n);

	int seq[SEQLEN_MAX], seqlen;
	int get_next(int p);

	inline int mod(Bignum a, int m)
	{return a >= 0 ? a % m : ((m - ((-a) % m)) % m);}
	Bignum pow_mod(int a, int n, int m);

	int work(int d);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	init_prime(PRIME_MAX);
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		int d;
		fscanf(fin, "%d%d", &d, &seqlen);
		for (int i = 0; i < seqlen; i ++)
			fscanf(fin, "%d", &seq[i]);
		int ans = work(d);
		if (ans == -1)
			fprintf(fout, "Case #%d: I don't know.\n", id);
		else fprintf(fout, "Case #%d: %d\n", id, ans);
	}
}

int Solve::work(int d)
{
	if (seqlen < 2)
		return -1;
	int max = 1;
	for (int i = 1; i <= d; i ++)
		max *= 10;
	int ans = -1;
	int max_ele = -1;
	for (int i = 0; i < seqlen; i ++)
		if (seq[i] > max_ele)
			max_ele = seq[i];
	for (int i = 0; i < nprime && prime[i] <= max; i ++)
		if (prime[i] > max_ele)
		{
			int tmp = get_next(prime[i]);
			if (ans == -1)
				ans = tmp;
			else if (tmp != -1 && ans != tmp)
				return -1;
		}
	return ans;
}

Solve::Bignum Solve::pow_mod(int a, int n, int m)
{
	a = mod(a, m);
	Bignum ans = 1, cur = a;
	while (n)
	{
		if (n & 1)
		{
			ans *= cur;
			if (ans >= m)
				ans %= m;
		}
		n >>= 1;
		cur *= cur;
		if (cur >= m)
			cur %= m;
	}
	return ans;
}

int Solve::get_next(int p)
{
	if (seqlen == 2)
	{
		if (seq[0] == seq[1])
			return seq[0];
		return -1;
	}
	Bignum a = pow_mod(seq[1] - seq[0], p - 2, p) * (seq[2] - seq[1]);
	a = mod(a, p);
	int b = mod(seq[1] - a * seq[0], p);
	assert((a * seq[0] + b) % p == seq[1]);
	assert((a * seq[1] + b) % p == seq[2]);
	for (int i = 3; i < seqlen; i ++)
		if ((a * seq[i - 1] + b) % p != seq[i])
			return -1;
	return (a * seq[seqlen - 1] + b) % p;
}

void Solve::init_prime(int n)
{
	static bool notp[PRIME_MAX + 1];
	for (int i = 2; i <= n; i ++)
		if (!notp[i])
		{
			prime[nprime ++] = i;
			for (int j = i << 1; j <= n; j += i)
				notp[j] = true;
		}
}

int main()
{
	Solve::solve(stdin, stdout);
}

