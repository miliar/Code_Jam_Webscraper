#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int m, v;
int canc[11000];
int type[11000]; // -1 - and -2 -or

void Load()
{
	scanf("%d%d", &m, &v);
	int i;
	for (i = 1; i <= (m - 1) / 2; i++)
	{
		scanf("%d%d", &type[i], &canc[i]);
		if (type[i] == 1) type[i] = -1;
		else type[i] = -2;
	}
	for (i = (m - 1) / 2 + 1; i <= m; i++)
	{
		canc[i] = 0;
		scanf("%d", &type[i]);
	}
}

int res[11000][2];

int Count(int ver, int v)
{
	if (res[ver][v] != -1) return res[ver][v];
	if (type[ver] >= 0)
	{
		if (type[ver] == v) res[ver][v] = 0;
		else res[ver][v] = 1000000000;
		return res[ver][v];
	}
	res[ver][v] = 1000000000;
	// not change
	int rl, rr;
	for (rl = 0; rl <= 1; rl++)
	{
		for (rr = 0; rr <= 1; rr++)
		{
			int cres = Count(2 * ver, rl) + Count(2 * ver + 1, rr);
			if (cres >= 1000000000) continue;
			int ru;
			if (type[ver] == -1) 
			{
				if (rl + rr == 2) ru = 1;
				else ru = 0;
			}
			else
			{
				if (rl + rr == 0) ru = 0;
				else ru = 1;
			}
			if (ru == v)
			{
				if (res[ver][v] > cres) res[ver][v] = cres;
			}
		}
	}
	// change
	if (canc[ver] == 1)
	{
		for (rl = 0; rl <= 1; rl++)
		{
			for (rr = 0; rr <= 1; rr++)
			{
				int cres = Count(2 * ver, rl) + Count(2 * ver + 1, rr) + 1;
				if (cres >= 1000000000) continue;
				int ru;
				if (type[ver] == -2) 
				{
					if (rl + rr == 2) ru = 1;
					else ru = 0;
				}
				else
				{
					if (rl + rr == 0) ru = 0;
					else ru = 1;
				}
				if (ru == v)
				{
					if (res[ver][v] > cres) res[ver][v] = cres;
				}
			}
		}
	}
	return res[ver][v];
}

void Solve()
{
	memset(res, 0xFF, sizeof(res));
	int r = Count(1, v);
	if (r == 1000000000) printf("IMPOSSIBLE");
	else printf("%d", r);
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