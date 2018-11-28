#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

int k, d;
int a[100];

int64 ans = -1;

int64 gcd(int64 x, int64 y)
{
	if (!x) return y;
	if (!y) return x;
	return gcd(y, x % y);
}

bool add(int64 x)
{
	if (ans == -1 || ans == x)
	{
		ans = x;
		return true;
	}
	return false;
}

const int maxl = 1000 * 1000 + 100;

bool pr[maxl];

void Solve()
{
	ans = -1;
	cin >> d >> k;
	int up = 1;
	for (int i = 0; i < d; i++)
		up *= 10;
	int down = 0;
	for (int i = 0; i < k; i++)
	{
		cin >> a[i];
		down = max(down, a[i] + 1);
	}
	if (k == 1)
	{
		printf("I don't know.\n");
		return;
	}
	vector<int64> vp;
	for (int i = down; i <= up; i++)
		if (pr[i])
			vp.pb(i);
	for (int i = 0; i <= up; i++)
	{
		int64 d = 0;
		int64 b = 0;
		int64 pc = 0;
		for (int j = 1; j < k; j++)
		{
			int64 cur = (int64)a[j] - ((int64)a[j - 1]) * (int64)i;
			b = cur;
			if (j > 1)
				d = gcd(d, abs(cur - pc));
			pc = cur;
		}
		if (d != 0 && d < down) continue;
		int64 next = ((int64)a[k - 1]) * ((int64)i) + b;
		if (d)
		{
			for (int64 t = 2; t * t <= d; t++)
			{
				if (d % t != 0) continue;
				while (d % t == 0)
					d /= t;
				if (t < down || t > up) continue;
				if (!add((next % t + t) % t) )
				{
					printf("I don't know.\n");
					return;
				}
			}
			if (d > 1)
			{
				int64 t = d;
				if (t >= down && t <= up && !add((next % t + t) % t) )
				{
					printf("I don't know.\n");
					return;
				}
			}
		}
		else
		{
			for (int t = 0; t < sz(vp); t++)
			{
				if (!add((next % vp[t] + vp[t]) % vp[t]) )
				{
					printf("I don't know.\n");
					return;
				}
			}
		}
	}
	if (ans == -1)
	{
		cerr << "Not found\n";
		printf("I don't know.\n");
		return;
	}
	cout << ans << "\n";
}

int main()
{
	memset(pr, 1, sizeof(pr));
	pr[0] = pr[1] = false;
	for (int i = 2; i < maxl; i++)
	{
		if (!pr[i]) continue;
		for (int j = i + i; j < maxl; j += i)
			pr[j] = false;
	}
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		cerr << "Testcase " << (it + 1) << "\n";
		Solve();
	}
	return 0;
}
