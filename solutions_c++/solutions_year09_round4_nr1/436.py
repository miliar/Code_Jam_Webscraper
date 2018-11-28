#include<stdio.h>

int n,count[50],c[50],od[50];

int process()
{
	int i,j,cnt;
	for(i=0;i<n;i++) c[i]=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(c[j]==0 && count[j]<=i)
			{
				c[j]=1;
				od[i]=j;
				break;
			}
		}
	}
	cnt=0;
	for(i=n-1;i>-1;i--)
	{
		for(j=0;j<=i;j++)
		{
			if(od[j]==i) break;
		}
		for(;j<i;j++){ od[j]=od[j+1]; cnt++; }
		od[i]=i;
	}
	return cnt;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,t,res,x;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			count[j]=-1;
			for(k=0;k<n;k++)
			{
				scanf("%1d",&x);
				if(x==1) count[j]=k;
			}
		}
		res=process();
		printf("Case #%d: %d\n",i,res);
	}
}