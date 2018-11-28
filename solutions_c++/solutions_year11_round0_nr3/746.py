#include "stdafx.h"
#if 1
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ios>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
using namespace std;

#define mp(x, y) make_pair(x, y)
#define sz(v) (int) ((v).size())
#define rep(i, n) for (int i = 0; i < n; i++)

void solve();
int main()
{
#ifdef __HOME__
	//freopen("1.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif
	solve();
	return 0;
}

#endif

int N;
int a[1000];

void solve()
{
	int T;
	cin >> T;
	rep(tc, T)
	{
		cout << "Case #" << tc + 1 << ": ";

		cin >> N;
		int s = 0;
		long long actual = 0;
		rep(i, N)
		{
			cin >> a[i];
			s ^= a[i];
			actual += a[i];
		}

		if (s != 0)
		{
			cout << "NO\n";
			continue;
		}

		cout << actual - *min_element(a, a + N) << '\n';
	}
}
