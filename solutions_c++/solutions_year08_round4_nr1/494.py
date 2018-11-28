#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#define INF 10000000
using namespace std;

struct NODE
{
	int gate, change;
}d[10005];

int m, v, va[10005], a[2][10005];

void Cal_vuale(int i)
{
	int l, r;
	l = i + i;
	r = l + 1;
	if (l > m) return ;
	Cal_vuale(l); 
	Cal_vuale(r);
	if (d[i].gate) va[i] = va[l] & va[r];
	else va[i] = va[l] | va[r];
}

int sovle(int i, int v)
{
	if (a[v][i] != -1) return a[v][i];
	if (va[i] == v) return a[v][i] = 0;
	int l, r, t1, t2, t3, t4, t;
	l = i + i;
	r = l + 1;
	if (l > m)
	{
		if (va[i] == v) return a[v][i] = 0;
		else return a[v][i] = INF;
	}
	t1 = sovle(l, 1);
	t2 = sovle(l, 0);
	t3 = sovle(r, 1);
	t4 = sovle(r, 0);
	if (d[i].gate)
	{
		if (v) a[v][i] = t1 + t3;
		else {
			a[v][i] = (t1 + t4) <? (t2 + t3);
			a[v][i] <?= t2 + t4;
		}
	}
	else {
		if (!v) a[v][i] = t2 + t4;
		else {
			a[v][i] = (t1 + t4) <? (t2 + t3);
			a[v][i] <?= t1 + t3;
		}
	}
	if (d[i].change)
	{
		if (!d[i].gate)
		{
			if (v) t = t1 + t3;
			else {
				t = (t1 + t4) <? (t2 + t3);
				t <?= t2 + t4;
			}
			a[v][i] <?= t + 1;
		}
		else {
			if (!v) t = t2 + t4;
			else {
				t = (t1 + t4) <? (t2 + t3);
				t <?= t1 + t3;
			}
			a[v][i] <?= t + 1; 
		}
	}
	if (a[v][i] > INF) a[v][i] = INF;
	return a[v][i];
}

int main()
{
	int i, top, cases, t = 0;
	freopen("D:\\A-large.in", "r", stdin);
//	freopen("in", "r", stdin);
	freopen("D:\\a.out", "w", stdout);
	scanf("%d", &cases);
	while (cases--)
	{
		printf("Case #%d: ", ++t);
		scanf("%d%d", &m, &v);
		for (i = 1; i <= m; i++)
			a[0][i] = a[1][i] = -1;
		top = (m - 1) / 2;
		for (i = 1; i <= top; i++)scanf("%d%d", &d[i].gate, &d[i].change);
		for (; i <= m; i++)
		{
			scanf("%d", va + i);
			d[i].change = 0;
		}
		Cal_vuale(1);
		sovle(1, v);
		if (a[v][1] < INF) printf("%d\n", a[v][1]);
		else puts("IMPOSSIBLE");
	}
	return 0;
}