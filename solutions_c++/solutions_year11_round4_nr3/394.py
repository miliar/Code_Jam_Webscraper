#define _USE_MATH_DEFINES

#include <iostream>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <queue>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("alignment.in" , "r", stdin);
	freopen("alignment.out" , "w", stdout);

	int t;
	cin >> t;
	vector<char> prime (1000001, true);
	prime[0] = prime[1] = false;
	for (long long i=2; i<1000001; ++i)
		if (prime[i])
			for (long long j=i*i; j<1000001; j+=i)
				prime[j] = false;
	vector<long long> primes;
	for (int i=2; i<1000001; ++i)
		if (prime[i])
			primes.push_back(i);
	for (int test = 0; test < t; ++test) {
		long long n, ans = 0;
		cin >> n;
		if (n > 1) {
			int i = 0;
			while (i < primes.size() && primes[i] * primes[i] <= n) {
				int k = 0;
				long long a = 1;
				while (a * primes[i] <= n) {
					++k;
					a *= primes[i];
				}
				ans += k - 1;
				++i;
			}
		} else ans = -1;
		cout << "Case #" << test + 1 << ": " << ans + 1 << '\n';
	}

	return 0;
}
