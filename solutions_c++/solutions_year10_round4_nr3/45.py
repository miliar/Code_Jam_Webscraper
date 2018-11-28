#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define mp make_pair

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

const int dx[] = {-1, 0};
const int dy[] = {0, -1};

set<ii> s;

queue<pair<ii, int> > q, qq;

void Solve()
{
	int r;
	cin >> r;
	s.clear();
	for (int it = 0; it < r; it++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int i = x1; i <= x2; i++)
			for (int j = y1; j <= y2; j++)
				s.insert(ii(i, j));
	}
	q = queue<pair<ii, int> >();
	qq = queue<pair<ii, int> >();
	for (set<ii>::iterator it = s.begin(); it != s.end(); it++)
	{
		bool f = false;
		int x = it->first, y = it->second;
		for (int dir = 0; dir < 2; dir++)
		{
			if (s.count(ii(x + dx[dir], y + dy[dir])))
			{
				f = true;
				break;
			}
		}
		if (!f)
			q.push(mp(ii(x, y), 0));
		x++;
		if (s.count(ii(x, y))) continue;
		if (!s.count(ii(x, y - 1))) continue;
		q.push(mp(ii(x, y), 1));
	}
	int res = 0;
	while (sz(s))
	{
		res++;
		qq = queue<pair<ii, int> >();
		while (!q.empty())
		{
			int t = q.front().second;
			int x = q.front().first.first;
			int y = q.front().first.second;
			q.pop();
			if (t == 0)
			{
				if (!s.count(ii(x, y))) continue;
				s.erase(ii(x, y));
				{
					int xx = x + 1, yy = y;
					if (s.count(ii(xx, yy)) && !s.count(ii(xx, yy - 1)))
						qq.push(mp(ii(xx, yy), 0));
				}
				{
					int xx = x, yy = y + 1;
					if (s.count(ii(xx, yy)) && !s.count(ii(xx - 1, yy)))
						qq.push(mp(ii(xx, yy), 0));
				}
			}
			else
			{
				if (s.count(ii(x, y))) continue;
				s.insert(ii(x, y));
				{
					int xx = x + 1, yy = y;
					if (!s.count(ii(xx, yy)) && s.count(ii(xx, yy - 1)))
						qq.push(mp(ii(xx, yy), 1));
				}
				{
					int xx = x, yy = y + 1;
					if (!s.count(ii(xx, yy)) && s.count(ii(xx - 1, yy)))
						qq.push(mp(ii(xx, yy), 1));
				}
			}
		}
		while (!qq.empty())
		{
			int t = qq.front().second;
			int x = qq.front().first.first;
			int y = qq.front().first.second;
			qq.pop();
			if (t == 0)
			{
				if (s.count(ii(x - 1, y)) || s.count(ii(x, y - 1)))
					continue;
			}
			else
			{
				if (!s.count(ii(x - 1, y)) || !s.count(ii(x, y - 1)))
					continue;
			}
			q.push(mp(ii(x, y), t));
		}
	}
	cout << res << "\n";
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		Solve();
	}
	return 0;
}
