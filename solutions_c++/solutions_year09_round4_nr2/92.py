#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int oo = 5000;
int m, n, d;
int maze[16];
int dp[16][1 << 8][8];

inline bool is_set(int x, int b)
{
	return (x & (1 << b)) != 0;
}

void jump(int row, int col, int act, int conf, int dep = 1)
{
	if (dep > d)
		return;
//	cout << "jump " << row << " " << col << " " << act << " " << dep << endl;
	if (row == m-1 || is_set(maze[row+1], col))
		dp[row][conf][col] = min(dp[row][conf][col], act);
	else
		jump(row+1, col, act, maze[row+1], dep+1);
}

void proceed(int row, int conf, int col, int act)
{
	int min_col = col, max_col = col;
//	cout << "proceed " << row << " " << col << " " << conf << endl;
	while (min_col > 0 && !is_set(conf, min_col-1) && is_set(maze[row+1], min_col-1))
		min_col--;
	while (max_col < n-1 && !is_set(conf, max_col+1) && is_set(maze[row+1], max_col+1))
		max_col++;

	if (min_col > 0 && !is_set(conf, min_col-1) && !is_set(maze[row+1], min_col-1))
		jump(row+1, min_col-1, act, maze[row+1]);
	if (max_col < n-1 && !is_set(conf, max_col+1) && !is_set(maze[row+1], max_col+1))
		jump(row+1, max_col+1, act, maze[row+1]);

//	cout << min_col << " -- " << max_col << endl;
	for (int y = 0; y < (1 << (max_col+1)); y += (1 << min_col))
	{
//		cout << "dig " << y << endl;
		int cnt = 0;
		for (int i = min_col; i <= max_col; i++)
			if (is_set(y, i))
				cnt++;
		if (!cnt || cnt == max_col - min_col + 1)
			continue;
		for (int i = min_col; i <= max_col; i++)
			if (is_set(y, i))
				jump(row+1, i, act + cnt, maze[row+1] ^ y);
	}
}

char* print_conf(int x)
{
	static char result[32];
	for (int i = 0; i < n; i++)
		result[i] = (x & (1 << i)) ? '#' : '.';
	result[n] = 0;
	return result;
}

int bits(char s[])
{
	int res = 0;
	reverse(s, s+n);
	for (int i = 0; s[i]; i++)
	{
		res <<= 1;
		if (s[i] == '#')
			res++;
	}
	return res;
}

int main()
{
	int kases;
	scanf("%d", &kases);
	for (int kase = 1; kase <= kases; kase++)
	{
		scanf("%d%d%d", &m, &n, &d);
		for (int i = 0; i < m; i++)
		{
			char s[16];
			scanf(" %s", s);
			maze[i] = bits(s);
		}

		memset(dp, 0x0F, sizeof(dp));
		dp[0][maze[0]][0] = 0;

		for (int l = 0; l < m-1; l++)
			for (int x = 0; x < (1 << n); x++)
				for (int c = 0; c < n; c++)
					if (dp[l][x][c] < oo)
					{
//						cout << l << " " << c << " " << print_conf(x) << ": " << dp[l][x][c] << endl;
//						printf("%d %d %s: %d\n", l, c, print_conf(x).c_str(), dp[l][x][c]);
						proceed(l, x, c, dp[l][x][c]);
					}

//		cout << dp[3][maze[3]][4] << endl;
//		cout << is_set(maze[4], 4) << endl;

		int res = oo;
		for (int x = 0; x < (1 << n); x++)
			for (int c = 0; c < n; c++)
				res = min(res, dp[m-1][x][c]);
		printf("Case #%d: ", kase);
		if (res < oo)
			printf("Yes %d\n", res);
		else
			printf("No\n");
	}
	return 0;
}
