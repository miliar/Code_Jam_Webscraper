#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

struct vine
{
	long long d;
	long long l;
};

long long n, m;
vine v[10100];
long long D;
long long profs[10100];

void read()
{
	long long i, j;
	cin >> n;
	
	for (i = 1; i <= n; ++i)
	{
		cin >> v[i].d >> v[i].l;
	}
	
	cin >> D;
}

void solve()
{
	long long i, j, i1, j1;

	long long cur;
	
	profs[1] = v[1].d;

	if (profs[1] + v[1].d >= D)
	{
		std::cout << "YES\n";
		return;
	}

	for (i = 2; i <= n; ++i)
	{
		profs[i] = -1;

		for (j = i - 1; j >= 1; --j)
		{
			if (v[j].d + profs[j] >= v[i].d) 
			{
				cur = min(v[i].l, v[i].d - v[j].d);

				if (cur > profs[i])
				{
					profs[i] = cur;

					if (profs[i] == v[i].l)
						break;
				}
			}
		}

		if (profs[i] + v[i].d >= D)
		{
			std::cout << "YES\n";
			return;
		}
	}

	std::cout << "NO\n";
} 
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t;
	cin >> t;
	long long i;
	for (i = 1; i <= t; ++i)
	{
		read();
		std::cout << "Case #" << i << ": ";
		solve();
	}
}