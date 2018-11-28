#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

#pragma comment(linker, "/STACK:16777216")

struct Room
{
	int n;
	int a[8];

	Room()
	{
		n = 0;
	}

	void add(int x)
	{
		a[n] = x;
		++n;
	}

	bool split(Room& r1, Room& r2, int x, int y)
	{
		r1.n = 0;
		r2.n = 0;
		for(int i = 0; i < n; ++i)
		{
			int z = i;
			for(int j = 1; j <= n; ++j)
			{
				z = (z + 1) % n;
				if (a[i] == x && a[z] == y && min(abs(z - i), n - abs(z - i)) > 1)
				{
					for(int k = 0; k <= j; ++k)
					{
						r1.add(a[(i + k) % n]);
					}
					for(int k = j; k <= n; ++k)
					{
						r2.add(a[(i + k) % n]);
					}
					return true;
				}
			}
		}
		return false;
	}
};

const int nmax = 16;

int wall[nmax][2];

queue<Room> q;
Room r[nmax];
int c[nmax];
int qq;
int cnt;
int n;

bool check(int i)
{
	bool b[nmax];
	memset(b, 0, sizeof(b));
	for(int j = 0; j < r[i].n; ++j)
	{
		b[c[r[i].a[j]]] = true;
	}
	for(int i = 0; i < qq; ++i)
	{
		if (!b[i])
		{
			return false;
		}
	}
	return true;
}

bool check()
{
	for(int i = 0; i < cnt; ++i)
	{
		if (!check(i))
		{
			return false;
		}
	}
	return true;
}

bool found;

void f(int d)
{
	if (found)
	{
		return;
	}
	if (d == n)
	{
		if (check())
		{
			found = true;
		}
		return;
	}
	for(int i = 0; i < qq && !found; ++i)
	{
		c[d] = i;
		f(d + 1);
	}
}

void solveTest()
{
	int m;
	scanf("%d%d", &n, &m);
	Room rt;
	for(int i = 0; i < n; ++i)
	{
		rt.add(i);
	}
	for(int i = 0; i < m; ++i)
	{
		scanf("%d", &wall[i][0]);
		--wall[i][0];
	}
	for(int i = 0; i < m; ++i)
	{
		scanf("%d", &wall[i][1]);
		--wall[i][1];
	}

	q.push(rt);
	cnt = 0;
	while(!q.empty())
	{
		rt = q.front();
		q.pop();
		Room r1, r2;
		bool f = true;
		for(int i = 0; i < m; ++i)
		{
			if (rt.split(r1, r2, wall[i][0], wall[i][1]))
			{
				q.push(r1);
				q.push(r2);
				f = false;
				break;
			}
		}
		if (f)
		{
			r[cnt] = rt;
			++cnt;
		}
	}
	int mx = 0;
	for(int i = 0; i < cnt; ++i)
	{
		mx = max(mx, r[i].n);
	}

	for(int i = mx; i > 0; --i)
	{
		found = false;
		qq = i;
		f(0);
		if (found)
		{
			break;
		}
	}
	printf("%d\n", qq);
	for(int i = 0; i < n; ++i)
	{
		printf("%d%c", c[i] + 1, i == n - 1 ? '\n' : ' ');
	}
}

int main()
{
	int t;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
		cerr << i + 1 << " Done!\n";
	}
	return 0;
}
