#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 1

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;


int main()
{
#ifndef ONLINE_JUDGE
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		ll n;
		scanf("%lld", &n);
		int ans;
		if (n == 1)
			ans = 0;
		else
		{	
			int _max = 1;
			int _min = 0;
			vector <ll> primes;

			ll k = 2;
			while (k * k <= n)
			{
				int j = 0;
				while (j < int(primes.size()) && primes[j] * primes[j] <= k && k % primes[j] != 0)
					++j;
				if (j >= int(primes.size()) || primes[j] * primes[j] > k)
				{
					primes.push_back(k);
					_min++;
					ll k0 = k;
					while (k0 <= n)
					{
						++_max;
						k0 *= k;
					}
					//dbg("%lld %lld\n", k, k0 / k);
				}
				++k;
			}
			ans = _max - _min;
		}
		printf("Case #%d: %d\n", ii, ans);
	}

	return 0;
}
