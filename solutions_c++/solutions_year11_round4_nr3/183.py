#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a) 


#define SIEVE_MAX 1000100
#define ISPRIME(n) (!(__sieve[(n)>>4] & (1<<(((n)>>1)&7))))
unsigned char __sieve[ (SIEVE_MAX>>4) + 47 ];
vector <long long> primes;

void init_sieve()
{
	memset(__sieve, 0, sizeof(__sieve));
    int smax = (int)(3 + sqrt(double(SIEVE_MAX)));
	for(int i=3; i<=smax; i+=2) if(ISPRIME(i)) { int j=i*i; while(j<SIEVE_MAX){ __sieve[j>>4]|=(1<<((j>>1)&7)); j+=i<<1; } }
	primes.resize(1,2); for (int i=3; i<SIEVE_MAX; i+=2) if (ISPRIME(i)) primes.push_back(i);
}


int main() 
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int tc, ix, po;
	long long n, res, tmp;

	init_sieve();

	fin >> tc;

	REP(tcase,tc) {
		fin >> n;

		res = 1; ix = 0;

		while (primes[ix]*primes[ix] <= n) {
			tmp = primes[ix]; po = 1;
			while (tmp*primes[ix] <= n) { tmp *= primes[ix]; ++po; }
			res += po-1;
			++ix;
		}

		if (n == 1) res = 0;

		fout << "Case #" << tcase+1 << ": " << res << endl;
		cout << tcase+1 << " / " << tc << endl;
	}

	fout.close();

	return 0;
}