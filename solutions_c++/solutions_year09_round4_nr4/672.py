#include<iostream>
#include<cmath>
#include<queue>
using namespace std;
struct node
{
	int x,y,z;
}s[234];
int m;
bool check(double mid)
{
	return 1;
}
double min(double a,double b)
{
	if(a<b)
		return a;
	return b;
}
double max(double a,double b)
{
	if(a>b)
		return a;
	return b;
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	for(int ca=1;ca<=zu;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%d",&m);
		for(int i=0;i<m;i++)scanf("%d%d%d",&s[i].x,&s[i].y,&s[i].z);
		/*double h=0,r=1e4;
		double res=r;
		while(fabs(r-h)>=1e-10)
		{
			double mid=r+h;
			mid/=2;
			if(check(mid))
			{
				res=r;
				r=mid;
			}
			else
			{
				h=mid;
			}
		}*/
		double res=0;
		if(m<=2)
		{
			for(int i=0;i<m;i++)
				res=max(res,s[i].z*1.0);
		}
		else
		{
			res=1e4;
			int a[2];
			for(int i=0;i<m;i++)
			{
				int ind=0;
				for(int j=0;j<m;j++)
				{
					if(i==j)continue;
					a[ind++]=j;
				}
				int x=a[0],y=a[1];
				res=min(res,max(s[i].z*1.0,sqrt(0.0+(s[x].x-s[y].x)*(s[x].x-s[y].x)+(s[x].y-s[y].y)*(s[x].y-s[y].y))+s[x].z+s[y].z));
			}
			res/=2;
		}
		printf("%.6lf\n",res);
	}
}