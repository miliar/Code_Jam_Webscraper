#include <iostream>
#include <cstdio>
using namespace std;
int g,t,i,a,b;
double sp,tmp,ans;
double p[100010];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for(g=1;g<=t;g++)
	{
		scanf("%d%d",&a,&b);
		for(i=1;i<=a;i++) scanf("%lf",&p[i]);
		sp=1; ans=2000000000;
		for(i=1;i<=a;i++)
		{
			sp*=p[i];
			tmp=sp*(b+a+1-2*i)+(1-sp)*(2*b+a+2-2*i);
			//printf("bs[%d]=%.6lf\n",i,tmp);
			if(tmp<ans) ans=tmp;
		}
		if(b+2<ans) ans=b+2;
		printf("Case #%d: %.6lf\n",g,ans);
	}
	return 0;
}
