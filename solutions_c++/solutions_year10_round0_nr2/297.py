// using the GMP library with C++ interface from http://gmplib.org/ from Ubuntu Lucid Lynx

#include <gmpxx.h>

#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	int tests;
	in >> tests;
	for(unsigned test = 1; test <= tests; ++test)
	{
		int n;
		in >> n;
		
		vector<mpz_class> t;
		t.resize(n);
		for(int i = 0; i < n; ++i)
			in >> t[i];

		sort(t.begin(), t.end());

		mpz_class gcd = t[1] - t[0];

		for(int i = 1; i < (n - 1); ++i) {
			mpz_class diff = t[i + 1] - t[i];
			mpz_class new_gcd;
			mpz_gcd (new_gcd.get_mpz_t(), gcd.get_mpz_t(), diff.get_mpz_t());
			gcd = new_gcd;
		}
		
		mpz_class v = -t[0];
		mpz_class x;
		mpz_fdiv_r(x.get_mpz_t(), v.get_mpz_t(), gcd.get_mpz_t());

		cout << "Case #" << test << ": " << x << endl;
	}
	return 0;
}

