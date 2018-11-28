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

int64 l;
int n;
int64 a[1000];

int64 gcd(int64 x, int64 y)
{
	if (!x) return y;
	if (!y) return x;
	return gcd(y, x % y);
}

int64 Gcd(int l, int r)
{
	int64 res = 0;
	for (int i = l; i < r; i++)
		res = gcd(res, a[i]);
	return res;
}

int64 gcd0(int64 x, int64 y, int64& a, int64& b)
{
	if (x == 0)
	{
		a = 0, b = 1;
		return y;
	}
	if (y == 0)
	{
		a = 1, b = 0;
		return x;
	}
	int64 d, aa, bb;
	d = gcd0(y, x % y, aa, bb);
	a = bb, b = aa - bb * (x / y);
	return d;
}

map<int64, int64> M;
int64 u[1000000];

void Solve()
{
	memset(u, -1, sizeof(u));
	cin >> l >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	sort(a, a + n);
	int64 d = Gcd(0, n);
	if (l % d)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	for (int i = 0; i < n; i++)
		a[i] /= d;
	l /= d;
	int64 res = 0;
	vector<int64> cur, next;
	M.clear();
	M[0] = 0;
	cur.pb(0);
	u[0] = 0;
	bool ok = false;
	int64 r0 = 1LL << 62LL;
	if (l % a[n - 1] == 0)
	{
		ok = true;
		r0 = l / a[n - 1];
	}
	while (!cur.empty())
	{
		int64 x = cur[sz(cur) - 1];
		cur.pop_back();
		for (int i = n - 1; i >= 0; i--)
		{
			int64 y = x + a[i];
			if (u[y % a[n - 1]] != -1)
			{
				int64 t = u[y % a[n - 1]];
				if (y < t) continue;
				if ((y - t) / a[n - 1] + M[t] <= M[x] + 1) continue;
			}
			M[y] = M[x] + 1;
			u[y % a[n - 1]] = y;
			if (y % a[n - 1] == l % a[n - 1])
			{
				r0 = min(r0, M[y] + max(l - y, 0LL) / a[n - 1]);
				ok = true;
			}
			next.push_back(y);
		}
		if (!sz(cur))
		{
			cur = next;
			next.clear();
			sort(all(cur));
		}
	}
	if (!ok)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	//assert(ok);
	res += r0;
	cout << res << "\n";
}

int main()
{
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
