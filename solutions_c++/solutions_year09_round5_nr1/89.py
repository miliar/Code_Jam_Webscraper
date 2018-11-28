// GCJ Round 3 - Problem A
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows
int mark[20][20];
string lab[20];
const int X[] = {0, 1, 0, -1};
const int Y[] = {1, 0, -1, 0};
#define FREECELL(x, y) ((x) >= 0 && (y) >= 0 && (x) < m && (y) < n && lab[x][y] == '.' && !mark[x][y])
bool isdangerous(VPII v)
{
	VI mark(v.size());
	mark[0] = 1;
	for (int i=1; i<=(int)v.size(); i++)
	{
		for (int j=0; j<(int)v.size(); j++)
			if (mark[j] == i)
				for (int k=0; k<(int)v.size(); k++)
					if (mark[k] == 0 && abs(v[j].first-v[k].first) + abs(v[j].second-v[k].second) <= 1)
						mark[k] = i+1;
	}
	return *min_element(mark.begin(), mark.end()) == 0;
}
int solve(int m, int n, VPII start, VPII end)
{
	sort(start.begin(), start.end());
	sort(end.begin(), end.end());
	typedef pair<VPII, int> state;
	queue<state> q;
	q.push(state(start, 0));
	memset(mark, 0, sizeof mark);
	set<VPII> visited;
	visited.insert(start);
	while (!q.empty())
	{
		state act = q.front();
		q.pop();
		VPII &pos = act.first;
		if (pos == end)
			return act.second;
		FORIT(it, pos)
		{
			mark[it->first][it->second] = 1;
		}
		int cnt = 0;
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
				if (mark[i][j])
					cnt++;
		assert(cnt == (int)pos.size());
		bool dangerous = isdangerous(pos);
		/*
		for (int i=0; i<m; i++)
		{
			for (int j=0; j<n; j++)
				cout << mark[i][j];
			cout << endl;
		}
		cout << endl;
		*/
		for (int i=0; i<(int)pos.size(); i++)
		{
			int x = pos[i].first, y = pos[i].second;
			for (int k=0; k<4; k++)
			{
				int x0 = x + X[k], y0 = y + Y[k];
				int x1 = x - X[k], y1 = y - Y[k];
				if (FREECELL(x0, y0) && FREECELL(x1, y1))
				{
					VPII tmp = pos;
					tmp[i] = PII(x0, y0);
					sort(tmp.begin(), tmp.end());
					if (dangerous && isdangerous(tmp))
						continue;
					if (!visited.count(tmp))
					{
						visited.insert(tmp);
						q.push(state(tmp, act.second + 1));
					}
				}
			}
		}
		FORIT(it, pos)
		{
			mark[it->first][it->second] = 0;
		}
	}
	return -1;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		int m, n;
		cin >> m >> n;
		for (int i=0; i<m; i++)
			cin >> lab[i];
		VPII start, end;
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
			{
				if (lab[i][j] == 'w' || lab[i][j] == 'o')
				{
					start.push_back(PII(i, j));
				}
				if (lab[i][j] == 'w' || lab[i][j] == 'x')
				{
					end.push_back(PII(i, j));
				}
				if (isalpha(lab[i][j]))
					lab[i][j] = '.';
			}
		int ret = solve(m, n, start, end);
		printf("Case #%d: ", tkase+1);
		cout << ret << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
