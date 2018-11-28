#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

const char input[] = "input.in";
const char output[] = "output.out";

struct flo
{
	int x, y, r;
};

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	
	int t;
	scanf("%d", &t);
	int test;
	for(test = 1; test <= t; ++test)
	{
		int n;
		scanf("%d", &n);
		double rmin;
		if(n == 1)
		{
			int x, y, r;
			scanf("%d %d %d", &x, &y, &r);
			rmin = r;
		}
		else if(n == 2)
		{
			int x1, y1, r1;
			int x2, y2, r2;
			scanf("%d %d %d", &x1, &y1, &r1);
			scanf("%d %d %d", &x2, &y2, &r2);
			rmin = r1;
			if(r2 > rmin) rmin = r2;
		}
		else if(n == 3)
		{
			flo v[6];
			int i;
			for(i = 0; i < n; ++i)
				scanf("%d %d %d", &v[i].x, &v[i].y, &v[i].r);
			v[3] = v[0];
			v[4] = v[1];
			
			rmin = 10000;
			for(i = 0; i < n; ++i)
			{
				double r = v[i+2].r;
				double d = sqrt((v[i].x-v[i+1].x)*(v[i].x-v[i+1].x) + (v[i].y-v[i+1].y)*(v[i].y-v[i+1].y));
				//if(r < d+r1+r2)
				double raza = (d + v[i].r + v[i+1].r) / 2;
				if(raza - r > 0) r = raza;
				if(r < rmin) rmin = r;
			}
		}
		printf("Case #%d: %.8f\n", test, rmin);
	}
	return 0;
}
