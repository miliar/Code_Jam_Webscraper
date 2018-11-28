#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int nt;

int L, U, W, G;

struct Point
{
	int x, y;
	
	void read()
	{
		scanf("%d %d", &x, &y);
	}
};

Point low[100], up[100];

double calc(double x)
{
	double res = 0.0;
	for(int i = 1; i < U; i++)
	if (up[i - 1].x <= x && x <= up[i].x)
	{
		double y = up[i - 1].y + (double)(up[i].y - up[i - 1].y) * (x - up[i - 1].x) / (up[i].x - up[i - 1].x);
		res += (x - up[i - 1].x) / 2.0 * (y + up[i - 1].y);
		break;
	}
	else
	{
		res += (up[i].x - up[i - 1].x) / 2.0 * (up[i].y + up[i - 1].y);
	}
	
	for(int i = 1; i < L; i++)
	if (low[i - 1].x <= x && x <= low[i].x)
	{
		double y = low[i - 1].y + (double)(low[i].y - low[i - 1].y) * (x - low[i - 1].x) / (low[i].x - low[i - 1].x);
		res -= (x - low[i - 1].x) / 2.0 * (y + low[i - 1].y);
		break;
	}
	else
	{
		res -= (low[i].x - low[i - 1].x) / 2.0 * (low[i].y + low[i - 1].y);
	}
	
	return res;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d:\n", tt);
		
		scanf("%d %d %d %d", &W, &L, &U, &G);
		
		for(int i = 0; i < L; i++) low[i].read();
		for(int i = 0; i < U; i++) up[i].read();
		
		double total = calc(W);
		
		for(int i = 1; i < G; i++)
		{
			double S = total * i / G;
			
			double left = 0, right = W;
			for(int iter = 0; iter < 100; iter++)
			{
				double x = (left + right) / 2;
				if (calc(x) < S) left = x; else right = x;
			}
			
			printf("%.10lf\n", left);
		}
		
	}
	return 0;
}