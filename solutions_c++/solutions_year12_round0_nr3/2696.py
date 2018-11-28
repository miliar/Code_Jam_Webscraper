#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) a.begin(), a.end()

const string name = "g";

const int NMAX = 2010000;

int A, B;
vector <int> g[NMAX];

int main()
{
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);

	forn(i, 2000001)
	{
		char s[8];
		sprintf(s, "%d", i);
		int n = strlen(s);
		forn(j, n)
		{
			if (atoi(s) != i) g[i].pb(atoi(s));
			char tmp = s[0];
			forn(f, n - 1)
				s[f] = s[f + 1];
			s[n - 1] = tmp;
		}
		sort(all(g[i]));
		g[i].resize(unique(all(g[i])) - g[i].begin());
	}

	int tst;
	cin >> tst;
	forn(t, tst)
	{
		cin >> A >> B;
		int ans = 0;
		for (int i = A; i <= B; ++i)
			forn(j, g[i].size())
				if (A <= g[i][j] && g[i][j] <= B) ans++;
		cout << "Case #" << t + 1 << ": " << ans / 2 << endl;
	}

	return 0;
}
