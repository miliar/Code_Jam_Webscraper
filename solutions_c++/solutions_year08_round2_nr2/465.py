#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void prim(vector<long long> &v, long long p, long long i2)
{
	long long	i, sq, j;
	bool		isp = true;

	if (p <= 2)
		v.push_back(2);

	if (p%2 == 0)
		p++;

	for (i=p;i<i2;i+=2)
	{
		sq = (long long)sqrt((double)i) + 1;
		isp = true;
		for (j=3;j<=sq;j+=2)
		{
			if (i %j == 0)
			{
				isp = false;
				break;
			}
		}
		if (isp)
			v.push_back(i);
	}
}

long long calc(long long i1, long long i2, long long p)
{
	int		t, ts, c;
	long long	ans, i, count, d1, d2, n, min;
	vector<long long>	primes;
	vector<long long>::iterator	it;

	prim(primes, p, i2);
	ts = primes.size();
	vector<long long>	s(ts);
	vector<int>	b(ts, 0);
	ts = primes.size();
	for (i=0;i<ts;i++)
	{
		s[i] = primes[i];
	}

	count = 0;
	for (i=i1;i<=i2;i++)
	{
		c = 0; min = -1;
		for (t=0;t<ts;t++)
		{
			if (primes[t] > i)
				break;
			if (i % primes[t] == 0)
			{
				b[t]++;
				if (c == 0)
				{
					min = primes[t];
				}
				else
				{
					if (min < s[t])
						s[t] = min;
				}
				c++;
			}
		}
		if (min == -1)
		{
			count++;
		}
	}

#if	0
	copy(s.begin(), s.end(), ostream_iterator<long long>(cout, " "));
	cout << endl;
	copy(s.begin(), s.end(), ostream_iterator<bool>(cout, " "));
	cout << endl;
	cout << count << endl;
#endif
	set<long long>	z;

	for (t=0;t<ts;t++)
		if (b[t])
			z.insert(s[t]);

	return z.size() + count;
}

int main()
{
	int	n, i;
	long long	i1, i2, p;

	cin >> n;
	for (i=0;i<n;i++)
	{
		cin >> i1 >> i2 >> p;
		cin.ignore(255, '\n');
		cout << "Case #" << (i+1) << ": " << calc(i1, i2, p) << endl;
	}
	return 0;
}
