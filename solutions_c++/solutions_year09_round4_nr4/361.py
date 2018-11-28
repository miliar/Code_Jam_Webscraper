#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;
#define N 10
int r[N], x[N], y[N], u[N];
double mx(double x, double y) { return x>y?x:y; }
int main()
{
	int i, n, t, ts;
	double R, z;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), i=0; i<n; scanf("%d%d%d", &x[i], &y[i], &r[i]), u[i]=i, i++);
		if(n==1) printf("Case #%d: %.9lf\n", t+1, (double)r[0]);
		else if(n==2) printf("Case #%d: %.9lf\n", t+1, mx(r[0], r[1]));
		else
		{
			for(R=1E20; ; )
			{
				z=mx((sqrt((double)(x[u[0]]-x[u[1]])*(x[u[0]]-x[u[1]])+(double)(y[u[0]]-y[u[1]])*(y[u[0]]-y[u[1]]))+r[u[0]]+r[u[1]])*0.5, r[u[2]]);
				if(z<R) R=z;
				if(!next_permutation(u, u+n)) break;
			}
			printf("Case #%d: %.9lf\n", t+1, R);
		}
	}
	return 0;
}