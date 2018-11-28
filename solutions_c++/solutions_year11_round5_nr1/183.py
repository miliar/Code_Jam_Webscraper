#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>


using namespace std;

struct sVector2d
{
	double x, y;
};

int N[2];
sVector2d p[2][102];

double CalcArea(double rb)
{
	double ans = 0.0, lc = 0.0, vl = p[1][0].y - p[0][0].y;
	int pn[2];
	for (pn[0] = 0, pn[1] = 0; lc < rb - 1e-5;)
	{
		int x = 0;
		if (p[1][pn[1]+1].x < p[x][pn[x]+1].x)  x = 1;
		double ev = min(rb, p[x][pn[x]+1].x);
		double nl[2];
		for (int i = 0; i <= 1; i ++)
			nl[i] = p[i][pn[i]].y + (p[i][pn[i]+1].y - p[i][pn[i]].y) * 
				(ev - p[i][pn[i]].x) / (p[i][pn[i]+1].x - p[i][pn[i]].x);
		double nvl = nl[1] - nl[0];
		ans += 0.5 * (ev - lc) * (vl + nvl);
		vl = nvl;
		lc = ev;  pn[x] ++;
	}
	return ans;
}

int work()
{
	int W, G;
	scanf("%d%d%d%d", &W, &N[0], &N[1], &G);
	for (int i = 0; i < N[0]; i ++)
		scanf("%lf%lf", &p[0][i].x, &p[0][i].y);
	for (int i = 0; i < N[1]; i ++)
		scanf("%lf%lf", &p[1][i].x, &p[1][i].y);

	double dTotArea = CalcArea(W);
	double dEArea = dTotArea / G;


	for (int i = 1; i < G; i ++)
	{
		double dAA = dEArea * i;
		double ll = 0.0, rr = W, mid;
		while (ll + 1e-7 < rr)
		{
			mid = (ll + rr) * 0.5;
			double dv = CalcArea(mid);
			if (dv < dAA)  ll = mid;
			else rr = mid;
		}
		mid = (ll + rr) * 0.5;
		printf("%.8f\n", mid);
	}

	return 0;
}

int main()
{
	freopen("a2.txt", "r", stdin);
	freopen("a2.ans", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k ++)
	{
		printf("Case #%d:\n", k);
		work();
	}
	return 0;
}