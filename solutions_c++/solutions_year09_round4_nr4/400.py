#include <cstdio>
#include <cmath>
#include <cstring>

#define sqr(x) ((x)*(x))

int T,N;
struct sc
{
	int x,y,r;
}c[3];

void init()
{
	int i;
	
	scanf("%d",&N);

	for (i=0;i<N;i++)
	{
		scanf("%d%d%d",&c[i].x,&c[i].y,&c[i].r);
	}
	
}


double g(int o,int p,int q)
{
	double r1,r2,d;
	
	r2=c[q].r;
	
	d=sqrt(sqr(c[o].x-c[p].x)+sqr(c[o].y-c[p].y));
	if (d<c[o].r)
		r1=c[o].r;
	else if (d<c[p].r)
		r1=c[p].r;
	else
		r1=0.5*(d+c[o].r+c[p].r);
	return r1>r2?r1:r2;
}

double work()
{
	
	double re,t;
	
	if (N==1)
		return c[0].r;
	if (N==2)
		return c[1].r>c[0].r?c[1].r:c[0].r;
	
	re=g(0,1,2);
	t=g(0,2,1);
	re=re<t?re:t;
	t=g(1,2,0);
	re=re<t?re:t;
	
	return re;
}

int main()
{
	int i;
	
	freopen("d-small-attempt0.in","r",stdin);
	freopen("d-small.out","w",stdout);
	scanf("%d",&T);
	for (i=1;i<=T;i++)
	{
		init();
		printf("Case #%d: %.6lf\n",i,work());
	}
	
	return 0;
}
