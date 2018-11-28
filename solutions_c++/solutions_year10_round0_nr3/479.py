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
typedef long long int64;

int const NMAX = 1010;
int n, k, r;
int64 p[NMAX], a[NMAX];
int used[NMAX];

int next(int &now)
{
	int old = now, res = 0;
	while (now < n && res + p[now] <= k)
	{
		res += p[now];
		now++;
	}
	if (now == n) now = 0;
	while (now < old && res + p[now] <= k)
	{
		res += p[now];
		now++;
	}
	return res;
}

void solve()
{
	cin >> r >> k >> n;
	forn(i, n)
		cin >> p[i];
		
	seta(used, 255);
	used[0] = 0;
	int now = 0, num = 0;
	a[0] = 0;
	while (true)
	{
		num++;
		a[num] = a[num - 1] + next(now);
		if (used[now] != -1) break;
		used[now] = num;
	}
	
	if (r <= num)
	{
		cout << a[r];
		return;
	}
	
	int64 ans = a[used[now]];
	num -= used[now];
	forn(i, num + 1)
		a[i] = a[i + used[now]];
	forn(i, num + 1)
		if (i) a[i] -= a[0];
	a[0] = 0;
	r -= used[now];
	
	ans += a[num] * (r / num);
	ans += a[r % num];
	cout << ans;
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
		cout << endl;
	}

	return 0;
}
