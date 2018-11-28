#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef pair<int, int> ii;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};


int fld[105][105];
int h, w;

int dp[105][105];

int last;
int solve(int x, int y)
{
	if (dp[x][y] != -1) return dp[x][y];
	
	int mx = 104, my = 104;
	fld[104][104] = 1123333;
	for (int i = 0; i < 4; ++i)
		if (x+dx[i] >= 0 && x+dx[i] < w && y+dy[i] >= 0 && y+dy[i] < h)
		if (fld[x+dx[i]][y+dy[i]] < fld[mx][my])
		{
			mx = x+dx[i];
			my = y+dy[i];
		}
	if (fld[mx][my] >= fld[x][y])
		dp[x][y] = last++;
	else dp[x][y] = solve(mx, my);
	return dp[x][y];
}

char s[30];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int test;
	cin >> test;
	for (int t = 0; t < test; ++t)
	{
		cin >> h >> w;
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				cin >> fld[j][i];
		memset(dp, -1, sizeof(dp));
		last = 0;
		for (int i = 0; i < w; ++i)
			for (int j = 0; j < h; ++j)
				solve(i, j);
		char lch = 'a';
		memset(s, 0, sizeof(s));
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				if (s[dp[j][i]] == 0)
					s[dp[j][i]] = lch++;
		cout << "Case #" << t+1 <<  ":\n";
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				cout << s[dp[j][i]];
				if (j < w-1) cout << ' ';
			}
			cout << endl;
		}
	}
}