#include<stdio.h>
#include<string.h>
int num,tot,n;
int g[1010],tim[1010];
long long int a[1010];
long long int calc(int num,int s,int e)
{
	num++;
	long long int ans=0;
	if(num<s)
	{
		for(int i=1; i<num; i++)
			ans+=a[i];
	}
	else
	{
		for(int i=s; i<e; i++)
			ans+=a[i];
		ans*=(num-s)/(e-s);
		for(int i=0; i<(num-s)%(e-s); i++)
			ans+=a[s+i];
		for(int i=1; i<s; i++)
			ans+=a[i];
	}
	return ans;
}
int main()
{
	int _,t;
	long long int ans;
	scanf("%d",&_);
	for(t=1; t<=_; t++)
	{
		scanf("%d%d%d",&num,&tot,&n);
		for(int i=0; i<n; i++)
			scanf("%d",&g[i]);
		int fir=0;
		memset(tim,-1,sizeof(tim));
		long long int qq=0;
		for(int i=0; i<n; i++)
			qq+=g[i];
		if(qq<=tot)
		{
			ans=qq*num;
		}
		else
		for(int i=1;;i++)
		{
			if(tim[fir]==-1)
				tim[fir]=i;
			else
			{
				ans=calc(num,tim[fir],i);
				break;
			}
			long long int&now=a[i];
			now=0;
			while(now+g[fir]<=tot)
			{
				now+=g[fir++];
				if(fir==n)fir=0;
			}
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}