#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 1000 + 10;
int b[N], e[N], w[N];
int p[3*N];
int pw[3*N];
int x, s, r, t, n;

//double calc(double tt)
//{
//	double ret = 0;
//	ret += min(tt, t*1.0) * (r-s);
//	ret += tt * s;
//	for (int i = 0; i <
//}
struct D
{
	int b, e, w;
};
D d[N];
bool cmp(D d1, D d2)
{
	return d1.w < d2.w;
}
double work()
{
	
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	int cnt = 0;
	int slen = 0;
	d[0].e = 0;
	for (int i = 1; i <= n; i++)
	{
		//scanf("%d%d%d", &b[i], &e[i], &w[i]);
		scanf("%d%d%d", &d[i].b, &d[i].e, &d[i].w);
		slen += d[i].b - d[i-1].e;
	}
	slen += x - d[n].e;
	n++;
	d[n].b = 0; d[n].e = slen; d[n].w = 0;

	sort(d+1, d+1+n, cmp);

	double eps = 1e-9;
	
	double totaltime = 0;

	for (int i = 1; i <= n; i++)
	{
		double curpos = d[i].b;
		double sdis = d[i].e - d[i].b;
		if (totaltime + eps < t)
		{
			if ((t - totaltime) * (r+d[i].w) > sdis)
			{
				totaltime += sdis / (r+d[i].w);
			}
			else
			{
				curpos = curpos + (r+d[i].w) * (t-totaltime);
				totaltime = t;
				totaltime += (d[i].e - curpos) / (s + d[i].w);
				curpos = d[i].e;
			}
		}
		else
		{
			totaltime += sdis / (s+d[i].w);
		}
	}
	return totaltime;
	//double left = 0, right = 1e9;
	//double eps = 1e-9;
	//while (left + eps < right)
	//{
	//	double mid = (left + right) / 2;
	//	double tmid = calc(mid);
	//	if (tmid > x)
	//		rigt = mid;
	//	else
	//		left = mid;
	//}
	//return left;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		double ret = work();
		printf("Case #%d: %.8f\n", testcase, ret);
	}
}