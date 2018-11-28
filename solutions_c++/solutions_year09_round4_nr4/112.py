#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define oo 50
struct Tpnt
{
	double x,y,r;
}	a[oo];
int N,Test,Case;

inline double sqr(const double& x)
{
	return x*x;
}
inline double dist(const Tpnt& A,const Tpnt& B)
{
	return sqrt(sqr(A.x-B.x)+sqr(A.y-B.y));
}

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%lf%lf%lf",&a[i].x,&a[i].y,&a[i].r);
}

inline void Solve()
{
	if (N==1) printf("%.10lf\n",a[1].r);
	else if (N==2) printf("%.10lf\n",max(a[1].r,a[2].r));
	else if (N==3)
	{
		double ans=1e100;
		for (int i=1;i<=3;++i)
			for (int j=i+1;j<=3;++j)
				ans=min(ans,max(a[6-i-j].r,(dist(a[i],a[j])+a[i].r+a[j].r))/2);
		printf("%.10lf\n",ans);
	}
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
