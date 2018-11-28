#include<stdio.h>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
struct point
{
	int x;
	int y;
}pt[5];
double area(int n,point p[])
{
	int i;
     double sum=0, x=p[0].x,y=p[0].y;
	for(i=2;i<n;i++)
	{
       sum+=(p[i-1].x-x)*(p[i].y-y)-(p[i-1].y-y)*(p[i].x-x);
	}
	return sum/2;
}
int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int c,n,m,t,i,j,k,l,a;
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",c);
		for(i=0;i<=n;i++)
			for(j=0;j<=m;j++)
			{
				for(k=0;k<=n;k++)
					for(l=0;l<=m;l++)
					{
						pt[0].x=0,pt[0].y=0;
						pt[1].x=i,pt[1].y=j;
						pt[2].x=k,pt[2].y=l;
						if(fabs((area(3,pt)-a*1.0/2))<10e-8)
						{
							printf("0 0 %d %d %d %d\n",i,j,k,l);
							goto A;
						}
					}
			}
			printf("IMPOSSIBLE\n");
A:;	}
	return 0;
}