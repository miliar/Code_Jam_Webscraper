#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

#define eps 1e-9
#define LOW 0.0

struct point
{
	double x, y;
};

double get_s(double X, vector<point> &p)
{
	int n = p.size();
	double sum = 0.0;
	for(int i=0; i<n-1; ++i)
	{
		if (p[i].x + eps    > X) break;
		if (p[i+1].x  - eps < X)
			sum += (p[i+1].x - p[i].x)*(p[i].y - LOW + p[i+1].y - LOW);
		else
		{
			double Y = (p[i+1].y - p[i].y)*(X - p[i].x)/(p[i+1].x - p[i].x) + p[i].y;
			sum += (X - p[i].x)*(p[i].y - LOW + Y - LOW);
		}
	}
	return sum;
}

int w, g, up_count, down_count;
vector<point> up, down;

int main()
{
    int tc;
	//freopen("B.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
		scanf("%i %i %i %i", &w, &down_count, &up_count, &g);
		down.resize(down_count);
		up.resize(up_count);
		for(int i=0; i<down_count; ++i) scanf("%lf %lf", &down[i].x, &down[i].y);
        for(int i=0; i<up_count; ++i) scanf("%lf %lf", &up[i].x, &up[i].y);
		double sum = get_s(w, up) - get_s(w, down);
        printf("Case #%i:\n", tt);
		for(int i=1; i<g; ++i)
		{
			double sneed = sum / g  * i;
			double A = 0;
			double B = w;
			double C;
			while (B - A > eps)
			{
				C = (A+B)*0.5;
				double tmp = get_s(C, up) - get_s(C, down);
				if (tmp > sneed) B = C; else A = C;
			}
			printf("%.9f\n", (A+B)*0.5);
		}
    }
}