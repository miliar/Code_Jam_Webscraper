#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#define MAX_LONG_LONG 9223372036854775807
#define MAX_INT  2147483647
#define MAX_LONG 2147483647
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
int x[10000];
int y[10000];
int z[10000];
int vx[10000];
int vy[10000];
int vz[10000];



int main() {
	freopen("..//input.txt", "rt", stdin);
	freopen("..//output.txt", "wt", stdout);
	int tc; 
	scanf("%d", &tc);
	int N;
	double dmin, tmin;
	long long cx1,cy1, cz1,  cx2, cy2, cz2;
	long long tmpcx1,tmpcy1, tmpcz1,  tmpcx2, tmpcy2, tmpcz2;

	for(int t = 1; t <= tc; t ++)
	{
		scanf("%d", &N);
		cx1 = 0; cy1=0;cz1=0;
		cx2 = 0;cy2=0;cz2=0;
		for(int i = 0; i < N; i ++)
		{
			scanf("%d %d %d %d %d %d", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);

			cx1 = cx1 + x[i];cy1 = cy1 + y[i]; cz1 = cz1+z[i];
			cx2 = cx2 + vx[i]; cy2=cy2+vy[i]; cz2=cz2+vz[i];
		}
		tmpcx1 = cx1;tmpcy1 = cy1;tmpcz1 = cz1;
		tmpcx2 = cx2;tmpcy2 = cy2;tmpcz2 = cz2;

		cx1 = cx1 * cx2;cy1 = cy1*cy2;cz1 = cz1 * cz2;
		cx2 = cx2 * cx2; cy2 = cy2 * cy2; cz2 = cz2 * cz2;
		if(cx1 + cy1 + cz1 > 0)
			tmin = 0;
		else
		{
			double dd= (cx2 + cy2 + cz2);
			if( dd != 0)
				tmin =  -(cx1 + cy1 + cz1)/dd;
			else tmin = 0;

		}			
		if(tmin < 0) tmin = 0;
		
		double xc, yc, zc;
			xc = tmpcx1 + tmin * tmpcx2;
			yc = tmpcy1 + tmin * tmpcy2;
			zc = tmpcz1 + tmin * tmpcz2;

			xc = xc * xc;
			yc = yc *  yc; 
			zc = zc * zc;

		double dmin = sqrt(double(xc + yc + zc)/(N*N));
		printf("Case #%d: %f %f\n", t,  dmin,tmin);
	}
}
