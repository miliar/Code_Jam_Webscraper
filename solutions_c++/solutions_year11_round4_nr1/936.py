#include <iostream>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstdio>

using namespace std;

static const int maxn = 10000;

int x, s, r, n;
double t;
int b[maxn], e[maxn], w[maxn];
vector<pair<pair<int, int>, int> > data;
vector<int> idx;

bool cmp(int a, int b)
{
	return data[a].second < data[b].second;
}

void solve()
{
	cin >> x >> s >> r >> t >> n;
	for (int i = 0; i < n; ++i)
		cin >> b[i] >> e[i] >> w[i];
	
	int xx = 0;
	data.clear();
	idx.clear();
	for (int i = 0; i < n; )
	{
		if (b[i] > xx)
		{
			data.push_back(make_pair(make_pair(xx, b[i]), s));
			xx = b[i];
		}
		else // b[i] == xx
		{
			data.push_back(make_pair(make_pair(b[i], e[i]), s + w[i]));
			xx = e[i];
			++i;
		}
		idx.push_back(idx.size());
	}
	if (xx < x)
	{
		data.push_back(make_pair(make_pair(xx, x), s));
		idx.push_back(idx.size());
	}
	sort(idx.begin(), idx.end(), cmp);
	
	for (int j = 0; j < static_cast<int>(data.size()); ++j)
	{
		//int i = idx[j];
		//cerr << data[i].first.first << ' ' << data[i].first.second << ' ' << data[i].second << endl;
	}

	double ans = 0;
	for (int j = 0; j < static_cast<int>(data.size()); ++j)
	{
		int i = idx[j];
		if (t > 0)
		{
			double ut = (data[i].first.second - data[i].first.first) / static_cast<double>(data[i].second - s + r);
			if (ut < t)
			{
				ans += ut;
				t -= ut;
			}
			else
			{
				double run = t * static_cast<double>(data[i].second - s + r);
				double left = (data[i].first.second - data[i].first.first) - run;
				ans += t + left / static_cast<double>(data[i].second);
				t = 0;
			}
		}
		else
			ans += (data[i].first.second - data[i].first.first) / static_cast<double>(data[i].second);
	}
	printf("%.10lf\n", ans);
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

