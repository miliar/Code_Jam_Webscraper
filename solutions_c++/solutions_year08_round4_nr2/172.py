#include <iostream>
using namespace std;
int n,m,v;

/*
struct gao
{
	int x,y;
	bool f;
}a[2501];
*/
/*
double compute(poi a,poi b,poi c)
{return (b.x*c.y);}
//计算三角形面积
double compute(poi a,poi b,poi c)
{return (b.x*c.y+c.x*a.y)-(a.y*b.x);}
double compute(poi a,poi b,poi c)
{return (a.x*b.y+b.x*c.y+c.x*a.y)-(a.y*b.x+b.y*c.x+c.y*a.x);}
*/

int main()
{
	freopen("bin5.txt","r",stdin);
	freopen("bout51.txt","w",stdout);
	int n,i,j,k,ii,p,x,y;
	scanf("%d",&n);
	int l,m,s;
	int a,b,c,d;
	for(ii=1;ii<=n;ii++)
	{
		bool f=true;
		printf("Case #%d: ",ii);
		scanf("%d%d%d",&l,&m,&s);
/*
		memset(a,0,sizeof(a));
		for(i=0;i<=l;i++)
			for(j=0;j<=m;j++)
			{
				a[i*j].f=true;
				a[i*j].x=i;
				a[i*j].y=j;
			}
		*/
		i=m;
		y=s/m;
		x=s%m;
		for(j=0;j<=l-y&&f;j++)
		{
			if(x==0||(j&&(x%j==0)&&x/j<=m))
			{
				a=i;
				b=j;
				c=j+y;
				if(x==0)
					d=0;
				else
					d=x/j;
				f=false;
			}
		}
		/*
		for(i=1;i<=m;i++)
			if(s%i==0&&(s/i)<=l)
				break;*/
		if(!f)
			printf("0 %d %d 0 %d %d\n",a,b,c,d);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}