#include <cstdio>
#include <cstdlib>
#include <cmath>
const double PI = 2*asin(1);
double x[1005],y[1005],r[1005],w,h;
double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));	
}
bool add_circle(int i)
{
	int cnt,j;
	/*for(cnt=1;cnt<=10000;cnt++)
	{
		int rd = rand()%10000001; 
		double tmp = (double)rd/10000000;
		x[i] = w*tmp;
		rd = rand()%10000001;
		tmp = (double)rd/10000000;
		y[i] = h*tmp;
		for(j=1;j<i;j++)
			if(dist(x[i],y[i],x[j],y[j]) < r[i]+r[j])
				break;
		if(i == j)
			return true;	
	}*/
	if(i == 1)
	{
		x[1] = y[1] = 0;
		return true;	
	}
	int trial = 10000;
	while(trial--)
	{
		//int v = rand()%(i-1)+1;
		int rd = rand()%101;
		double tmp = (double)rd/101;
		double th = 2*PI*tmp;
		//x[i] = x[v] + (r[i]+r[v])*sin(th);
		//y[i] = y[v] + (r[i]+r[v])*cos(th);
		x[i] = w*tmp;
		rd = rand()%101;
		tmp = (double)rd/101;
		y[i] = h*tmp;
		if(x[i] > w || y[i] > h)
			continue;
		for(j=1;j<i;j++)
			if(dist(x[i],y[i],x[j],y[j]) < r[i]+r[j])
				break;
		if(i == j)
			return true;
	}	
	return false;
}
int comp(const void *p,const void *q)
{
	return *(double*)q > *(double*)p ? 1 : -1; 	
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	srand(42);
	int cn,t,n,i;
	double tmp;
	scanf("%d",&t);
	for(cn=1;cn<=t;cn++)
	{
		scanf("%d",&n);
		scanf("%lf%lf",&w,&h);
		for(i=1;i<=n;i++)
			scanf("%lf",&r[i]);
		//qsort(r+1,n,sizeof(double),comp);
		while(true)
		{
			for(i=1;i<=n;i++)
				if(!add_circle(i))	
					break;
			if(i == n+1)
				{
					printf("Case #%d: ",cn);
					for(i=1;i<=n;i++)
						printf("%.1f %.1f ",x[i],y[i]);
					printf("\n");
					break;	
				}
		}	
	}	
}
