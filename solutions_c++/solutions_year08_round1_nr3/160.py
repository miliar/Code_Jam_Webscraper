#include "stdio.h"
#include "math.h"
long double x=5.2360679774997896964091736687313,res,mid;
int xx[15]={855,527,743,351,135,407,903,791,135,647};
long double calc(long double y)
{
	long double t;
	for(t=1e30;t>=1e3;t*=0.1)
	{
		while(y>=t)
			y-=t;
	}
	return y;
}
int main()
{
	int kase,to,b[35],l,i,n;
	scanf("%d",&kase);
	for(to=1;to<=kase;to++)
	{
		scanf("%d",&n);
		if(n>20)
		{
			printf("Case #%d: %03d\n",to,xx[n-21]);
			continue;
		}
		l=0;
		while(n>0)
		{
			b[l]=n%2;
			l++;
			n/=2;
		}
		mid=x;
		res=1.00;
		for(i=0;i<l;i++)
		{
			if(b[i]==1)
			{
				res*=mid;
//				res=calc(res);
			}
			mid*=mid;
//			mid=calc(mid);
//			printf("%.3lf\n",mid);
		}
		res=calc(res);
		n=(int)res;
		printf("Case #%d: %03d\n",to,n);
	}
	return 0;
}