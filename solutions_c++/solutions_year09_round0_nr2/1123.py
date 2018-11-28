#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int h, w;
int ma[110][110];

void Load()
{
	scanf("%d%d", &h, &w);
	int i, j;
	for (i = 0; i < h; i++)
	{
		for (j = 0; j < w; j++)
		{
			scanf("%d", &ma[i][j]);
		}
	}
}

class Edge
{
public:
	int be, en;
};

int first[11000];
int next[21000];
Edge edg[21000];
int ne;

void AddEdge(int v1, int v2)
{
	edg[ne].be = v1;
	edg[ne].en = v2;
	next[ne] = first[v1];
	first[v1] = ne;
	ne++;
}

const int di[4] = {-1, 0, 0, 1};
const int dj[4] = {0, -1, 1, 0};

char was[110][110];
char ccom;
          
void Dfs(int v)
{
	int i;
	was[v / w][v % w] = ccom;
	for (i = first[v]; i != -1; i = next[i])
	{
		int nv = edg[i].en;
		if (was[nv / w][nv % w] == 0) Dfs(nv);
	}
}

void Solve()
{
	ne = 0;
	memset(first, 0xFF, sizeof(first));
	int i, j, ni, nj;
	for (i = 0; i < h; i++)
	{
		for (j = 0; j < w; j++)
		{
			int cmin = 2000000000;
			int mk = -1;
			int k;
			for (k = 0; k < 4; k++)
			{
				ni = i + di[k];
				nj = j + dj[k];
				if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
				if (ma[ni][nj] >= ma[i][j]) continue;
				if (ma[ni][nj] < cmin)
				{
					cmin = ma[ni][nj];
					mk = k;
				}
			}
			if (mk != -1)
			{
				AddEdge(i * w + j, (i + di[mk]) * w + j + dj[mk]);
				AddEdge((i + di[mk]) * w + j + dj[mk], i * w + j);
			}
		}
	}
	memset(was, 0, sizeof(was));
	ccom = 'a' - 1;
	for (i = 0; i < h; i++)
	{
		for (j = 0; j < w; j++)
		{
			if (was[i][j] == 0)
			{
				ccom++;
				Dfs(i * w + j);
			}
		}
	}
	for (i = 0; i < h; i++)
	{
		printf("\n");
		for (j = 0; j < w; j++)
		{
			printf("%c ", was[i][j]);
		}
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d:", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}