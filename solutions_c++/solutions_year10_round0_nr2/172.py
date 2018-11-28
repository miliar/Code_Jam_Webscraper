#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)
#define seta(a, b) memset(a, b, sizeof(a))
#define x first
#define y second
#define y1 botva
#define pb push_back
#define mp make_pair

int const BASE = 10000;
int const BASEL = 4;
class int64
{
public:
	int data[120];
	
	int64() { seta(data, 0); }
	
	void read()
	{
		seta(data, 0);
		char s[60];
		scanf("%s", s);
		data[0] = strlen(s);
		forn(i, data[0])
			data[i + 1] = s[data[0] - i - 1] - '0';
	}
	
	void print()
	{
		forn(i, data[0])
			cout << data[data[0] - i];
		cout << endl;
	}
};

bool operator<(const int64 &a, const int64 &b)
{
	if (a.data[0] != b.data[0]) return a.data[0] < b.data[0];
	for (int i = a.data[0]; i >= 1; i--)
		if (a.data[i] != b.data[i]) return a.data[i] < b.data[i];
	return true;
}

int64 operator-(const int64 &a, const int64 &b)
{
	int64 res;
	int r = 0;
	res = a;
	for (int i = 1; i <= res.data[0]; i++)
	{
		res.data[i] -= b.data[i] + r;
		if (res.data[i] < 0)
		{
			r = 1;
			res.data[i] += 10;
		}
		else r = 0;
	}
	while (res.data[0] > 1 && res.data[res.data[0]] == 0) res.data[0]--;
	return res;
}

int64 operator%(const int64 &a, const int64 &b)
{
	int64 res, tmp;
	res = a;
	for (int i = a.data[0]; i >= 0; i--)
	{
		seta(tmp.data, 0);
		for (int j = b.data[0]; j >= 1; j--)
			tmp.data[j + i] = b.data[j];
		tmp.data[0] = b.data[0] + i;
		
		while (tmp < res)
			res = res - tmp;
	}
	return res;
}

int n;
int64 x, y, now;

int64 gcd(int64 a, int64 b)
{
	if (b < a) swap(a, b);
	if (a.data[0] == 1 && a.data[1] == 0) return b;
	return gcd(b % a, a);
}

void solve()
{
	cin >> n;
	x.read();
	forn(i, n - 1)
	{
		y.read();
		if (x < y) y = y - x;
		else y = x - y;
		if (!i) now = y;
		else now = gcd(now, y);
	}
	((now - (x % now)) % now).print();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	forn(t, tests)
	{
		cout << "Case #" << t + 1 << ": ";
		solve();
	}

	return 0;
}
