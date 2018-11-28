// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

struct point
{
	long long x, y;
};

long long min(long long a, long long b)
{
	if(b<a)
		return b;
	else
		return a;
}

long long abs(long long a)
{
	if (a<0)
		a=-a;
	return a;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int N;
	scanf("%i\n",&N);

	for(int z=0; z<N; z++)
	{
		long long n, A, B, C, D, x0, y0, M;
		scanf("%lli %lli %lli %lli %lli %lli %lli %lli\n", &n, &A, &B, &C, &D, &x0, &y0, &M);
		point *points = new point [n];
		points[0].x = x0;
		points[0].y = y0;
		points[1].x = (A*points[0].x+B) % M;
		points[1].y = (C*points[0].y+D) % M;
		long long minx = min(points[0].x, points[1].x);
		long long miny = min(points[0].y, points[0].y);
		long long dx = abs(points[1].x-points[0].x);
		long long dy = abs(points[1].y-points[0].y);
		for (long long i=2; i<n; i++)
		{
			points[i].x = (A*points[i-1].x+B) % M;
			points[i].y = (C*points[i-1].y+D) % M;
			for (long long j=0; j<i; j++)
			{
				if(abs(points[i].x-points[j].x)>0)
					dx = min(dx, abs(points[i].x-points[j].x));
				if(abs(points[i].y-points[j].y)>0)
					dy = min(dy, abs(points[i].y-points[j].y));
			}
			minx = min(minx, points[i].x);
			miny = min(miny, points[i].y);
		}
		//printf("%lli %lli %lli %lli\n",minx, miny, dx, dy);
		long long result=0;
		for (long long i=0; i<n-2; i++)
			for (long long j=i+1; j<n-1; j++)
				for (long long k=j+1; k<n; k++)
				{
					if (((points[i].x+points[j].x+points[k].x)%3+(points[i].y+points[j].y+points[k].y)%3)==0)
					{
						/*long long cx = (points[i].x+points[j].x+points[k].x)/3;
						long long cy = (points[i].y+points[j].y+points[k].y)/3;
						int f1, f2;
						f1=f2=0;
						for (long long g=minx; g > cx; g=g+dx)
							if (g==cx)
								f1=1;
						for (long long g=miny; g > cy; g=g+dy)
							if (g==cy)
								f2=1;
						int f=f1&&f2;
						if (f)*/
							result++;
					}
				}
		printf("Case #%i: %lli\n",z+1,result);
	}
	return 0;
}

