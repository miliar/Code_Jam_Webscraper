#include <iostream>
#include <math.h>
using namespace std;
int main ()
{
	freopen("al.txt","r",stdin);
	freopen("ansl.txt","w",stdout);
	int T;
	int t,l,p,c,i;
	double ans;
	double x;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d%d",&l,&p,&c);
		x=l;
		for(i=0;;i++)
		{
			x*=c;
			if(x>=p)break;
		}
		if(i==0)ans=0;
		else 
			ans=log(i)/log(2);
		if(i==1)ans=1;
		if(ans!=int(ans))ans+=0.5;
		if(ans==int(ans)&&ans!=0)
		{
			if(i%2==0)ans++;
		}
		printf("Case #%d: %.0lf\n",t,ans);
	}
}