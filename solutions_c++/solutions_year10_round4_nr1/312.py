#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

const int MAX = 1024;

vector<int> A[MAX];
int n, s, M[MAX][MAX], dx, dy;

inline int get(int x, int y)
{
	if (x >= dx && y >= dy)
	{
		x -= dx; y -= dy;
		if (x < n && y < n)
			return M[x][y];
	}
	return -1;
}

bool can(int s)
{
	for (int x = s / 2; x >= 0; x--)
	{
		for (int y = s - 1; y >= 0; y--)
		{
			int has = -1, t;
			t = get(x, y);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(s - 1 - x, s - 1 - y);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(y, x);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(s - 1 - y, s - 1 - x);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;
		}
	}
	for (int x = s / 2; x < s; x++)
	{
		for (int y = s - 1; y < s; y++)
		{
			int has = -1, t;
			t = get(x, y);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(s - 1 - x, s - 1 - y);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(y, x);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;

			t = get(s - 1 - y, s - 1 - x);
			if (has == -1) has = t;
			else if (t != -1 && t != has) return false;
		}
	}
	return true;
}

bool check(int s)
{
	int Shift = s - n;
	for (dx = 0; dx <= Shift; dx++)
	{
		for (dy = 0; dy <= Shift; dy++)
		{
			if (can(s)) return true;
		}
	}
	return false;
}

int solve()
{
	for (int i = 0; i < n; i++)
	{
		int j, ct = 0;
		for (j = 1; j <= 2 * n - 1; j++)
			if (!A[j].empty()) break;
		for (; j <= 2 * n - 1 && ct < n;)
		{
			M[i][ct] = A[j + ct].back();
			A[j + ct].pop_back();
			ct++;
		}
	}
	//for (int i = 0; i < n; i++)
	//{
	//	for (int j = 0; j < n; j++)
	//		printf("%d", M[i][j]);
	//	printf("\n");
	//}
	for (s = n; ; s++)
	{
		if (check(s))
		{
			//printf("s : %d\n", s);
			return s*(s+1)/2+s*(s-1)/2 - n*(n+1)/2-n*(n-1)/2;
		}
	}
	return -1;
}

int main()
{
	freopen("f:\\A-large.in", "r", stdin);
	freopen("f:\\A-large.out", "w", stdout);

	int T, x;
	scanf("%d", &T);
	//T = 100;
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
		{
			A[i].clear();
			for (int j = 0; j < i; j++)
			{
				scanf("%d", &x);
				//x = rand() % 10;
				A[i].push_back(x);
			}
		}
		for (int i = n - 1; i >= 1; i--)
		{
			A[2 * n - i].clear();
			for (int j = 0; j < i; j++)
			{
				scanf("%d", &x);
				//x = rand() % 10;
				A[2 * n - i].push_back(x);
			}
		}
		printf("Case #%d: %d\n", t_case, solve());
		fprintf(stderr, "Case #%d: %d\n", t_case, solve());
	}
	return 0;
}
