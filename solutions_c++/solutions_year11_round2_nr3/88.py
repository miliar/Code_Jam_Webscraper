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

const int MAX = 2010;

int t, n, m;
int a[MAX], b[MAX];
vector <vector <int> > comps;

int cnt, best;
vector <int> color, ans;

inline bool check()
{
	cnt = 0;
	bool taken[8];
	memset(taken, 0, sizeof(taken));
	for (int i = 0; i < n; ++i)
		taken[color[i]] = true;
	for (int i = 0; i < 8; ++i)
		cnt += taken[i];

	for (int i = 0; i < comps.size(); ++i)
	{
		memset(taken, 0, sizeof(taken));
		for (int j = 0; j < comps[i].size(); ++j)
			taken[color[comps[i][j]]] = true;
		int tcnt = 0;
		for (int i = 0; i < 8; ++i)
			tcnt += taken[i];
		if (tcnt != cnt) return false;
	}
	return true;
}

void print()
{
	for (int i = 0; i < comps.size(); ++i)
    {
     	cerr << "comp " << i << ":\n";
       	for (int j = 0; j < comps[i].size(); ++j)
       		cerr << comps[i][j] << ' ';
       	cerr << endl;
    }
}

int main()
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> n >> m;
		color.resize(n);
		for (int i = 0; i < m; ++i)
			cin >> a[i];
		for (int i = 0; i < m; ++i)
			cin >> b[i];
		for (int i = 0; i < n; ++i)
			--a[i], --b[i];

		comps.assign(1, vector <int> (n));
		for (int i = 0; i < n; ++i)
			comps[0][i] = i;

        for (int i = 0; i < m; ++i)
        {
        	int x = a[i], y = b[i];
        	if (x > y) swap(x, y);
        	vector <vector <int> > new_comps;
        	for (int j = 0; j < comps.size(); ++j)
        	{
        		if (!binary_search(comps[j].begin(), comps[j].end(), x) ||
        			!binary_search(comps[j].begin(), comps[j].end(), y))
        		{
        			new_comps.push_back(comps[j]);
        			continue;
        		}
        		vector <int> comp = comps[j], comp1, comp2;
        		for (int k = 0; k < comp.size(); ++k)
        		{
        			if (comp[k] >= x && comp[k] <= y)
        				comp1.push_back(comp[k]);
        			if (comp[k] <= x || comp[k] >= y)
        				comp2.push_back(comp[k]);
        		}
                new_comps.push_back(comp1), new_comps.push_back(comp2);
        	}
        	comps = new_comps;
        }

        best = 0;
        int mx = (1 << (3 * (n - 1)));
        for (int mask = 0; mask < mx; ++mask)
        {
        	color[0] = 0;
        	for (int i = 1; i < n; ++i)
        		color[i] = ((mask >> (3 * (i - 1))) & 7);
        	if (check() && cnt > best)
        	{
        		best = cnt;
        		ans = color;
        	}
        }

        vector <int> temp = ans;
        sort(temp.begin(), temp.end());
        temp.erase(unique(temp.begin(), temp.end()), temp.end());
        for (int i = 0; i < n; ++i)
        	ans[i] = find(temp.begin(), temp.end(), ans[i]) - temp.begin() + 1;

		cout << "Case #" << tt << ": " << best << '\n';
		for (int i = 0; i < n; ++i)
			cout << ans[i] << ' ';
		cout.put('\n');

		cerr << tt << " solved\n";
	}

	return 0;
}
