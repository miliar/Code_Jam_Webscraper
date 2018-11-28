#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
using namespace std;

#define FOR(i, n)		for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)		for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)			memset(x, 0, sizeof(x))
#define CLX(x, v)		memset(x, v, sizeof(x))
#define ALL(x)			(x).begin(), (x).end()
#define PB				push_back
#define MP				make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

//////////////////////////////////////////////////////////////////////////

const int N = 10;

int n, m;
int v[N], u[N];
vector<PII> w;

void Scan()
{
	scanf("%d %d", &n, &m);
	FOR(i, m)
	{
		scanf("%d", &v[i]);
		v[i]--;
	}
	FOR(i, m)
	{
		scanf("%d", &u[i]);
		u[i]--;
	}
}

VI GetWall(PII t)
{
	VI res;
	res.PB(t.first);
	int u = t.first, v = t.second;
	while (v != t.first)
	{
		res.PB(v);
		int v2;
		for (int vv = (v + 1) % n; vv != u; vv = (vv + 1) % n)
		{
			FOR(i, w.size())
				if ((w[i].first == v && w[i].second == vv) ||
					(w[i].first == vv && w[i].second == v))
				{
					v2 = vv;
				}
		}
		u = v;
		v = v2;
	}
	int mn = 0;
	FOR(i, res.size()) if (res[i] < res[mn]) mn = i;
	VI res2;
	FOR(i, res.size()) res2.PB(res[(mn + i) % res.size()]);
	return res2;
}

set<VI> s;
vector<VI> ss;

int res;
VI resv;
int cur;
VI curv;

int HASH[10];

int VSize(VI & ccc)
{
	CL(HASH);
	FOR(i, ccc.size()) HASH[ccc[i]] = 1;
	int res = 0;
	FOR(i, 10) res += HASH[i];
	return res;
}

VI v2;
bool Check()
{
	FOR(i, ss.size())
	{
		v2.clear();
		FOR(j, ss[i].size()) v2.PB(curv[ ss[i][j] ]);
		if (VSize(v2) != cur) return false;
	}
	return true;
}


void D(int v, int mx = 1)
{
	if (v == n)
	{
		cur = VSize(curv);
		if (cur > res && Check())
		{
			res = cur;
			resv = curv;
		}
	}
	else
	{
		for (int i = 1; i <= mx; i++)
		{
			curv[v] = i;
			D(v + 1, max(i + 1, mx));
		}
	}
}

void Solve()
{
	w.clear();
	FOR(i, m) w.PB(MP(v[i], u[i]));
	FOR(i, n) w.PB(MP(i, (i + 1) % n));
	sort(ALL(w));
	w.resize(unique(ALL(w)) - w.begin());

	s.clear();
	FOR(i, w.size()) s.insert(GetWall(w[i]));
	
	ss.clear();
	for (set<VI>::iterator i = s.begin(); i != s.end(); i++) ss.PB(*i);

	res = 1;
	resv = VI(n, 1);

	curv.resize(n);
	D(0);

	printf("%d\n", res);
	FOR(i, resv.size())
	{
		if (i) printf(" ");
		printf("%d", resv[i]);
	}
	printf("\n");
	fflush(stdout);
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#else
	/*{
		string s = "";
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}*/
//#endif

	int tt;
	scanf("%d", &tt);
	FOR(i, tt)
	{
		Scan();
		printf("Case #%d: ", i + 1);
		Solve();
	}
	
	return 0;
}
