#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

typedef struct P
{
	int p, v;

	bool operator<(const P& pp) const
	{
		return p < pp.p;
	}
} P;

int c, d, n;
P ps[200];

int valid(long double t)
{
	//printf("---%Lf\n", t);
	long double last = -100000000000;
	for(int i = 0; i < c; i++)
	{
		long double maxleft = max(ps[i].p - t, last + d);
		long double right = maxleft + (ps[i].v - 1) * d;
		if(right > ps[i].p && right - ps[i].p > t)
			return 0;
		last = right;
	}
	return 1;
}

long double binsearch()
{
	long double a = 0.;
	long double b = d*n;
	while(b-a > 0.0000000000001)
	{
		long double mid = (a+b)/2;
		if(valid(mid))
			b = mid;
		else a = mid;
	}
	return (a+b)/2;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		scanf("%d%d", &c, &d);
		n = 0;
		for(int j = 0; j < c; j++)
		{
			scanf("%d%d", &ps[j].p, &ps[j].v);
			n += ps[j].v;
		}
	
		printf("Case #%d: %.12Lf\n", i, binsearch());
	}
	return 0;
}
