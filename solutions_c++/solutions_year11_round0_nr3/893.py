#include<stdio.h>
#include<string.h>
int a[1000];
int main()
{
	int t,tt,n,i,x,s,ss;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		s=ss=0;
		x=10000000;
		for (i=0;i<n;i++)
		{
			scanf("%d",a+i);
			if (a[i]<x)
				x=a[i];
			s^=a[i];
			ss+=a[i];
		}
		if (s!=0)
			printf("Case #%d: NO\n",tt);
		else
			printf("Case #%d: %d\n",tt,ss-x);
	}
	return 0;
}