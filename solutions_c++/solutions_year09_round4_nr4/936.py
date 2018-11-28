#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxn 50
#define eps 1e-10
#define PI 3.1415926535897932384626433832795

int x[maxn], y[maxn], r[maxn];

double dx[500];
double dy[500];
int dirs;

struct cir
{
	double x, y, r;
	cir(double x, double y, double r) : x(x), y(y), r(r) {}
};

int n;
int cnt;
LL mask[20000];
double rad[20000];

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt(SQR(x1-x2) + SQR(y1-y2));
}

void add(cir c)
{
	LL m = 0;
	FOR(i, n) if (dist(c.x, c.y, x[i], y[i]) + r[i] <= c.r + 10.0*eps) m |= 1<<i;
	rad[cnt] = c.r;
	mask[cnt++] = m;
}

void add2(int i, int j)
{

	double d = dist(x[i], y[i], x[j], y[j]);
	rad[cnt] = max((double)r[i], r[j] - d) + d + max((double)r[j], r[i] - d);
	rad[cnt] /= 2;
	mask[cnt++] = (1<<i) | (1<<j);
	return;
	


	double X = (x[i] + x[j]) / 2.0;
	double Y = (y[i] + y[j]) / 2.0;
	double R = max( dist(X,Y,x[i],y[i]) + r[i], dist(X,Y,x[j],y[j]) + r[j] );


	for (double step = 100.0; step > eps; step *= 0.5)
	{
		while (1)
		{
			double bestr = 1e15;
			double bestx, besty;
			FOR(dir, dirs)
			{
				double x1 = X + dx[dir] * step;
				double y1 = Y + dy[dir] * step;
				double r1 = max( dist(x1,y1,x[i],y[i]) + r[i], dist(x1,y1,x[j],y[j]) + r[j] );
				if (r1 < bestr)
				{
					bestr = r1;
					bestx = x1;
					besty = y1;
				}
			}
			if (bestr >= R - eps)
				break;
			else
			{
				X = bestx;
				Y = besty;
				R = bestr;
			}
		}
	}
	add(cir(X,Y,R));
}

void add3(int i, int j, int k)
{
	double X = (x[i] + x[j] + x[k]) / 3.0;
	double Y = (y[i] + y[j] + y[k]) / 3.0;
	double R = max( dist(X,Y,x[i],y[i]) + r[i], dist(X,Y,x[j],y[j]) + r[j] );
	R = max(R, dist(X,Y,x[k],y[k]) + r[k]);

	for (double step = 100.0; step > eps; step *= 0.5)
	{
		while (1)
		{
			double bestr = 1e15;
			double bestx, besty;
			FOR(dir, dirs)
			{
				double x1 = X + dx[dir] * step;
				double y1 = Y + dy[dir] * step;
				double r1 = max( dist(x1,y1,x[i],y[i]) + r[i], dist(x1,y1,x[j],y[j]) + r[j] );
				r1 = max(r1, dist(X,Y,x[k],y[k]) + r[k]);
				if (r1 < bestr)
				{
					bestr = r1;
					bestx = x1;
					besty = y1;
				}
			}
			if (bestr >= R - eps)
				break;
			else
			{
				X = bestx;
				Y = besty;
				R = bestr;
			}
		}
	}
	add(cir(X,Y,R));
}

void solvecase() {
	scanf("%d", &n);

	dirs = 50;
	double da = (2*PI)/dirs;
	double alpha = 0;
	for (int i = 0; i < dirs; i++)
	{
		dx[i] = cos(alpha);
		dy[i] = sin(alpha);
		alpha+=da;
	}

	FOR(i, n) scanf("%d%d%d", &x[i], &y[i], &r[i]);
	
		cnt = 0;
		FOR(i, n) add(cir(x[i], y[i], r[i]));
		FOR(i, n) FOR(j, i)
			add2(i, j);
		FOR(i, n) FOR(j, i) FOR(l, j)
			//add3(i, j, l);
			;
			
		LL all = (1ll<<n)-1;
		double res = 1e15;
		FOR(i, cnt)
			FOR(j, i+1)
				if ((mask[i] | mask[j]) == all)
				{
					res = min(res, max(rad[i], rad[j]));
				}
		printf("%.8lf", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("D-small-attempt3.in", "rt", stdin);
	//freopen("D-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}