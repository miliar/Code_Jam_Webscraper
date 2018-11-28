#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#pragma comment(linker, "/STACK:67108864")
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define mp make_pair
#define pb push_back

vector <int> v, mx, mxs;

int findmx(int idx, int delta)
{
	int mx = -1;
	for (int i = 10; i >= 0; --i)
		for (int j = i; j >= 0; --j)
		{
			int k = v[idx] - i - j;
			if (k < 0 || k > 10)
				break;
			if (max(abs(i - k), max(abs(i - j), abs(j - k))) <= delta)
				mx = max(mx, max(i, max(j, k)));
		}
	return mx;
}

void solve(int t)
{
	int ans = 0;
	int n, s, p;
	cin >> n >> s >> p;
	v.resize(n);
	mx.resize(n);
	mxs.resize(n);
	forn(i, n)
		cin >> v[i];
	forn(i, n)
	{
		mx[i] = findmx(i, 1);
		mxs[i] = findmx(i, 2);
	}
	forn(i, n)
	{
		if (mx[i] >= p)
			ans++;
		else if (mx[i] < p && mxs[i] >= p && s > 0)
		{
			s--;
			ans++;
		}
	}
	cout << "Case #" << t << ": " << ans << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	forn(i, t)
		solve(i + 1);
	return 0;
}