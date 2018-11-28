#include<stdio.h>
#include<math.h>
#define maxn 3
double x[maxn],y[maxn],r[maxn];
int n;

#define two(a) ((a)*(a))
#define fmax(a,b) a<b?b:a
//#define fmin(a,b) a<b?a:b

double findans(int n1,int n2)
{
	double d=sqrt(two(x[n1]-x[n2])+two(y[n1]-y[n2]))+r[n1]+r[n2];
	return d/2;
}

double solve()
{
	scanf("%d",&n);
	for(int i=0;i<n;++i)
		scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
	if(n==1) return r[0];
	if(n==2) return fmax(r[0],r[1]);
	if(n==3)
	{
		double re=1e20;
		double p,t;
		p=findans(0,1);
		t=fmax(p,r[2]);
		if(t<re) re=t;

		p=findans(0,2);
		t=fmax(r[1],p);
		if(t<re) re=t;

		p=findans(1,2);
		t=fmax(p,r[0]);
		if(t<re) re=t;

		return re;
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
		printf("Case #%d: %lf\n",i+1,solve());
	return 0;
}

