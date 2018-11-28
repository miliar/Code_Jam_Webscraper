#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "gcj";

int N,n,m;
int h[311][311];
char c[311][311];
char dir[311][311];

int cnt = 0;
void Rec(int i, int j, char color)
{
	++cnt;
	if (i<0 || i>=n || j<0 || j>=m || c[i][j] != -1)
		return;
	c[i][j] = color;
	if (dir[i][j] == 'N') Rec(i-1, j, color);
	if (dir[i][j] == 'S') Rec(i+1, j, color);
	if (dir[i][j] == 'W') Rec(i, j-1, color);
	if (dir[i][j] == 'E') Rec(i, j+1, color);

	if (i<n-1 && dir[i+1][j] == 'N') Rec(i+1, j, color);
	if (i>0   && dir[i-1][j] == 'S') Rec(i-1, j, color);
	if (j<m-1 && dir[i][j+1] == 'W') Rec(i, j+1, color);
	if (j>0   && dir[i][j-1] == 'E') Rec(i, j-1, color);
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &N);
	for (int I=1; I<=N; ++I)
	{
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				scanf("%d", &h[i][j]);
		memset(c, -1, sizeof c);

		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
			{
				int cur = 1000000000;
				dir[i][j] = '-';
				
				if (i>0 && h[i-1][j] < h[i][j] && h[i-1][j] < cur)
					dir[i][j] = 'N',
					cur = h[i-1][j];
				
				if (j>0 && h[i][j-1] < h[i][j] && h[i][j-1] < cur)
					dir[i][j] = 'W',
					cur = h[i][j-1];
				
				if (j<m-1 && h[i][j+1] < h[i][j] && h[i][j+1] < cur)
					dir[i][j] = 'E',
					cur = h[i][j+1];
				
				if (i<n-1 && h[i+1][j] < h[i][j] && h[i+1][j] < cur)
					dir[i][j] = 'S',
					cur = h[i+1][j];
			}

		char col = 'a';
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				if (c[i][j] == -1)
					Rec(i, j, col++);

		printf("Case #%d:\n", I);
		for (int i=0; i<n; ++i)
		{
			for (int j=0; j<m; ++j)
				printf("%c ", c[i][j]);
			printf("\n");
		}
	}

	return 0;
} 