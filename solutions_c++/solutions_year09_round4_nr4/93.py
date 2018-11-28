#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define sqr(x) ((x)*(x))
int n,x[50],y[50],r[50];
double ret;

inline double Dist(double x1,double y1,double x2,double y2)
{	return sqrt(sqr(x1-x2)+sqr(y1-y2));	}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int Test,Case=0;
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		if (n<3) ret=max(r[0],r[1]);
		else {
			ret=1e99;
			ret<?=max((double)r[0],(r[1]+r[2]+Dist(x[1],y[1],x[2],y[2]))/2);
			ret<?=max((double)r[1],(r[0]+r[2]+Dist(x[0],y[0],x[2],y[2]))/2);
			ret<?=max((double)r[2],(r[0]+r[1]+Dist(x[0],y[0],x[1],y[1]))/2);
		}
		printf("Case #%d: %.10lf\n",++Case,ret);
	}
	return 0;
}
