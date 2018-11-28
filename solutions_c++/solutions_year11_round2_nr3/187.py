#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define inf 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair

#define NMax 2048

int N, M;
pii v[2048];

int ind;
short int points[128][128], st[128];
short int size[128];
int check;

inline int contains(int poly, int xx, int yy)
{
	int fx = 0, fy = 0;
	
	for (int i = 1; i <= size[poly]; ++i)
	{
		fx |= points[poly][i] == xx;
		fy |= points[poly][i] == yy;
	}
	return fx && fy;
}

void split(int poly, int xx, int yy)
{
	int i, poz1, poz2;
	
	for (i = 1; i <= size[poly]; ++i)
	{
		if (points[poly][i] == xx)
			poz1 = i;
		if (points[poly][i] == yy)
			poz2 = i;
	}
	
	++ind;
	int from = minim(poz1, poz2);
	int to = maxim(poz1, poz2);
	for (i = from; i <= to; ++i)
		points[ind][++size[ind]] = points[poly][i];
	for (i = from+1; i+to-from-1 <= size[poly]; ++i)
		points[poly][i] = points[poly][i+to-from-1];
	for (; i <= size[poly]; ++i)
		points[poly][i] = 0;
	size[poly] -= to-from-1;
}

inline int valid(int nr_c)
{
	int i, j, use[128] = {0};
	
	for (i = 1; i <= ind; ++i)
	{
		memset(use, 0, (nr_c+1) * sizeof(int));
		for (j = 1; j <= size[i]; ++j)
			use[st[points[i][j]]] = 1;
		for (j = 1; j <= nr_c; ++j)
			if (!use[j])
				return 0;
	}
	return 1;
}

void back(int nivel, int nr_col)
{
	if (nivel == N+1)
	{
		if (valid(nr_col))
			check = 1;
		return ;
	}
	
	for (int i = 1; i <= nr_col && !check; ++i)
	{
		st[nivel] = i;
		back(nivel+1, nr_col);
	}
}

int main()
{
	int T, t, i, j;
	
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		
		memset(points, 0, sizeof(points));
		memset(size, 0, sizeof(size));
		
		scanf("%d %d", &N, &M);
		for (i = 1; i <= M; ++i)
			scanf("%d", &v[i].x);
		for (i = 1; i <= M; ++i)
			scanf("%d", &v[i].y);
		
		size[ind = 1] = N;
		for (i = 1; i <= N; ++i)
			points[1][i] = i;
		
		for (i = 1; i <= M; ++i)
			for (j = 1; j <= ind; ++j)
				if (contains(j, v[i].x, v[i].y))
				{
					split(j, v[i].x, v[i].y);
					break;
				}
				
		int nr_col = N;
		for (i = 1; i <= ind; ++i)
			nr_col = minim(nr_col, size[i]);
		
		for (i = nr_col; i; --i)
		{
			check = 0;
			back(1, i);
			if (check)
				break;
		}
		
		printf("%d\n", i);
		for (i = 1; i <= N; ++i)
			printf("%d ", st[i]);
		printf("\n");
	}
	
	return 0;
}
