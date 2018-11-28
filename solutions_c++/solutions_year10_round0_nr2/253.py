/*
 * $File: fair_warning.cpp
 * $Date: Sun May 09 00:13:50 2010 +0800
 *
 * GNU MP library is used in this program.
 *
 * Compiling Options:
 *   g++ % -o %:r -O2 -Wall -lgmp
 */
#include <cstdio>
#include <gmp.h>
#include <cassert>

namespace Solve
{
	const int NNUM_MAX = 1005, NUMLEN_MAX = 55;
	mpz_t num[NNUM_MAX], delta[NNUM_MAX];
	int nnum;

	void init(FILE *fin);
	void free();

	inline int gcd(int a, int b)
	{
		while (b)
		{
			int x = a % b;
			a = b;
			b = x;
		}
		return a;
	}

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int c;
	fscanf(fin, "%d", &c);
	int id = 0;
	while (c --)
	{
		id ++;
		init(fin);
		mpz_t t, tmp1, tmp2, y;
		mpz_inits(t, tmp1, tmp2, y, NULL);
		for (int i = 1; i < nnum; i ++)
		{
			mpz_sub(tmp1, num[0], num[i]);
			if (mpz_cmp_si(tmp1, 0))
			{
				if (mpz_cmp_si(t, 0) == 0)
				{
					if (mpz_sgn(tmp1) > 0)
						mpz_set(t, tmp1);
					else mpz_neg(t, tmp1);
				}
				else
				{
					mpz_gcd(tmp2, t, tmp1);
					mpz_set(t, tmp2);
				}
			}
		}
		for (int i = 0; i < nnum; i ++)
		{
			mpz_mod(tmp1, num[i], t);
			if (mpz_sgn(tmp1) > 0)
			{
				mpz_sub(tmp2, t, tmp1);
				if (mpz_cmp(tmp2, y) > 0)
					mpz_set(y, tmp2);
			}
		}
		gmp_fprintf(fout, "Case #%d: %Zd\n", id, y);
		/*
		for (int i = 0; i < nnum; i ++)
		{
			mpz_add(tmp1, num[i], y);
			mpz_mod(tmp2, tmp1, t);
			assert(mpz_cmp_si(tmp2, 0) == 0);
		}
		int ti = mpz_get_si(t), yi = mpz_get_si(y);
		printf("Checking %d:\n", id);
		int x[3], min = 1 << 30;
		for (int i = 0; i < nnum; i ++)
		{
			x[i] = mpz_get_si(num[i]);
			if (x[i] < min)
				min = x[i];
		}
		for (int i = 0; i <= min; i ++)
		{
			int t1 = gcd(x[0] + i, x[1] + i);
			for (int j = 2; j < nnum; j ++)
				t1 = gcd(t1, x[j] + i);
			assert(t1 < ti || (t1 == ti && i >= yi));
		}
		*/
		mpz_clears(t, tmp1, tmp2, y, NULL);
		free();
	}
}

void Solve::init(FILE *fin)
{
	fscanf(fin, "%d", &nnum);
	char tmp[NUMLEN_MAX];
	for (int i = 0; i < nnum; i ++)
	{
		fscanf(fin, "%s", tmp);
		mpz_init_set_str(num[i], tmp, 10);
	}
}

void Solve::free()
{
	for (int i = 0; i < nnum; i ++)
		mpz_clear(num[i]);
}

int main()
{
	Solve::solve(stdin, stdout);
}

