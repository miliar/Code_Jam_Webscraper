#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#define MAXN 1020
using namespace std;

struct pt
{
	int speed;
	double len;
	bool operator < (const pt &p) const
	{return speed < p.speed;}
};

int n, w, r, t, l;
pt ori[MAXN];

void Solve()
{
	int i, a, b, c, total;
	double leftTime, sum, tl, len;
	scanf("%d%d%d%d%d", &l, &w, &r, &t, &n);
	for (i = 0, total = l; i < n; i++)
	{
		scanf("%d%d%d", &a, &b, &c);
		ori[i] = (pt){c, b - a};
		total -= (b - a);
	}
	ori[i] = (pt){0, total};
	sort (ori, ori + n + 1);
	
	for (i = 0, leftTime = t, sum = 0; i < n + 1; i++)
	{
		a = ori[i].speed + w;
		b = ori[i].speed + r;
		len = ori[i].len;
		if (leftTime == 0)
			sum += len / a;
		else if (leftTime < len / b)
		{
			sum += leftTime;
			tl = len - b * leftTime;
			sum += tl / a;
			leftTime = 0;
		}
		else
		{
			sum += len / b;
			leftTime -= len / b;
		}
	}
	printf("%.10f\n", sum);
}

int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int t, f;
	cin >> t;
	for (f = 1; f <= t; f++)
	{
		printf("Case #%d: ", f);
		Solve();
	}
	return 0;
}
