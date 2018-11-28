#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

struct State
{
	double time;
	int x,y,cnt;
};
bool operator < (const State &a,const State &b)
{
	return a.time < b.time || a.time == b.time && a.x < b.x
		|| a.time == b.time && a.x == b.x && a.y < b.y || 
		a.time == b.time && a.x == b.x && a.y == b.y && a.cnt < b.cnt;
}

const int nmax = 105;
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
double d[nmax][nmax][5];
int L[nmax][nmax],R[nmax][nmax];
bool used[nmax][nmax];
double happyTime[nmax][nmax];
int n,m,h;
set < State > q;

void read()
{
	scanf("%d%d%d",&h,&n,&m);
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			scanf("%d",&R[i][j]);
		}
	}
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			scanf("%d",&L[i][j]);
		}
	}
	_(used,0);
	q.clear();
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			for (int k = 0; k < 5; k ++)
			{
				d[i][j][k] = INF;
			}
		}
	}
}

bool in(int x,int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool can(double t,int x,int y,int nx,int ny)
{
	if (!in(nx,ny))
		return false;

	double w = max( (double)L[x][y], (double)h - t * 10.0);
	double nw = max( (double)L[nx][ny], (double) h - t * 10.0);
	
	return w + 50.0 - eps <= R[nx][ny] &&
		L[x][y] + 50.0 - eps <= R[nx][ny] &&
		L[nx][ny] + 50.0 - eps <= R[nx][ny] &&
		L[nx][ny] + 50.0 - eps <= R[x][y];
}

void upd(int x,int y,int cnt,double t)
{
	State cur;
	cur.x = x;
	cur.y = y;
	cur.cnt = cnt;
	cur.time = d[x][y][cnt];
	if (d[x][y][cnt] > t)
	{
		q.erase(cur);
		d[x][y][cnt] = cur.time = t;
		q.insert(cur);
	}
}

int calc(int x,int y,double t)
{
	int ret = 0;
	for (int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (can(t,x,y,nx,ny))
		{
			ret++;
		}
	}
	return ret;
}

void init(int x,int y)
{
	if (used[x][y]) return;
	upd(x,y,calc(x,y,0),0);
	used[x][y] = true;
	for (int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (can(0,x,y,nx,ny))
		{
			init(nx,ny);
		}
	}
}

void dij()
{
	while (!q.empty())
	{
		int x = q.begin()->x;
		int y = q.begin()->y;
		double t = q.begin()->time;
		int cnt = q.begin()->cnt;
		q.erase(q.begin());

		double lvl = max( (double)L[x][y], (double)h - t * 10.0);

		for (int i = 0; i < 4; i ++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			double cost;
			if (can(t,x,y,nx,ny))
			{
				if (lvl - L[x][y] >= 20.0)
					cost = 1.0;
				else
					cost = 10.0;
				upd(nx,ny,calc(nx,ny,t + cost),t + cost);
			}
			if (in(nx,ny))
			{
				double l = t,r = INF;
				for (int its = 0; its < 75; its ++)
				{
					double mid = (l + r) / 2.0;
					if (can(mid,x,y,nx,ny))
						r = mid;
					else
						l = mid;
				}
				upd(x,y,calc(x,y,r),r);
			}
		}
	}
}

bool solve()
{
	read();
	init(0,0);
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			happyTime[i][j] = min( 0.0, ( (double)h - (double)(R[i][j] - 50.0) ) / 10.0 );
		}
	}
	dij();
	double ans = INF;
	for (int i = 0; i < 5; i ++)
	{
		ans = min(ans, d[n-1][m-1][i]);
	}
	printf("%.1lf\n",ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		printf("Case #%d: ",i + 1);
		solve();
	}
	return 0;
}