#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())
#define pb push_back

typedef vector<int> longint;


longint a;

void trim(longint& a)
{
	while ((int)a.size() > 1 && a[(int)a.size() - 1] == 0) a.erase(a.end() - 1);
}

void sum(longint a, longint b, longint& c, int osn)
{
	c.clear();
	int k = max((int)a.size(), (int)b.size());
	while ((int)a.size() < k) a.pb(0);
	while ((int)b.size() < k) b.pb(0);
	c = longint(k + 1);
	forn(i, k)
	{
		c[i + 1] = (a[i] + b[i] + c[i]) / osn;
		c[i] = (a[i] + b[i] + c[i]) % osn;
	}
	trim(c);
}

void mul(longint a, longint b, longint& c, int osn)
{
	c.clear();
	c = longint((int)a.size() + (int)b.size() + 1);
	forv(i, a)
	{
		forv(j, b)
		{
			c[i + j + 1] = (a[i] * b[i] + c[i + j]) / osn;
			c[i + j] = (a[i] * b[i] + c[i + j]) % osn;
		}
	}
	trim(c);
}

longint toLongint(int n, int osn)
{
	longint ans;
	while (n > 0)
	{
		ans.pb(n % osn);
		n /= osn;
	}
	if ((int)ans.size() == 0)
		ans.pb(0);
	return ans;
}

int res[10];
int step[100];

longint next(longint a, int osn)
{
	longint res;
	forv(i, a)
	{
		longint tmp;
		mul(toLongint(a[i], osn), toLongint(a[i], osn), tmp, osn);
		sum(res, tmp, res, osn);
	}
	trim(res);
	return res;
}

bool ok(longint a, int osn)
{
	set<longint> used;
	while (used.count(a) == 0)
	{
		used.insert(a);
		a = next(a, osn);
	}
	trim(a);
	return (int)a.size() == 1 && a[0] == 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int tests;
	scanf("%d\n", &tests);
	forn(test, tests)
	{
		string s;
		getline(cin, s);
		stringstream st(s);
		int x;
		int sz = 0;
		while (st >> x)
		{
			step[sz++] = x;
		}

		int result = 2;
		for ( ; ; result++)
		{
			bool fl = true;
			forn(j, sz)
			{
				if (!ok(toLongint(result, step[j]), step[j]))
					fl = false;
			}
			if (fl)
			{
				printf("Case #%d: %d\n", test + 1, result);
				break;
			}
		}
	}

	return 0;
}

