#include<iostream>
#include<cmath>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
using namespace std;

const long maxn=5;

double p[maxn][3];
long n,t;

void init()
{
	scanf("%d",&n);
	fo(i,1,n)
		fo(j,0,2) scanf("%lf",&p[i][j]);
}
double dist(long i, long j)
{
	return sqrt((p[i][0]-p[j][0])*(p[i][0]-p[j][0])+(p[i][1]-p[j][1])*(p[i][1]-p[j][1]));
}
double max(double x, double y)
{
	return x>y?x:y;
}
double min(double x, double y)
{
	return x<y?x:y;
}
void solve()
{
	if (n==1) printf("%.6lf\n",p[1][2]);
	else if (n==2) printf("%.6lf\n",max(p[1][2],p[2][2]));
	else {
		double ans=1e100,now;
		now=max((dist(1,2)+p[1][2]+p[2][2])/2.0, p[3][2]);
		ans=min(ans,now);
		now=max((dist(1,3)+p[1][2]+p[3][2])/2.0, p[2][2]);
		ans=min(ans,now);
		now=max((dist(2,3)+p[2][2]+p[3][2])/2.0, p[1][2]);
		ans=min(ans,now);
		printf("%.6lf\n",ans);
	}
}
int main()
{
	freopen("DS.in","r",stdin);
	freopen("DS.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		init();
		printf("Case #%d: ",l);
		solve();
	}
	return 0;
}
