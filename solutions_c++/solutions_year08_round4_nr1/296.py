#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;

const int inf = 12345678;
vector<int> g, c, mn0, mn1;
int m;

void rec(int nd)
{
	if (nd+nd+1 >= m)
	{
		if (g[nd] == 0) 
			mn0[nd] = 0; 
		else 
			mn1[nd] = 0;
		return;
	}

	rec(nd+nd+1);
	rec(nd+nd+2);

	if (g[nd] == 1)
	{
		mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn1[nd+nd+2]);
		mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn1[nd+nd+2]);
		mn0[nd] = min(mn0[nd], mn1[nd+nd+1] + mn0[nd+nd+2]);
		mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn0[nd+nd+2]);
	}
	else
	{
		mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn0[nd+nd+2]);
		mn1[nd] = min(mn1[nd], mn0[nd+nd+1] + mn1[nd+nd+2]);
		mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn0[nd+nd+2]);
		mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn1[nd+nd+2]);
	}

	if (c[nd])
	{
		if (g[nd] == 0)
		{
			mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn1[nd+nd+2] + 1);
			mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn1[nd+nd+2] + 1);
			mn0[nd] = min(mn0[nd], mn1[nd+nd+1] + mn0[nd+nd+2] + 1);
			mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn0[nd+nd+2] + 1);
		}
		else
		{
			mn0[nd] = min(mn0[nd], mn0[nd+nd+1] + mn0[nd+nd+2] + 1);
			mn1[nd] = min(mn1[nd], mn0[nd+nd+1] + mn1[nd+nd+2] + 1);
			mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn0[nd+nd+2] + 1);
			mn1[nd] = min(mn1[nd], mn1[nd+nd+1] + mn1[nd+nd+2] + 1);
		}
	}
}

int main()
{
	ifstream fin("a.in"); ofstream fout("a.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int v;
		fin >> m >> v;

		g.assign(m, 0);
		c.assign(m, 0);
		mn0.assign(m, inf);
		mn1.assign(m, inf);

		FOR(i, (m-1)/2) fin >> g[i] >> c[i];
		FORD(i, (m-1)/2, m-1) fin >> g[i];

		rec(0);
		int res = (v) ? mn1[0] : mn0[0];

		fout << "Case #" << tt+1 << ":";
		if (res == inf)
			fout << " IMPOSSIBLE" << endl;
		else
			fout << " " << res << endl;
	}
	return 0;	
}
