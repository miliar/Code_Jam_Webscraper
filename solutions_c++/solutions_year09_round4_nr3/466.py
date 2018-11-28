#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int n, k;

int data[200][100];
bool amap[200][200];
int set[200], sn, result;
int kashi;
bool used[200];

void dfs(int now, int value, int set)
{
	int i, j;
	bool yes = 1;
	kashi++;
	if (kashi > 33000000) return;
	if (value >= result) return;
	
	for (i = 0; i < n; i++)
		if (!used[i]) break;
	if (i == n)
	{
		result = min(result, value);
		return;
	}
	
	for (i = now; i < n; i++)
	{
		if (!used[i])
		{
			for (j = 0; j < n; j++)
			{
				if (set & (1 << j))
				{
					if (!amap[i][j]) break;
				}
			}
			if (j == n)
			{
				used[i] = 1;
				set ^= 1 << i;
				dfs(i + 1, value, set);
				set ^= 1 << i;
				used[i] = 0;
				yes = 0;
			}
		}
	}
	
	if (yes)
		dfs(0, value + 1, 0);
}

int main()
{
	int tcase, tno, i, j, t;
	
	scanf("%d", &tcase);
	for (tno = 1; tno <= tcase; tno++)
	{
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++)
			for (j = 0; j < k; j++)
				scanf("%d", &data[i][j]);
		clr(amap);
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
			{
				for (t = 0; t < k; t++)
					if (data[i][t] >= data[j][t]) break;
				if (t == k) amap[i][j] = amap[j][i] = 1;	
			}
		
		result = MAXINT;
		kashi = 0;
		clr(used);
		used[0] = 1;
		dfs(1, 1, 1);
		printf("Case #%d: %d\n", tno, result);
		
	}
	
	return 0;
}

