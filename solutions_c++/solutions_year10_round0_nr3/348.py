#include<stdio.h>
#include<string.h>
#define MAX 2001
int a[MAX],cnt[MAX],next[MAX];
int main()
{
	int cs,r,k,n,i,j,d,sum;
	long long ans;
	scanf("%d",&cs);
	for(d=1;d<=cs;d++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			a[n+i]=a[i];
		}
		for(i=0;i<n;i++)
		{
			for(sum=0,j=i;j<i+n;j++)
			{
				if(sum+a[j]>k)
					break;
				sum+=a[j];
			}
			cnt[i]=sum;
			next[i]=j%n;
		}
		for(ans=i=j=0;i<r;i++)
		{
			ans+=cnt[j];
			j=next[j];
		}
		printf("Case #%d: %lld\n",d,ans);
	}
}
