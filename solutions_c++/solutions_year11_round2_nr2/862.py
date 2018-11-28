#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;
double v[300];
double p[300];

bool check(long double l, long double h)
{
	if (l-h > -1e-9 && l-h < 1e-9)
		return true;
	return false;
}

double fix(double d)
{
	if (d > -1e-9 && d < 1e-9)
		return 0;
	return d;
}

bool allgood(int c, int d)
{
	for (int i = 0; i < c; ++i)
	{
		if (v[i] > 1)
			return false;
	}
	for (int i = c-2; i >= 0; --i)
	{
		if (p[i+1] - p[i] < d)
			return false;
	}
	return true;
}

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d: ", q);
		
		int c, d;
		
		scanf("%d%d", &c, &d);
		for (int i = 0; i < c; ++i)
			scanf("%lf%lf", &p[i], &v[i]);
			
			
		if (allgood(c, d))
		{
			printf("0.0\n");
			continue;
		}
		
		int maximo = 0;
		long double l = d/2.0, h = 2000000000;
		long double t;
		for (int i = 0; i < 100; ++i)
		{
			if (check(l, h) || l > h)
				break;
			t = (h-l)/2.0 + l;
			long double ma = p[c-1] + t;
			ma = ma - d*(v[c-1]-1);
			bool high = false;
			
			if (p[c-1]-ma > t)
			{
				high = true;
			}
			else
			{
				for (int j = c-2; j >=0; --j)
				{
					if (p[j] + t < ma - d)
					{
						ma = p[j] + t;
						ma = ma - d*(v[j]-1);
					}
					else
						ma = ma - d*v[j];
					if (p[j]-ma > t)
					{
						high = true;
						break;
					}
				}
			}
			if (high)
				l = t;
			else	
				h = t;
		}
		printf("%lf\n", fix((double)(t)));
	}
	
	return 0;
}

