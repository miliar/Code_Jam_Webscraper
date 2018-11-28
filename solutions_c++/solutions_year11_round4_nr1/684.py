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

vector <pair <pair <LD, LD>, LD> > v;
LD x, s, r, tim;
int n;

int main()
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int t;
	cin >> t;
	cout << fixed << setprecision(9);
	for (int test = 1; test <= t; ++test)
	{
		LD ans = 0.0;
		cin >> x >> s >> r >> tim >> n;
		v.clear();
		for (int i = 0; i < n; ++i)
		{
			LD b, e, vv;
			cin >> b >> e >> vv;
			v.push_back(make_pair(make_pair(b, e), vv));
		}
		sort(v.begin(), v.end());

		vector <pair <pair <LD, LD>, LD> > v1;
		LD xx = 0.0;
		for (int i = 0; i < n; ++i)
		{
			if (xx + 1e-6 < v[i].first.first)
				v1.push_back(make_pair(make_pair(xx, v[i].first.first), 0.0));
			v1.push_back(v[i]);
			xx = v[i].first.second;
		}
		if (xx < x)
			v1.push_back(make_pair(make_pair(xx, x), 0.0));
		v = v1;
		n = v.size();

		vector <pair <LD, int> > vv (n);
		for (int i = 0; i < n; ++i)
			vv[i] = make_pair((v[i].second + s) / (v[i].second + r), i);
		sort(vv.begin(), vv.end());

		for (int i = 0; i < n; ++i)
			ans += (v[i].first.second - v[i].first.first) / (v[i].second + s);

		for (int i = 0; i < n; ++i)
		{
			if (tim < 1e-7) break;
			LD vvv = v[vv[i].second].second;
			LD tt = (v[vv[i].second].first.second - v[vv[i].second].first.first) / (vvv + r);
			tt = min(tt, tim);
			ans -= ((vvv + r) / (vvv + s) - 1) * tt;
			tim -= tt;
		}

		cout << "Case #" << test << ": " << ans << '\n';
	}

	return 0;
}
