#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

int H, W, A[128][128];
int Res[128][128];

char cur_ch = 'a';

const int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int dfs(int x, int y)
{
	int ret = Res[x][y];
	int best = -1, bestA = A[x][y];
	for (int d = 0; d < 4; d++)
	{
		int nx = x + dir[d][0], ny = y + dir[d][1];
		if (nx >= 0 && nx < H && ny >= 0 && ny < W)
		{
			if (A[nx][ny] < bestA)
			{
				bestA = A[nx][ny];
				best = d;
			}
		}
	}
	if (best != -1)
	{
		int ch = dfs(x + dir[best][0], y + dir[best][1]);
		if (ch < ret)
			ret = ch;
	}
	return ret;
}

void set(int x, int y, int ch)
{
	Res[x][y] = ch;
	int best = -1, bestA = A[x][y];
	for (int d = 0; d < 4; d++)
	{
		int nx = x + dir[d][0], ny = y + dir[d][1];
		if (nx >= 0 && nx < H && ny >= 0 && ny < W)
		{
			if (A[nx][ny] < bestA)
			{
				bestA = A[nx][ny];
				best = d;
			}
		}
	}
	if (best != -1)
		set(x + dir[best][0], y + dir[best][1], ch);
}

int main()
{
	freopen("f:\\B-small-attempt0.in", "r", stdin);
	freopen("f:\\B-small.out1", "w", stdout);
	int T, t_case = 1;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d %d", &H, &W);
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				scanf("%d", &A[i][j]);
		cur_ch = 'a';

		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				Res[i][j] = 150;

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				if (Res[i][j] == 150)
				{
					int ch = dfs(i, j);
					if (ch == 150) ch = cur_ch++;
					set(i, j, ch);
				}
			}
		}
		
		printf("Case #%d:\n", t_case++);
		for (int i = 0; i < H; i++)
		{
			bool first = true;
			for (int j = 0; j < W; j++)
			{
				if (!first) printf(" ");
				first = false;
				printf("%c", Res[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
