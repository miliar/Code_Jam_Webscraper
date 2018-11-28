#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <cassert>

using namespace std;

int test;
string name = "a";

const int nn = 1 << 20;

bool pp[1 << 20];

void init()
{
	memset(pp, 1, sizeof pp);
	for (int i = 2; i < nn; i++) if (pp[i])
	{
		for (int j = i + i; j < nn; j+=i) pp[j] = 0;
	}
}

long long pow(long long x, long long p, long long m)
{
	assert(x);
	long long res = 1;
	while (p)
	{
		if (p & 1) res = res * x % m;
		p >>= 1;
		x = x * x % m;
	}
	return res;
}

int inv(int x, int m)
{
	x = ( x % m + m ) % m;
	return pow(x, m - 2, m);
}

void solve()
{
	long long ans = -1;

	int d, k;
	cin >> d >> k;
	int a[10];
	for (int i = 0; i < k; i++) cin >> a[i];
	int D = 1;
	for (int i = 0; i < d; i++) D *= 10;

	if (k > 1 && a[0] == a[1])
		ans = a[0];

	if (k > 2 && a[0] != a[1])
	{
		int M = a[0];
		for (int i = 0; i < k; i++) M = max(M, a[i]);
		for (int p = M + 1; p <= D && ans >= -1; p++) if (pp[p])
		{
			long long X = a[0];
			long long S = a[1] - a[0];
			long long T = a[2] - a[1];
			long long A = T * inv(S, p); A = (A % p + p) % p;
			long long B = a[1] - a[0] * A; B = (B % p + p ) % p;
			
			bool ok = true;
			for (int i = 1; i < k; i++)
			{
				X = (A * X + B) % p;
				if (X != a[i]) ok = false;
			}
			if (ok)
			{
				if (ans == -1 || ans == (A * X + B) % p) ans = (A * X + B) % p;
				else ans = -2;
			}
		}
	}

	cout << "Case #" << test << ": ";
	if (ans >= 0)
		cout << ans << endl;
	else
		cout << "I don't know." << endl;

	cerr << "Case #" << test << ": ";
	cerr << ans << endl;
}

int main()
{
	init();

	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (test = 1; test <= tests; test++)
		solve();

	return 0;
}