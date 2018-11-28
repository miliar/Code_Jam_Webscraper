// CodeJam2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <queue>
using namespace std;

int maze[102][102];
int id[102][102];
int out_id[102][102];
vector<int> in_id[102][102];

int dir[4][2] = {-1,0, 0,-1, 0,1, 1,0};

queue<int> q;

int main()
{
	freopen("c:\\B-small-attempt0.in", "r", stdin);
	freopen("c:\\B-small-attempt0.out", "w+", stdout);

	int i, j, k, l, m, n,c;
	int T, H, W;
	scanf("%d", &T);
	for(c = 0;c < T; c++)
	{
		scanf("%d%d", &H, &W);
		for(j = 0;j < H; j++)
		{
			for(k = 0;k < W; k++)
			{
				scanf("%d", &maze[j][k]);
				in_id[j][k].clear();
			}
		}
		m = 1000000;

		memset(out_id, -1, sizeof(out_id));

		for(i = 0;i < H; i++)
		{
			for(j = 0;j < W; j++)
			{
				int lowx = i, lowy = j;
				for(k = 0;k < 4; k++)
				{
					int xx = i + dir[k][0];
					int yy = j + dir[k][1];
					if(xx < 0 || yy < 0 || xx >= H || yy >= W)
					{
						continue;
					}
					if(maze[lowx][lowy] > maze[xx][yy])
						lowx = xx, lowy = yy;
				}

				if(lowx == i && lowy == j) continue;
				out_id[i][j] = lowx*W + lowy;
				in_id[lowx][lowy].push_back(i*W + j);
			}
		}

		for(i = 0;i < H; i++)
		{
			for(j = 0;j < W; j++)
			{
				if(out_id[i][j] == -1)
				{
					while(!q.empty()) q.pop();
					q.push(i*W+j);
					id[i][j] = m;
					while(!q.empty())
					{
						int tmp = q.front();
						q.pop();
						int x = tmp/W, y = tmp%W;
						for(k = 0;k < in_id[x][y].size(); k++)
						{
							int xx = in_id[x][y][k]/W, yy = in_id[x][y][k]%W;
							id[xx][yy] = m;
							q.push(in_id[x][y][k]);
						}
					}
					m++;
				}
			}
		}

		int n_id = 0;
		for(i = 0;i < H; i++)
		{
			for(j = 0;j < W; j++)
			{
				if(id[i][j] < 100) continue;
				m = id[i][j];
				id[i][j] = n_id;
				for(k = 0;k < H; k++)
				{
					for(l = 0;l < W; l++)
					{
						if(id[k][l] == m)
						{
							id[k][l] = n_id;
						}
					}
				}
				n_id++;
			}
		}

		printf("Case #%d:\n", c+1);
		for(i = 0;i < H; i++)
		{
			for(j = 0;j < W-1; j++)
			{
				printf("%c ", id[i][j]+'a');
			}
			printf("%c\n", id[i][j]+'a');
		}
		
	}
	
	return 0;
}

