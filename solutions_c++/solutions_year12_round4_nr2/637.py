#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int r[1050], x[1050], y[1050];
int ind[1050];

bool cmp(int i, int j)
{
	return r[i] > r[j];
}

int n, w, l;

void solve(int & pos, int x0, int y0)
{
	if (x0 > w || y0 > l || pos == n)
		return;
	x[ind[pos]] = x0;
	y[ind[pos]] = y0;
	pos++;
	int oldr = r[ind[pos - 1]];
	solve(pos, x0, y0 + oldr + r[ind[pos]]);
	solve(pos, x0 + oldr + r[ind[pos]], y0);
	solve(pos, x0 + oldr + r[ind[pos]], y0 + oldr + r[ind[pos]]);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, tt;
	scanf("%d", &T);
	for (tt = 0; tt < T; ++tt)
	{
		int i;
		scanf("%d%d%d", &n, &w, &l);
		for (i = 0; i < n; ++i)
		{
			scanf("%d", &r[i]);
			ind[i] = i;
		}
		sort(ind, ind + n, cmp);
		int pos = 0;
		solve(pos, 0, 0);
		if (pos < n)
			throw 42;
		printf("Case #%d: ", tt + 1);
		for (i = 0; i < n; ++i)
			printf("%.2lf %.2lf ", (double)x[i], (double)y[i]);
		printf("\n");
	}
	
	return 0;
}