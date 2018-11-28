#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cstring>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)
#define seta(a, b) memset(a, b, sizeof(a))
#define fs first
#define sc second
#define y1 botva
#define pb push_back
#define mp make_pair

int const NMAX = 210;
int v[NMAX], p[NMAX], n;
set <int> s;
int a[3000020];

void solve()
{
	cin >> n;
	seta(a, 0);
	forn(i, n)
	{
		cin >> p[i] >> v[i];
		p[i] += 1200000;
		if (v[i] >= 2) s.insert(p[i]);
		a[p[i]] += v[i];	
	}
	
	long long ans = 0;
	while (s.size() != 0)
	{
		int poz = *s.begin();
		s.erase(poz);
		
		int tmp = a[poz] / 2;
		ans += tmp;
		a[poz - 1] += tmp;
		a[poz + 1] += tmp;
		a[poz] -= 2 * tmp;
		if (a[poz - 1] - tmp < 2 && a[poz - 1] >= 2) s.insert(poz - 1);
		if (a[poz + 1] - tmp < 2 && a[poz + 1] >= 2) s.insert(poz + 1);
	}
	
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
