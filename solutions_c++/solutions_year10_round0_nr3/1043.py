#include<stdio.h>
#include<string.h>

int a[1001];
int u[1001];
long long sum[1001];

int main()
{
	int t,p;
	int r,k,n;
	int i,j;
	int s;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d%d%d",&r,&k,&n);
		s=0;
		for (i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			s=s+a[i];
		}
		if (s<=k)
		{
			printf("Case #%d: %lld\n",p,r*(long long)s);
			continue;
		}
		memset(u,-1,sizeof(u));
		u[1]=0;
		sum[0]=0;
		j=1;
	    for (i=1;i<=r;i++)
		{
			s=0;
			while (s<=k)
			{
				s=s+a[j];
				j++;
				if (j==n+1) j=1;
			}
			j--;
			if (j==0) j=n;
			s=s-a[j];
			sum[i]=sum[i-1]+s;
			if (u[j]>=0) break;
			u[j]=i;
		}
		long long res;
		if (i==r+1) res=sum[r];
		else res=(r-u[j])/(i-u[j])*(sum[i]-sum[u[j]])+sum[(r-u[j])%(i-u[j])+u[j]];
		printf("Case #%d: %lld\n",p,res);
	}
	return 0;
}


