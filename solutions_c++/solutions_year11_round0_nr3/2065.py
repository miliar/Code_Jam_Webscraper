#include<stdio.h>

int main()
{
	int t,n,ca=1;
	int in[1010];
	scanf("%d",&t);
	while(ca<=t)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		scanf("%d",in+i);
		int min=2000000;
		int sum=0;
		for(int i=0;i<n;i++)
		{
			if(in[i]<min)
			min=in[i];
			sum+=in[i];
		}
		int temp=0;
		for(int i=0;i<n;i++)
		{
			temp^=in[i];
		}
		if(temp)
		{
			printf("Case #%d: NO\n",ca);
		}
		else
		{
			printf("Case #%d: %d\n",ca,sum-min);
		}

		ca++;
	}
}
