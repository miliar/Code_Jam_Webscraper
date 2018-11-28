#include <stdio.h>
int main ()
{
	int cas,ca,n,i,sum,tt,mmin,x;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		sum=tt=0;
		mmin=10000000;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&x);
			tt^=x;
			sum+=x;
			if(x<mmin)
				mmin=x;
		}
		if(tt==0)
		{
			printf("Case #%d: %d\n",ca,sum-mmin);
		}
		else
			printf("Case #%d: NO\n",ca);


	}
}