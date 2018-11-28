#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define CL(x) memset(x, 0, sizeof(x));

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

int n, k;
char a[60][60];
char b[60][60];

void Rot()
{
	FOR(i, n)
		FOR(j, n)
			b[j][n - 1 - i] = a[i][j];
	FOR(i, n)
		FOR(j, n)
		a[i][j] = b[i][j];
}

bool Win0(int x, int y, int dx, int dy, char c)
{
	int cnt = 0;
	while (x >= 0 && x < n && y >= 0 && y < n && cnt < k && a[x][y] == c)
	{
		cnt++;
		x += dx;
		y += dy;
	}
	return cnt == k;
}

bool Win(char c)
{
	FOR(i, n)
		FOR(j, n)
	{
		if (Win0(i, j, 0, 1, c)) return 1;
		if (Win0(i, j, 1, 0, c)) return 1;
		if (Win0(i, j, 1, 1, c)) return 1;
		if (Win0(i, j, 1, -1, c)) return 1;
	}
	return 0;
}

void Solve()
{
	scanf("%d %d", &n, &k);
	FOR(i, n)
		scanf("%s", a[i]);
	Rot();
	FOR(i, n)
	{
		int p = n - 1;
		for (int j = n - 1; j >= 0; j--)
			if (a[j][i] != '.')
				a[p--][i] = a[j][i];
		while (p >= 0)
		{
			a[p][i] = '.';
			p--;
		}
	}
	bool wr = Win('R');
	bool wb = Win('B');
	if (wr && wb)
	{
		printf("Both\n");
		return;
	}
	if (wr)
	{
		printf("Red\n");
		return;
	}
	if (wb)
	{
		printf("Blue\n");
		return;
	}
	printf("Neither\n");
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}