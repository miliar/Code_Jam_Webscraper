#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);

	//freopen("input.txt", "r", stdin);

	int i, j, cas, now, n, x[3], y[3], r[3], mr;
	double sol, dist;
	scanf("%d\n",&cas);

	for(now = 1; now <= cas; now++) {
		printf("Case #%d: ",now);
		scanf("%d\n",&n);
		
		for(i=0; i<n; i++) {
			scanf("%d %d %d",&x[i],&y[i],&r[i]);
			if(i==0) mr = r[i];
			else {
				if(mr < r[i]) mr = r[i];
			}
		}

		if(n <= 2) {
			sol = (double)mr;	
		}
		else {
			dist = sqrt((double)((x[0] - x[1])*(x[0] - x[1]) + (y[0] - y[1])*(y[0] - y[1]))) + (double)r[0] + (double)r[1];
			dist /= 2.0;
			sol = dist;
			if(sol < (double)r[2]) sol = (double)r[2];

			dist = sqrt((double)((x[1] - x[2])*(x[1] - x[2]) + (y[1] - y[2])*(y[1] - y[2]))) + (double)r[1] + (double)r[2];
			dist /= 2.0;
			if(sol > dist) sol = dist;
			if(sol < (double)r[0]) sol = (double)r[0];


			dist = sqrt((double)((x[0] - x[2])*(x[0] - x[2]) + (y[0] - y[2])*(y[0] - y[2]))) + (double)r[0] + (double)r[2];
			dist /= 2.0;
			if(sol > dist) sol = dist;
			if(sol < (double)r[1]) sol = (double)r[1];
		}

		printf("%.6f\n",sol);
	}

	return 0;
}