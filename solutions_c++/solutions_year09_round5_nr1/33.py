#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

const int MAXN = 12;
const int MAXK = 5;

class State
{
public:
	int pi[MAXK];
	int pj[MAXK];
};

int n, m, k;

bool operator<(const State &a, const State &b)
{
	int i;
	for (i = 0; i < k; i++)
	{
		if (a.pi[i] < b.pi[i]) return true;
		if (a.pi[i] > b.pi[i]) return false;
		if (a.pj[i] < b.pj[i]) return true;
		if (a.pj[i] > b.pj[i]) return false;
	}
	return false;
}

State bs, es;
char ma[MAXN][MAXN];

void Load()
{
	scanf("%d%d", &n, &m);
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			char c = getchar();
			while (! ((c == '.') || (c == '#') || (c == 'o') || (c == 'x') || (c == 'w'))) c = getchar();
			ma[i][j] = c;
		}
	}
}

void Trim(State &a)
{
	int f = 1;
	while (f)
	{
		f = 0;
		int i;
		for (i = 0; i < k - 1; i++)
		{
			if (a.pi[i] > a.pi[i + 1] || (a.pi[i] == a.pi[i + 1] && a.pj[i] > a.pj[i + 1]))
			{
				int t = a.pi[i];
				a.pi[i] = a.pi[i + 1];
				a.pi[i + 1] = t;
				t = a.pj[i];
				a.pj[i] = a.pj[i + 1];
				a.pj[i + 1] = t;
				f = 1;
			}
		}
	}
}

map<State, int> dst;
vector<State> q;
const int di[5] = {-1, 1, 0, 0, 0};
const int dj[5] = {0, 0, -1, 1, 0};

int rt[MAXK];

int Root(int x)
{
	if (x != rt[x]) rt[x] = Root(rt[x]);
	return rt[x];
}

bool Check(State &a)
{
	int i;
	for (i = 0; i < k; i++) rt[i] = i;
	int j;
	for (i = 0; i < k; i++)
	{
		for (j = i + 1; j < k; j++)
		{
			if (abs(a.pi[i] - a.pi[j]) + abs(a.pj[i] - a.pj[j]) == 1)
			{
				rt[Root(i)] = Root(j);
			}
		}
	}
	for (i = 1; i < k; i++) if (Root(i) != Root(0)) return false;
	return true;
}

void Solve()
{
	int cb, ce;
	cb = ce = 0;
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (ma[i][j] == 'o')
			{
				bs.pi[cb] = i;
				bs.pj[cb] = j;
				cb++;
				ma[i][j] = '.';
			}
			else if (ma[i][j] == 'x')
			{
				es.pi[ce] = i;
				es.pj[ce] = j;
				ce++;
				ma[i][j] = '.';
			}
			else if (ma[i][j] == 'w')
			{
				bs.pi[cb] = i;
				bs.pj[cb] = j;
				cb++;
				es.pi[ce] = i;
				es.pj[ce] = j;
				ce++;
				ma[i][j] = '.';
			}
		}
	}
	k = cb;
	Trim(bs);
	Trim(es);
	dst.clear();
	q.clear();
	dst[bs] = 0;
	q.push_back(bs);
	int hd = 0;
	while (hd < q.size())
	{
		// which box and where
		int p;
		int curd = dst[q[hd]];
		//cerr << "PRocessing state: ";
		//for (p = 0; p < k; p++) cerr << "(" << q[hd].pi[p] << "," << q[hd].pj[p] << ") ";
		//cerr << dst[q[hd]] << "\n";
		for (p = 0; p < k; p++)
		{
			int k;
			for (k = 0; k < 4; k++)
			{
				int ni1 = q[hd].pi[p] + di[k];
				int nj1 = q[hd].pj[p] + dj[k];
				int pi1 = q[hd].pi[p] - di[k];
				int pj1 = q[hd].pj[p] - dj[k];
				if (ni1 < 0 || ni1 >= n || nj1 < 0 || nj1 >= m) continue;
				if (ma[ni1][nj1] == '#') continue;
				if (pi1 < 0 || pi1 >= n || pj1 < 0 || pj1 >= m) continue;
				if (ma[pi1][pj1] == '#') continue;
				int f = 1;
				int pp;
				for (pp = 0; pp < ::k; pp++)
				{
					if (pp == p) continue;
					if (q[hd].pi[pp] == pi1 && q[hd].pj[pp] == pj1)
					{
						f = 0;
						break;
					}
				}
				for (pp = 0; pp < ::k; pp++)
				{
					if (pp == p) continue;
					if (q[hd].pi[pp] == ni1 && q[hd].pj[pp] == nj1)
					{
						f = 0;
						break;
					}
				}
				if (!f) continue;
				State ns = q[hd];
				ns.pi[p] = ni1;
				ns.pj[p] = nj1;
				Trim(ns);
				int cl = 1;
				if (Check(ns) || Check(q[hd]))
				{
					if (dst.find(ns) == dst.end() || dst[ns] > curd + cl)
					{
						dst[ns] = curd + cl;
						q.push_back(ns);
					}
				}
			}
		}
		hd++;
	}
	if (dst.find(es) == dst.end()) cout << "-1";
	else cout << dst[es];
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}