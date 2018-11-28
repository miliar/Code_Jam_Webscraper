#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <iostream>

using namespace std;

#define MAXN 10010

const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int p[MAXN];
int rank[MAXN];
bool visited[MAXN];

void preprocess()
{
	memset(rank, 0, sizeof(rank));
	memset(visited, 0, sizeof(visited));
	for (int i = 0; i < MAXN; i++)
		p[i] = i;
}

int g[110][110];
char res[110][110];

inline int mymap(int i, int j, int W)
{
	return i * W + j;
}

int find_set(int i)
{
	if (i == p[i])
		return i;
	else return p[i] = find_set(p[i]);
}

void union_set(int i, int j)
{
	int t = find_set(i);
	int r = find_set(j);
	if (t != r)
	{
		if (rank[t] > rank[r])
		{
			p[r] = t;
		}
		else
		{
			p[t] = r;
			if (rank[t] == rank[r])
				rank[r]++;
		}
	}
}

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
	int t, T, i, j, k, H, W;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d%d", &H, &W);
		preprocess();
		for (i = 0; i < H; i++)
		{
			for (j = 0; j < W; j++)
				scanf("%d", &g[i][j]);
		}
		for (i = 0; i < H; i++)
		{
			for (j = 0; j < W; j++)
			{
				int m = MAXN;
				int x1 = -1, y1 = -1;
				for (k = 0; k < 4; k++)
				{
					int x = i + dir[k][0];
					int y = j + dir[k][1];
					if (x >= 0 && x < H && y >= 0 && y < W)
					{
						if (g[i][j] > g[x][y])
						{
							if (m > g[x][y])
							{
								m = g[x][y];
								x1 = x;
								y1 = y;
							}
						}
					}
				}
				if (m != MAXN)
				{
					union_set(mymap(i, j, W), mymap(x1, y1, W));
				}
			}
		}
		char cur = 'a';
		int i1, j1;
		for (i = 0; i < H * W; i++)
		{
			for (j = 0; j < i; j++)
			{
				if (find_set(i) == find_set(j))
				{
					res[i / W][i % W] = res[j / W][j % W];
					break;
				}
			}
			if (i == j)
			{
				res[i / W][i % W] = cur;
				cur++;
			}
		}
		printf ("Case #%d:\n", t);
		for (i = 0; i < H; i++)
		{
			for (j = 0; j < W; j++)
			{
				if (j != 0)
					printf (" ");
				printf ("%c", res[i][j]);
			}
			printf ("\n");
		}
	}
	return 0;
}