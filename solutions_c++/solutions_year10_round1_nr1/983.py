#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>

#define sz(x) (int)(x).size()

using namespace std;
typedef vector <int> vi;
typedef vector <vi> vvi;

bool check(vvi &a, int y, int x, int k, int val)
{
	int dx[] = {0, 0, 1, -1, 1, 1, -1, -1};
	int dy[] = {1, -1, 0, 0, -1, 1, -1, 1};
	for (int i = 0; i < 8; i++)
	{
		int tx = x;
		int ty = y;
		bool ans = true;
		for (int j = 0; j < k - 1; j++)
		{
			tx += dx[i];
			ty += dy[i];
			if (tx < 0 || tx > sz(a) - 1) {ans = false; break;}
			if (ty < 0 || ty > sz(a) - 1) {ans = false; break;}
			if (a[ty][tx] != val) {ans = false; break;}
		}
		if (ans) return true;
	}
	return false;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t;
	cin >> t;
	for (int z = 0; z < t; z++)
	{
		int n, k;
		scanf("%d %d ", &n, &k);
		vvi a(n, vi(n));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				char t;
				scanf("%c ", &t);
				if (t == '.') continue;
				if (t == 'R') a[i][j] = 1;
				if (t == 'B') a[i][j] = 2;
			}
		for (int i = 0; i < n; i++) 
		{
			int kol = 0;
			for (int j = n - 1; j >= 0; j--)
			{
				if (a[i][j]) continue;
				if (kol == n) break;
				kol++;
				a[i].erase(a[i].begin() + j);
				a[i].insert(a[i].begin(), 0);
				j++;
			}
		}
		bool red = false;
		bool blue = false;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				if (!a[i][j]) continue;
				if (a[i][j] == 1 && !red) red = check(a, i, j, k, a[i][j]);
				if (a[i][j] == 2 && !blue) blue = check(a, i, j, k, a[i][j]);
			}
		printf("Case #%d: ", z + 1);
		if (red && blue)
		{
			printf("Both\n");
			continue;
		}
		if (red)
		{
			printf("Red\n");
			continue;
		}
		if (blue)
		{
			printf("Blue\n");
			continue;
		}
		printf("Neither\n");
	}
	return 0;
}