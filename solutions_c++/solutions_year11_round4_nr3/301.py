#include <fstream>
#include <string>
using namespace std;
typedef long long ll;

template<typename T>
bool isPrime(T n) { if (n<2) return false;
					for (int i=2; i*i<=n; ++i) if (n%i==0) return false;
					return true; }

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	ll N;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> N;
		if (N==1)
		{
			fout << "Case #" << zz << ": 0" << endl;
			continue;
		}

		ll allPrimes = 0, allPowers = 0;
		for (ll i=2; i<= N; ++i)
		{
			if (isPrime(i))
			{
				++allPrimes;
				ll next = 1;
				while ((next*=i) <= N)
					++allPowers;
			}
		}

		ll result = N==1 ? 0 : (1 + allPowers - allPrimes);
		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}
