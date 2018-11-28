#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <iomanip>
using namespace std;

main ()
{
	int t,n;
	double T;
	scanf("%d",&t);

	for (int k = 1; k <= t; k++)
	{
		cout << "Case #" << k << ": ";
		scanf("%d%lf",&n,&T);

		double x[1000001];

		int sz = 0;
		for (int i = 0; i < n; i++) 
		{
			int p,v;
			scanf("%d%d",&p,&v);

			for (int j = 0; j < v; j++) x[sz++] = p;
		}

		sort(x,x+sz);

		double low = 0, high = 10000000000000000ll,mid;
		for (int step = 0; step < 100; step++)
		{
			mid = (low+high)/2;
			double x1 = x[0]-mid;
			int i;
			bool poss = true;
			for (i = 1; i < sz; i++)
			{
				double x2;
				if (x[i]+mid-x1 > T || fabs(x[i]+mid-x1-T) <= 1e-9)
				{
					if (x1+T < x[i])
					{
						x2 = max(x1+T,x[i]-mid);
					}
					else 
					{
						x2 = min(x[i]+mid,x1+T);
					}
					x1 = x2;
				}
				else { poss = false; break; }
			}
			if (poss)
			{
				high = mid;
			}
			else
			{
				low = mid;
			}
		}
		cout << fixed;
		cout << setprecision(4) << mid << "\n";
	}
}

