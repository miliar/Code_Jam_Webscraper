#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int nt = 1; nt <= tests; ++nt)
	{
		int x, s, r, t, n;
		cin >> x >> s >> r >> t >> n;

		vector<pair<int, int> > v; 

		int rest = x;

		for (int i = 0; i < n; ++i)
		{
			int b, e, w;
			cin >> b >> e >> w;
			rest -= (e - b);
			v.push_back(make_pair(w, e - b));
		}
		v.push_back(make_pair(0, rest));

		sort(v.begin(), v.end());

		LD ans = 0.0L;
		LD tl = t;
		bool run = true;
		for (size_t i = 0; i < v.size(); ++i)
		{
        	if (!run) ans += (LD)v[i].second / (v[i].first + s);
        	else
        	{
        		LD rt = (LD)v[i].second / (v[i].first + r);
        		if (rt < tl)
        		{
        			ans += rt; tl -= rt;
        		}
        		else
        		{
        			ans += tl + (v[i].second - (v[i].first + r) * tl) / (v[i].first + s);
        			tl = 0;
        			run = false;
        		}
        	}

		}
		cout << fixed << setprecision(10) << "Case #" << nt << ": " << ans << '\n';
	}

	return 0;
}
