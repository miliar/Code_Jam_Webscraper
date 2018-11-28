#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
const int lim = 255;
using namespace std;

int p[1000000 + 5];
double d;
int c, n;
double l, r, m;

void init()
{
	scanf("%d%lf", &c, &d);
	int q, v;
	n = 0;
	for (int i = 0; i < c; i++)
	{
		scanf("%d%d", &q, &v);
		for (int j = 0; j < v; j++)
			p[n++] = q;
	}
}
int check(double mid)
{
    double pos;
    pos = p[0] - mid;
    for(int i = 1; i < n; i++)
    {
        if(p[i] + mid < pos + d)
            return 0;
        pos = max(p[i] - mid, pos + d);
    }
    return 1;
}

void process()
{
	l = 0.0;
	r = 1e12;
	for(int k = 0; (k < lim) && (l < r - 1e-8); k++)
	{
		m = (l + r) * 0.5;
		if(check(m) == 1)
			r = m;
		else
			l = m;
	}
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
		init();
		process();
        printf("Case #%d: %.6f\n", t, r);
    }
    return 0;
}
