#include<cstdio>
#include<map>
using namespace std;
const int inf=1<<30;
double p[109];
int a,b;
double solve(int t,int a)
{
	double res=1;
	for(int i=0;i<a;i++)
	{
		if(t&(1<<i))
		{
			res=res*(1-p[i]);
		}
		else res=res*p[i];
	}
	return res;
}
int Ti(int t,int a,int b,int k)
{
	if(k==1)
	{
		if(t==0)return b-a+1;
		else return b-a+1+b+1;
	}
	if(k==2)
	{
		return Ti(t/2,a-1,b,1)+1;
	}
	if(k==3)
	{
		return Ti(t/4,a-2,b,1)+2;
	}
	else return b+2;
}
int main()
{
	int ca;
	freopen(".//A-small-attempt1.in","r",stdin);
	freopen("ansA.out","w",stdout);
	scanf("%d",&ca);
	for(int ii=1;ii<=ca;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d%d",&a,&b);
		for(int i=a-1;i>=0;i--)
		{
			scanf("%lf",&p[i]);
		}
		int M=1<<a;
		double ans=inf,tmp;
		for(int ty=1;ty<=4;ty++)
		{
			tmp=0;
			for(int i=0;i<M;i++)
			{
				tmp+=solve(i,a)*Ti(i,a,b,ty);
			//	printf("%d %.2lf %d  ",i,solve(i,a),Ti(i,a,b,ty));
			}
			//printf("%d %.6lf\n",ty,tmp);
		//	puts("");
			ans=min(ans,tmp);
		}
		printf("%.6lf\n",ans);
	}
	return 0;
}