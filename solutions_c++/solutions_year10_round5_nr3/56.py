#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int test;
string name = "c";

void solve()
{
	long long ans = 0;

	map<int, int> m;
	int n;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int x, c;
		cin >> x >>c;
		m[x] += c;
	}

	while (true)
	{
		bool ok = false;
		for (map<int, int>::iterator im = m.begin(); im != m.end(); im++)
		{
			if (im->second > 1)
			{
				int x = im->first;
				im->second -= 2;
				m[x-1]++;
				m[x+1]++;
				ok = true;
				ans++;
				break;
			}
		}
		if (!ok) break;
	}

	cout << "Case #" << test << ": ";
	cout << ans << endl;

	cerr << "Case #" << test << ": ";
	cerr << ans << endl;
}

int main()
{
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (test = 1; test <= tests; test++)
		solve();

	return 0;
}