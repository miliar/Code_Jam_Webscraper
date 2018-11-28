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

int mas[1000][3];

int Solution()
{
	int x, s, r, t, n;
	cin >> x >> s >> r >> t >> n;

	map<int, int> m;
	int last = 0;
	for(int i = 0; i < n; ++i)
	{
		int m1, m2, m3;
		cin >> m1 >> m2 >> m3;
		if(m1 > last)
			m[0] += m1 - last;
		m[m3] += m2 - m1;
		last = m2;
	}
	if(last < x)
		m[0] += x - last;

	vector<pair<int, int> > v;
	for(map<int, int> :: iterator it = m.begin(); it != m.end(); ++it)
		v.pb(mp(it->first, it->second));
	sort(v.begin(), v.end());

	double time = 0, ost = t;
	for(int i = 0; i < (int)v.size(); ++i)
	{
		double t1 = (double)v[i].second / (r + v[i].first);
		if(t1 <= ost)
		{
			time += t1;
			ost -= t1;
		}
		else
		{
			time += ost + (double)(v[i].second - ost * (r + v[i].first)) / (s + v[i].first);
			ost = 0;
		}
	}

	printf("%.9lf\n", time);
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
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
