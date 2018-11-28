#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const int MAXN=1009;
const double ZERO=1e-7;
int T;
int n;
double w,l;
struct circle
{
	double r,x,y;
	int num;
} c[MAXN];
int ans[MAXN];

bool cmp(const struct circle &a,const struct circle &b)
{
	return a.r>b.r;
}

void init()
{
	scanf("%d %lf %lf",&n,&w,&l);
	for (int i=1;i<=n;i++)
	{
		scanf("%lf",&c[i].r);
		c[i].num=i;
	}
}

bool ok(double xx,double yy,int m)
{
	if (xx>w+ZERO || yy>l+ZERO) return false;
	for (int i=1;i<m;i++)
		if ((xx-c[i].x)*(xx-c[i].x)+(yy-c[i].y)*(yy-c[i].y)<(c[i].r+c[m].r)*(c[i].r+c[m].r)-ZERO) return false;
	c[m].x=xx;	c[m].y=yy;
	return true;
}

void work()
{
	sort(c+1,c+n+1,cmp);
	for (int i=1;i<=n;i++)	ans[c[i].num]=i;

	c[1].x=c[1].y=0;

	for (int i=2;i<=n;i++)
	{
		bool done=false;
		for (int j=1;j<i;j++)
		{
			double xx,yy;
			xx=c[j].x+c[j].r+c[i].r;	yy=c[j].y;
			if (ok(xx,yy,i))
			{	
				done=true;	break;
			}
			xx=c[j].x;	yy=c[j].y+c[j].r+c[i].r;
			if (ok(xx,yy,i))
			{	
				done=true;	break;
			}
		}
		if (!done) cerr<<"ERROR !"<<i<<endl;
	}
	for (int i=1;i<=n;i++)	printf(" %.3f %.3f",c[ans[i]].x,c[ans[i]].y);
	printf("\n");
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		printf("Case #%d:",t);
		work();
	}
	return 0;
}
