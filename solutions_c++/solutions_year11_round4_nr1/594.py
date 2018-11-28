#include <iostream>

using namespace std;

struct road
{
	double l,r,w;
	bool operator <(const road &A) const
	{
		return w<A.w;
	}
};

road e[20000];
double x,s,r,t,n;

void init()
{
	double ans=0;
	scanf("%lf%lf%lf%lf%lf",&x,&s,&r,&t,&n);
	double left = x;
	for (int i=0;i<n;i++)
	{
		scanf("%lf%lf%lf",&e[i].l,&e[i].r,&e[i].w);
		left-= e[i].r-e[i].l;
	}
	for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++)
			if (e[j]<e[i]) swap(e[i],e[j]);
	if (left<=t*r)
	{
		ans+=left/r;
		t-=ans;
	}
	else
	{
		ans+=t+(left-r*t)/s;
		t=0;
	}
	for (int i=0;i<n;i++)
	{
			if ((e[i].r-e[i].l)<=t*(r+e[i].w))
			{
				ans+=(e[i].r-e[i].l)/(r+e[i].w);
				t-=(e[i].r-e[i].l)/(r+e[i].w);
			}
			else
			{
				ans+=t+((e[i].r-e[i].l)-(r+e[i].w)*t)/(s+e[i].w);
				t=0;
			}
	}
	printf("%.9lf\n", ans);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		init();
	}
}
