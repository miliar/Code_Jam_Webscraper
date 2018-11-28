#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

struct Pt
{
	double x, y, r;
};
double sqr(double x)
{
	return x*x;
}
double dist(Pt &a, Pt &b)
{
	return sqrt( sqr(a.x-b.x)+sqr(a.y-b.y ) )+a.r+b.r;
}


vector<Pt> pt;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, n;

	cin >> nt;
	for(int it=0; it<nt; it++)
	{
		cin >> n;
		pt.resize(n);
		for(int i=0; i<n; i++)
		{
			cin >> pt[i].x >> pt[i].y >> pt[i].r;
		}

		if( n==1 )
		{
			printf( "Case #%d: %.6lf\n", (it+1), pt[0].r);
			continue;
		}
		else if( n==2 )
		{
			printf( "Case #%d: %.6lf\n", (it+1), max(pt[0].r, pt[1].r));
			continue;
		}
		
		double rmax = 1.e20;	

		for(int i=0; i<n; i++)
		{
			for(int j=i+1; j<n; j++)
			{
				double cur = dist( pt[i], pt[j] ) * 0.5;
				if( cur < rmax )
					rmax = cur;
			}
		}

		for(int i=0; i<n; i++)
		{
			if( pt[i].r > rmax )
				rmax = pt[i].r;
		}

		printf( "Case #%d: %.6lf\n", (it+1), rmax);
	}
	return 0;
}