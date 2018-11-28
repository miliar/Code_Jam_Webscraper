// qb.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include "cstdio"

const int MAXN = 10001;

int map[100][100];
char label[100][100];
int t,h,w;

int set[MAXN],rank[MAXN] = {0};

int FindSet(int x)
{
	int p1 = x;

	while (set[p1] != p1)
	{
		p1 = set[p1];
	}
	return p1;
}

void MakeSet(int x)
{
	set[x] = x;
	rank[x] = 0;
}

void Link(int a,int b)
{
	if(rank[a] > rank[b])
	{
		set[b] = a;
	}
	else if(rank[a] < rank[b])
	{
		set[a] = b;
	}
	else
	{
		set[a] = b;
		rank[b]++;
	}
}

void Union(int a,int b)
{
	Link(FindSet(a),FindSet(b));
}

int main()
{
	freopen("e:\\B-large.txt","r",stdin);
	freopen("e:\\a.txt","w",stdout);
	int i,j,k,p,minp,ii,jj;
	int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

	scanf("%d",&t);
	for (int z = 1; z <= t; z++)
	{
		scanf("%d%d",&h,&w);

		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
			{
				scanf("%d",&map[i][j]);
			}

		for (i = 0; i < 100; i++)
			for (j = 0; j < 100; j++)
			{
				label[i][j] = '\0';
				MakeSet(i * 100 + j);
			}

		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
			{
				minp = 10000000,p = -1;
				for (k = 0; k < 4; k++)
				{
					ii = i + dir[k][0],jj = j + dir[k][1];
					if (ii < 0 || ii >= h || jj < 0 || jj >= w || map[ii][jj] >= map[i][j]) continue;
					if (map[ii][jj] < minp)
						p = k,minp = map[ii][jj];
				}

				if (p == -1) continue;
				//printf("%d %d %d %d\n",i,j,i + dir[p][0],j + dir[p][1]);
				Union(i * w + j,(i + dir[p][0]) * w + j + dir[p][1]);
			}

		printf("Case #%d: \n",z);
		char ch = 'a';
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				if (label[i][j] != '\0') 
				{
					printf("%c ",label[i][j]);
					continue;
				}
				label[i][j] = ch;
				printf("%c ",label[i][j]);

				p = i * w + j;
				for (k = p + 1; k < h * w; k++)
				{
					ii = k / w, jj = k % w;
					if (FindSet(p) == FindSet(k))
						label[ii][jj] = ch;
				}
				ch++;
			}
			printf("\n");
		}
	}

	return 0;
}

