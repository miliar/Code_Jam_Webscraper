#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <iterator>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

int t, n;
string s[200];
LD ans[200];
LD wp[200], owp[200], oowp[200];

void solve()
{
	for (int i = 0; i < n; ++i)
	{
		int cnt = 0, good = 0;
		for (int j = 0; j < n; ++j)
		{
			if (s[i][j] != '.') ++cnt;
			if (s[i][j] == '1') ++good;
		}
		wp[i] = LD(good) / cnt;
	}

	for (int i = 0; i < n; ++i)
	{
		LD sum = 0.0; int cnt0 = 0;
		for (int j = 0; j < n; ++j)
		{
			if (j == i || s[i][j] == '.') continue;
			int cnt = 0, good = 0;
			for (int k = 0; k < n; ++k)
			{
				if (k == i) continue;
				if (s[j][k] != '.') ++cnt;
				if (s[j][k] == '1') ++good;
			}
			sum += LD(good) / cnt;
			++cnt0;
		}
		owp[i] = sum / cnt0;
	}

	for (int i = 0; i < n; ++i)
	{
		LD sum = 0.0; int cnt = 0;
		for (int j = 0; j < n; ++j)
		{
			if (s[i][j] == '.') continue;
			sum += owp[j]; ++cnt;
		}
		oowp[i] = sum / cnt;
	}

	for (int i = 0; i < n; ++i)
		ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];	
}

int main()
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	cin >> t;
	cout << fixed << setprecision(10);
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> s[i];
		cout << "Case #" << tt << ":\n";
		solve();
		for (int i = 0; i < n; ++i)
			cout << ans[i] << '\n';
	}

	return 0;
}
