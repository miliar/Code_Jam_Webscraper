#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <cassert>
#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;

void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int TEST;

int n;
vector< pair<int, int> > g[105];
double wp[105], owp[105], oowp[105];

char tmp[10005];

bool solve()
{
	TEST++;

	for (int i = 0; i < 105; i++)
		g[i].clear();

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", tmp);
		for (int j = 0; j < n; j++)
			if (tmp[j] == '1')
			{
				g[i].pb(mp(j, 1));
				//g[j].pb(mp(i, 0));
			}
			else if (tmp[j] == '0')
			{
				g[i].pb(mp(j, 0));
				//g[j].pb(mp(i, 1));
			}
	}

	_(wp, 0);
	_(owp, 0);
	_(oowp, 0);
	for (int i = 0; i < n; i++)
		if (g[i].size() != 0)
		{
			for (int j = 0; j < g[i].size(); j++)
				wp[i] += g[i][j].second;
			wp[i] /= (double)g[i].size();
		}

	for (int i = 0; i < n; i++)
	{
		int cc = 0;
		for (int j = 0; j < g[i].size(); j++)
		{
			int x = g[i][j].first;
			if (g[x].size() > 1)
			{
				double t = 0.0;
				for (int k = 0; k < g[x].size(); k++)
					t += g[x][k].second;
				t -= (1.0 - g[i][j].second);
				//cc += g[x].size() - 1;
				t /= (double)(g[x].size() - 1);
				cc++;
				owp[i] += t;
			}
		}
		if (cc > 0)
			owp[i] /= (double)cc;
		else
			owp[i] = 0.0;
	}

	for (int i = 0; i < n; i++)
		if (g[i].size() != 0)
		{
			for (int j = 0; j < g[i].size(); j++)
				oowp[i] += owp[g[i][j].first];
			oowp[i] /= (double)g[i].size();
		}



	printf("Case #%d:\n", TEST);
	for (int i = 0; i < n; i++)
		printf("%.6lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);

	return false;
}

int main()
{
	prepare();
	int tn; TEST = 0;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}