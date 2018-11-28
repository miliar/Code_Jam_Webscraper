#include<stdio.h>
#include<math.h>

#include<algorithm>

using namespace std;

int n;
double a[11], b[11], c[11];

double Go(int x, int y, int z)
{
	double dist;

	double ret = c[x];
	dist = sqrt( (a[y]-a[z])*(a[y]-a[z]) + (b[y]-b[z])*(b[y]-b[z]));
	return max(ret, (dist+c[y]+c[z])/2.0);
}

int main(void)
{
	int T;
	int l1, l0;

	double ret;

	freopen("d1.in","r",stdin);
	freopen("d1.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		for(l1=0;l1<n;l1++)
		{
			scanf("%lf %lf %lf\n",&a[l1],&b[l1],&c[l1]);
		}

		if(n == 1)
		{
			ret = c[0];
		}
		else if(n == 2)
		{
			ret = max(c[0], c[1]);
		}
		else if(n == 3)
		{
			ret = Go(0, 1, 2);
			ret = min(ret, Go(1, 0, 2));
			ret = min(ret, Go(2, 0, 1));
		}
		printf("Case #%d: %lf\n",l0, ret);
	}
	return 0;
}