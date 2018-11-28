#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

int n;
int color[10], ans[10];
vector< set<int> > v;

bool paint(int ver, int col)
{
	if(ver > n)
	{
		for(int i = 0; i < v.size(); ++i)
		{
			vector<bool> da(col + 1, false);
			for(set<int> :: iterator it = v[i].begin(); it != v[i].end(); ++it)
				da[ color[ *it ] ] = true;
			for(int j = 1; j <= col; ++j)
				if(da[j] == false)
					return false;
		}
		for(int i = 1; i <= n; ++i)
			ans[i] = color[i];
		return true;
	}
	else
	{
		for(int i = 1; i <= col; ++i)
		{
			color[ver] = i;
			if(paint(ver + 1, col))
				return true;
		}
	}
	return false;
}

int Solution()
{
	int m;
	cin >> n >> m;

	v.clear();
	set<int> s;
	for(int i = 1; i <= n; ++i)
		s.insert(i);
	v.push_back(s);

	int mas[9];
	for(int i = 0; i < m; ++i)
		cin >> mas[i];

	for(int i = 0; i < m; ++i)
	{
		int x, y = mas[i];
		cin >> x;
		if(x > y)
		{
			int t = x; x = y; y = t;
		}

		int j;
		for(j = 0; j < v.size(); ++j)
			if(v[j].find(x) != v[j].end() && v[j].find(y) != v[j].end())
				break;

		set<int> s1, s2;
		for(set<int> :: iterator it = v[j].begin(); it != v[j].end(); ++it)
			if((*it) >= x && (*it) <= y)
				s1.insert(*it);
			else
				s2.insert(*it);
		s2.insert(x); s2.insert(y);

		v[j].clear();
		v[j] = s1;
		v.pb(s2);
	}

	int size = 0;
	for(int i = 0; i < v.size(); ++i)
		size = max(size, (int)v[i].size());
	for(int i = size; i >= 1; --i)
		if(paint(1, i))
		{
			cout << i << endl;
			break;
		}
	for(int i = 1; i < n; ++i)
		cout << ans[i] << ' ';
	cout << ans[n] << endl;
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		Solution();
	}
#ifdef debug
	system("@pause");
#endif
	return 0;
}
