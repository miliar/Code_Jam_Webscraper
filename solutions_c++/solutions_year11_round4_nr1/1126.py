#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	
	//freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int tc = 1; tc <= tests; tc ++)
	{
		double t;
		int x, s, r,  n;
		cin >> x >> s >> r >> t >> n;
		int now,b,e,w;
		r-=s;
		vector <pair<int,int> > a;
		now = 0;
		for (int i = 0; i < n; i ++)
		{
			cin >> b >> e >> w;
			if (b > now)
				a.push_back(make_pair(s,b-now));
			a.push_back(make_pair(s+w,e-b));
			now = e;
		}
		if (now < x)
			a.push_back(make_pair(s,x-now));

		sort(a.begin(),a.end());
		double ans = 0;
		for (int i = 0; i < a.size(); i ++)
		{
			if (t > 1e-9)
			{
				int v = r + a[i].first;
				double tt = (double)a[i].second/v;
				if (tt <= t)
				{
					t -= tt;
					a[i].first += r;
				}
				else
				{
					tt = t;
					t =0;
					double len = tt*v;
					ans += (double)(a[i].second-len)/(a[i].first);
					ans += (double)(len)/(a[i].first+r);
					continue;
				}
			}
			ans += (double)(a[i].second)/(a[i].first);
		}

		cout << "Case #" << tc << ": ";
		printf("%.9lf\n", ans);
	}
	return 0;
}
