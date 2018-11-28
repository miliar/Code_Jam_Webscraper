#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()


int main()
{
#ifdef _DEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		int n, a, b, c, d, x, y, m;
		cin >> n >> a >> b >> c >> d >> x >> y >> m;
		vector<pii> p;
		p.push_back(make_pair(x, y));
		for (int i = 0; i < n - 1; ++i)
		{
			x = (a * (ll)x + b) % m;
			y = (c * (ll)y + d) % m;
			p.push_back(make_pair(x, y));
		}

		int ans = 0;
		for (int i = 0; i < n; ++i)
			for (int j = i + 1; j < n; ++j)
				for (int k = j + 1; k < n; ++k)
					if ((p[i].first + p[j].first + p[k].first) % 3 == 0 &&
						(p[i].second + p[j].second + p[k].second) % 3 == 0)
						++ans;

		printf("Case #%d: %d\n", test, ans);
	}

}