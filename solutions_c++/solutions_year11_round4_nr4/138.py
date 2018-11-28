#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

const int maxn = 100;

struct Cedge
{
	int t;
	Cedge *next;
}edge[2000], *e[maxn];

int n, m, tot, best, b2, TT;
bool v[maxn], vv[maxn];

void addedge(int s, int t)
{
	tot++;
	edge[tot].t = t;
	edge[tot].next = e[s];
	e[s] = &edge[tot];
	
	tot++;
	edge[tot].t = s;
	edge[tot].next = e[t];
	e[t] = &edge[tot];
}

void init()
{
	tot = 0;
	memset(e, 0, sizeof(e));
	scanf("%d%d", &n, &m);
	for(int i = 1 ; i <= m ; i++)
	{
		int x, y;
		scanf("%d,%d", &x, &y);
		addedge(x, y);
	}
}

int calc()
{
	memset(vv, 0, sizeof(vv));
	int s = 0;
	v[1] = false;
	for(Cedge *j = e[0] ; j ; j = j -> next)
			vv[j -> t] = true;
	for(int i = 2 ; i <= n ; i++)
	if(v[i])
	{
		for(Cedge *j = e[i] ; j ; j = j -> next)
			vv[j -> t] = true;
	}
	for(int i = 1 ; i <= n ; i++)
		if(vv[i] && !v[i]) s++;
	return s;
}

void dfs(int i, int s)
{
	if(s > best) return;
	if(i == 1)
	{
		if(s < best) best = s, b2 = calc();
		else if(s == best) b2 = max(calc(), b2);
		return;
	}
	for(Cedge *j = e[i] ; j ; j = j -> next)
	{
		int k = j -> t;
		if(!v[k])
		{
			v[k] = true;
			dfs(k, s + 1);
			v[k] = false;
		}
	}
}

void work()
{
	best = maxn;
	b2 = 0;
	dfs(0, 0);
	printf("Case #%d: %d %d\n", TT, best - 1, b2);
}

int main()
{
	int TTT;
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	scanf("%d", &TTT);
	for(TT = 1 ; TT <= TTT ; TT++)
	{
		init();
		work();
	}
	return 0;
}
