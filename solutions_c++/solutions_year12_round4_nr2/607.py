#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct point 
{
	double x, y;
};
struct opa
{
	double x1, x2, y1, y2;
	opa(){};
	opa( double _x1, double _x2, double _y1, double _y2)
	{
		x1 = _x1;
		x2 = _x2;
		y1 = _y1;
		y2 = _y2;
	}
};
point p[1024]; int br;
double r[1024], L, W;
int id[1024];
opa c[1024];


bool cmp (int p1, int p2)
{
	return r[p1] > r[p2];
}

int checkIn (double R, opa e)
{
	if(e.x1 == 0 && R > e.x2 && e.x2 != W)
		return 0;
	
	if(e.y1 == 0 && R > e.y2 && e.y2 != L)
		return 0;
	
	if(e.x2 == W && R > e.x2 - e.x1 && e.x1 != 0)
		return 0;
	
	if(e.y2 == L && R > e.y2 - e.y1 && e.y1 != 0)
		return 0;
	
	if (e.x1 != 0 && e.x2 != W && e.x2 - e.x1 < 2*R)
		return 0;
	
	if (e.y1 != 0 && e.y2 != L && e.y2 - e.y1 < 2*R)
		return 0;
	
	return 1;
}
void solve ()
{
	int n;
	scanf ("%d%lf%lf", &n, &W, &L);
	int i; 
	for (i = 0; i < n; i ++)
	{
		id[i] = i;
		scanf ("%lf", &r[i]);
	}
	sort (id, id + n, cmp);
	br = 0; 
	c[br ++] = opa(0, W, 0, L);
	int j;
	for (i = 0; i < n; i ++)
	{
		double R = r[id[i]];
				
		for (j = 0; j < br; j ++)
		{
			if ( checkIn (R, c[j]) )
			{
				double dx = c[j].x1 ==0? 0 : R;
				double dy = c[j].y1 ==0? 0 : R;
				
				p[id[i]].x = c[j].x1 + dx;
				p[id[i]].y = c[j].y1 + dy;
				//cout << p[id[i]].x << endl;
				if (dx == 0) dx = R;
				else dx = 2*R;
				if (dy == 0) dy = R;
				else dy = 2*R;
				
				c[br ++] = c[j];
				c[br - 1].x1 += dx;
				
				c[j].y1 = min(c[j].y1 + dy, L);
				c[j].x2 = min (c[j].x1 + dx, W);
				
				break;
			}
		}
		
		if (j == br)
			exit(1);
	}
	
	for (i = 0; i < n; i ++)
	{
		printf (" %lf %lf",p[i].x, p[i].y);
	}
	
	printf ("\n");
}
int main ()
{
	
	int t; 
	scanf ("%d", &t);
	int i; 
	for (i =1; i <=t; i++)
	{
		printf("Case #%d:", i);
		solve();
	}	
	
	return 0;
}