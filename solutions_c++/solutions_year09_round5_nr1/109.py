#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

typedef long double ld;
typedef long long ll;
const double pi = M_PI;

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

int n, m;
char a[13][13];
int used[13][13];
int b[13][13];
int iter;

struct Point
{
	int x, y;
};

inline bool operator<(const Point& a, const Point& b)
{
	return a.x < b.x || ((a.x == b.x) && a.y < b.y);
}

inline bool operator==(const Point& a, const Point& b)
{
	return a.x == b.x && a.y == b.y;
}

bool valid(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m && a[x][y] != '#';
}


void dfs(int x, int y)
{
	used[x][y] = iter;
	forn(i, 4)
	{
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (valid(xx, yy) && used[xx][yy] != iter && a[xx][yy] == 'o') dfs(xx, yy);
	}
}

bool dang(vector<Point>& p)
{
	iter++;
	dfs(p[0].x, p[0].y);
	forv(i, p) if (used[p[i].x][p[i].y] != iter) return true;
	return false;
}


void solve(int tc)
{
	cerr << tc << endl;
	scanf("%d %d\n", &n, &m);
	forn(i, n)
	{
		forn(j, m)
		{
			scanf("%c", &a[i][j]);
		}
		scanf("\n");
	}

	vector<Point> st, fn;
	forn(i, n)
	{
		forn(j, m)
		{
			if (a[i][j] == 'x')
			{
				a[i][j] = '.';
				Point pt = {i, j};
				fn.pb(pt);
			}
			if (a[i][j] == 'o')
			{
				a[i][j] = '.';
				Point pt = {i, j};
				st.pb(pt);
			}
			if (a[i][j] == 'w')
			{
				a[i][j] = '.';
				Point pt = {i, j};
				st.pb(pt);
				fn.pb(pt);
			}
		}
	}

	map<vector<Point>, int> d;
	d[st] = 0;

	queue<vector<Point> > q;
	q.push(st);

	vector<Point> u;

	while (!q.empty())
	{
		vector<Point> v = q.front(); q.pop();
		vector<Point> tmp = v;
		sort(all(tmp));
		if (tmp == fn)
		{
			printf("Case #%d: %d\n", tc, d[v]);
			return;
		}
		forv(i, v) a[v[i].x][v[i].y] = 'o';
		bool danger = dang(v);
		u = v;
		int dv = d[v];
		forv(i, v)
		{
			Point p = v[i];
			forn(j, 4)
			{
				int x = p.x + dx[j];
				int y = p.y + dy[j];
				if (!valid(x, y)) continue;
				if (!valid(p.x - dx[j], p.y - dy[j])) continue;
				if (a[x][y] == 'o') continue;
				if (a[p.x - dx[j]][p.y - dy[j]] == 'o') continue;
				a[p.x][p.y] = '.';
				a[x][y] = 'o';
				u[i].x = x;
				u[i].y = y;
				if (!dang(u))
				{
					if (!d.count(u)) 
					{
						d[u] = dv + 1;
						q.push(u);
					}
				} else if (!danger)
				{
					if (!d.count(u))
					{
						d[u] = dv + 1;
						q.push(u);
					}
				}
				u[i] = v[i];
				a[x][y] = '.';
				a[p.x][p.y] = 'o';
			}
		}
		forv(i, v) a[v[i].x][v[i].y] = '.';
	}
	printf("Case #%d: %d\n", tc, -1);
}

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) solve(it+1);

	return 0;
}