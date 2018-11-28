#include <iostream>
#include <gmp.h>
#include <gmpxx.h>
#define maxN 10000

using std::cin;
using std::cout;
using std::endl;

int N;
mpz_class a[maxN];

mpz_class
gcd(mpz_class a, mpz_class b)
{
	return(b == 0? a: gcd(b, a % b));
}

int
main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		cin >> N;
		int i;
		for (i = 0; i < N; i++)
			cin >> a[i];
		mpz_class q = abs(a[1] - a[0]);
		for (i = 2; i < N; i++)
			q = gcd(q, abs(a[i] - a[i - 1]));
		cout << "Case #" << z << ": " << (q - a[0] % q) % q << endl;
	}
	return(0);
}
