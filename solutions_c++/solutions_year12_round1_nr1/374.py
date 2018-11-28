#include<stdio.h>
#include<math.h>
double sump[200001];

int main()
{
	int t,bk,a,b,i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(bk=1;bk<=t;++bk)
	{
		scanf("%d%d",&a,&b);
		sump[0]=1;
		for(i=1;i<=a;++i)
		{
			scanf("%lf",&sump[i]);
			sump[i]*=sump[i-1];
		}
		double ans=1e+20;
		for(i=a;i>=1;--i)
		{
			double now=a-i+sump[i]*(b-i+1)+(1-sump[i])*(2*b-i+2);
			if(now<ans)
				ans=now;
		}
		if(b+2<ans)
			ans=b+2;
		printf("Case #%d: %.6lf\n",bk,ans);
	}
	return 0;
}
