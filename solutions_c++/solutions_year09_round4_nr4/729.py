#include<stdio.h>
#include<math.h>
struct node
{
	int x;
	int y;
	int r;
}a[50];
int ti,tn,i,n;
double s;
double maxn(double x,double y)
{
	return x>y?x:y;
}
double minn(double x,double y)
{
	return x<y?x:y;
}
double calc(int x,int y)
{
	return (double(a[x].r+a[y].r)+sqrt(double((a[x].x-a[y].x)*(a[x].x-a[y].x)+(a[x].y-a[y].y)*(a[x].y-a[y].y))))/2.0;
}
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&tn);
	for (ti=1;ti<=tn;ti++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%d%d%d",&a[i].x,&a[i].y,&a[i].r);
		if (n==1) printf("Case #%d: %d\n",ti,a[0].r);
		else
			if (n==2)
			{
				if (a[0].r>=a[1].r) printf("Case #%d: %d\n",ti,a[0].r);
				else printf("Case #%d: %d\n",ti,a[1].r);
			}
			else
			{
				s=maxn(calc(0,1),double(a[2].r));
				s=minn(maxn(calc(0,2),double(a[1].r)),s);
				s=minn(maxn(calc(1,2),double(a[0].r)),s);
				printf("Case #%d: %lf\n",ti,s);
			}
	}
	return 0;
}
