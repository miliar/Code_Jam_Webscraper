
// GNU MP Bignum library http://gmplib.org/
#include <gmpxx.h>

#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

void gcd(mpz_class a, mpz_class b, mpz_class & gcd_value)
{
	mpz_gcd(gcd_value.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t());
}

void gcd(std::vector<mpz_class> & sub, size_t begin_pos, size_t l, mpz_class & value)
{
	if (l == 1)	
	{
		value = sub[begin_pos];
		return ;
	}

	mpz_class a, b;

	for (size_t i = begin_pos; i < (l - 1); ++i)
	{
		gcd(sub[i], sub[i + 1], value);
		sub[i + 1] = value;
	}

	value = sub[begin_pos + l - 1];
}

void fair(std::vector<mpz_class> & t, size_t l, mpz_class & value)
{
	mpz_class m, x, r, q;

	m = t[0];

	for (size_t i = 0; i < l - 1; ++i)
	{
		t[i] = t[i + 1] - t[i];
	}

	gcd(t, 0, l - 1, x);

	mpz_cdiv_qr(q.get_mpz_t(), r.get_mpz_t(), m.get_mpz_t(), x.get_mpz_t());
	value = r * (-1);
}

class mpz_less : public std::binary_function<mpz_class const &, mpz_class const &, bool>
{
public:
	bool operator()(mpz_class const & a, mpz_class const & b) const
	{
		return a < b;
	}
};

int main(int argc, char** argv) 
{
	size_t c, n;
	std::string value;
	size_t const maxn = 2000;
	std::vector<mpz_class> t(maxn);

	std::ifstream fin("B-large.in");
	std::ofstream fout("B-large.out");
	
	mpz_class out;

	fin >> c;
	for (size_t i = 0; i < c; ++i)
	{
		fin >> n;		
		for (size_t j = 0; j < n; ++j)
		{
			fin >> value;
			t[j] = value;
		}

		// Sort events
		std::sort(t.begin(), t.begin() + n, mpz_less());

		fair(t, n, out);
		fout << "Case #" << i + 1 << ": " << out << std::endl;
	}

	fin.close();
	fout.close();

    return (0);
}

