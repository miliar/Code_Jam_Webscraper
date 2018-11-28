#include<stdio.h>

int num[1000];
int digitsum[21];

int main()
{
	int ncase,tcase,i,j,t,n,min,sum;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		for(i=0;i<21;i++)
		{
			digitsum[i]=0;
		}
		scanf("%d",&n);
		min=9999999;
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			sum+=t;
			num[i]=t;
			if(t<min)
				min=t;
			for(j=0;j<21;j++)
			{
				digitsum[j]+=t%2;
				t/=2;
			}	
		}
		t=0;
		for(i=0;i<21;i++)
		{
			if(digitsum[i]%2==1)
			{
				t=1;
				break;
			}
		}
		if(t==1)
		{
			printf("Case #%d: NO\n",tcase);
		}
		else
		{
			printf("Case #%d: %d\n",tcase,sum-min);
		}
	}
	return 0;
}
