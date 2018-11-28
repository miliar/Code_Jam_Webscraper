#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define FORZ(i, n) FOR(i, 0, n)
#define pb push_back
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define cl(x) memset(x, 0, sizeof(x))

struct Node
{
	int v;
	int c;
	int n;
};

int v, m;

vector <Node> nodes;

bool Check(int v)
{
	if(v >= (m - 1) / 2)
		return nodes[v].v;
	else
	{
		if(nodes[v].n == 1)
			return Check(2 * v + 1) & Check(2 * v + 2);
		else
			return Check(2 * v + 1) | Check(2 * v + 2);
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	FORZ(i, n)
	{
		nodes.clear();
		scanf("%d%d", &m, &v);
		FORZ(j, (m - 1) / 2)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			Node f;
			f.c = y;
			f.v = x;
			f.n = x;
			nodes.pb(f);
		}
		FOR(j, (m - 1) / 2, m)
		{
			int x;
			scanf("%d", &x);
			Node f;
			f.c = 0;
			f.v = x;
			f.n = x;
			nodes.pb(f);
		}
		int ans;
		if(Check(0) == v)
			ans = 0;
		ans = -1;
		FORZ(j, 1 << ((m - 1) / 2))
		{
			bool flag = true;
			FORZ(k, (m - 1) / 2)
			{
				if(j & (1 << k))
					nodes[k].n = 1;
				else
					nodes[k].n = 0;
				if(nodes[k].c == 0 && nodes[k].n != nodes[k].v)
				{
					flag = false;
					break;
				}
			}
			if(!flag) 
				continue;
			if(Check(0) == v)
			{
				int d = 0;
				FORZ(k, (m - 1) / 2)
					if(nodes[k].n != nodes[k].v)
						d++;
				if(d < ans || ans == -1)
					ans = d;
			}
		}
		printf("Case #%d: ", i + 1);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}