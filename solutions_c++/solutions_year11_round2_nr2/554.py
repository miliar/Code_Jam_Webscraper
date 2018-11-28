#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;

int n, d;
int all;
pii a[205];
void Load()
{
	scanf("%d%d", &n, &d);
	all = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &a[i].fi, &a[i].se);
		all += a[i].se;
	}	
}

inline ldb dist(ldb a, ldb b)
{
	return fabs(a - b);
}

ldb pos[1000005];
inline bool good(ldb t)
{
	int cur = 0;
	for (int i = 0; i < n; i++)
	{
		if (i > 0 && (dist(pos[cur - 1], a[i].fi - t) < d + eps || (a[i].fi - t < pos[cur - 1] + eps)))
		{
			if (dist(pos[cur - 1] + d, a[i].fi) - eps > t) return false;
			pos[cur] = pos[cur - 1] + d;
			cur++;
		}
		else
		{
			pos[cur] = a[i].fi - t;
			cur++;
		}
		for (int j = 1; j < a[i].se; j++)
		{
			if (dist(pos[cur - 1] + d, a[i].fi) - eps > t) return false;
			pos[cur] = pos[cur - 1] + d;
			cur++;
		}
	}
	sort(pos + 0, pos + cur);
	for (int i = 1; i < cur; i++)
		if (dist(pos[i - 1], pos[i]) + eps < d) return false;
	return true;	
}

const int maxit = 50;
void Solve()
{
	ldb lo = 0.0, hi = 1e8;
	ldb md;
	for (int it = 0; it < maxit; it++)
	{
		md = (lo + hi) / 2.0;
		if (good(md))
			hi = md;
		else
			lo = md;	
	}
	//cerr << lo << endl;
	printf("%.10lf", (double)hi);
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
