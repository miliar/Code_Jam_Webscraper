#define _CRT_SECURE_NO_DEPRECATE
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

void ASS(bool b)
{
	if (!b)
	{
		++*(int*)0;
	}
}

int n;

int d[128][128][128];
char s[128];
int p[128];
queue<int> q;

void add(int z, int x, int y, int dd)
{
	if (x > 0 && x < 101 && y > 0 && y < 101 && d[z][x][y] == 0)
	{
		d[z][x][y] = dd;
		q.push(z);
		q.push(x);
		q.push(y);
	}
}

int Solve()
{
	cin >> n;
	FOR(i, n)
	{
		char buf[16];
		scanf("%s", buf);
		ASS(buf[0] == 'O' || buf[0] == 'B');
		s[i] = buf[0] == 'O';
		cin >> p[i];
	}
	FOR(z, n + 1)
		FOR(i, 102)
			FOR(j, 102)
				d[z][i][j] = 0;
	while (!q.empty())
		q.pop();
	add(0, 1, 1, 1);
	while (!q.empty())
	{
		int z = q.front();
		q.pop();
		int x = q.front();
		q.pop();
		int y = q.front();
		q.pop();
		int dd = d[z][x][y] + 1;
		if (z == n)
			return dd - 2;
		if (s[z])
		{
			if (p[z] == x)
			{
				add(z + 1, x, y, dd);
				add(z + 1, x, y - 1, dd);
				add(z + 1, x, y + 1, dd);
			}
		}
		else
		{
			if (p[z] == y)
			{
				add(z + 1, x, y, dd);
				add(z + 1, x - 1, y, dd);
				add(z + 1, x + 1, y, dd);
			}
		}
		for (int dx = -1; dx <= 1; dx++)
			for (int dy = -1; dy <= 1; dy++)
				add(z, x + dx, y + dy, dd);
	}
	ASS(0);
	return -1;
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	cin >> t;
	FOR(i, t)
	{
		int res = Solve();
		printf("Case #%d: %d\n", i + 1, res);
	}

	return 0;
}