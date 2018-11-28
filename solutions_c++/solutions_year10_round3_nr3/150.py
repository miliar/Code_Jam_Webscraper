// C.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int T, N, M, x;
vector< vector< int > > mas;

int board(int x, int y)
{
	int r = 0;
	bool good = true;
	while (good)
	{
		r++;
		for (int i = x; i <= x + r; i++)
		{
			if (mas[i][y + r] == 0 && mas[i][y + r - 1] == 1 || mas[i][y + r] == 1 && mas[i][y + r - 1] == 0)
			{
			}
			else
			{
				good = false;
			}
		}
		for (int i = y; i <= y + r; i++)
		{
			if (mas[x + r][i] == 0 && mas[x + r - 1][i] == 1 || mas[x + r][i] == 1 && mas[x + r - 1][i] == 0)
			{
			}
			else
			{
				good = false;
			}
		}
	}
	return r;
}

void fill(int x, int y, int s)
{
	for (int i = x; i < x + s; i++)
	{
		for (int j = y; j < y + s; j++)
		{
			mas[i][j] = -1;
		}
	}
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d %d", &M, &N);
		mas.clear();
		mas.resize(M + 2);
		mas[0].assign(N + 2, -1);
		for (int i = 0; i < M; i++)
		{
			mas[i + 1].resize(N + 2);
			mas[i + 1][0] = -1;
			mas[i + 1][N + 1] = -1;
			scanf("%x", &x);
			for (int j = N - 1; j >= 0; j--)
			{
				mas[i + 1][j + 1] = x & 1;
				x >>= 1;
				//printf("%d", mas[i + 1][j + 1]);
			}
			//printf("\n");
		}
		mas[M + 1].assign(N + 2, -1);
		vector< pair< int, int > > result;
		bool ok = true;
		while (ok)
		{
			int maxsize = -1;
			int mx = 0, my = 0;

			for (int i = 0; i < M; i++)
			{
				for (int j = 0; j < N; j++)
				{
					if (mas[i + 1][j + 1] != -1)
					{
						int size = board(i + 1, j + 1);
						if (size > maxsize)
						{
							maxsize = size;
							mx = i + 1;
							my = j + 1;
						}
					}
				}
			}
			if (maxsize != -1)
			{
				if (!result.empty() && maxsize == result[result.size() - 1].first)
				{
					result[result.size() - 1].second++;
				}
				else
				{
					result.resize(result.size() + 1);
					result[result.size() - 1].first = maxsize;
					result[result.size() - 1].second = 1;
				}
				fill(mx, my, maxsize);
			}
			else
			{
				ok = false;
			}
		}
		printf("Case #%d: %d\n", t + 1, result.size());
		for (int i = 0; i < (int)result.size(); i++)
		{
			printf("%d %d\n", result[i].first, result[i].second);
		}
	}
	return 0;
}

