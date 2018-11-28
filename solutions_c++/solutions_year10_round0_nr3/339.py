#include <cstdio>
#include <memory>

#define N 1005

int n,p,r,k,i,test,t,j;
int a[N],c[N];
long long f[N],cur,sum;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%d%d%d",&r,&k,&n);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		if(sum<=k)
		{
			printf("Case #%d: %I64d\n",t,sum*r);
			continue;
		}
		memset(f,-1,sizeof(f));
		memset(c,0,sizeof(c));
		i=0;
		cur=0;
		p=0;
		bool flag;
		while(p<r)
		{
			if(f[i]!=-1)
			{
				cur=f[i]+(cur-f[i])*((r-c[i])/(p-c[i]));
				p=c[i]+((r-c[i])/(p-c[i]))*(p-c[i]);
			}
			if(p>=r) break;
			f[i]=cur;
			c[i]=p;
			sum=0;
			j=i;
			flag=1;
			while(flag)
			{
				if(sum+a[j]<=k)
				{
					sum+=a[j];
					j=(j+1)%n;
				}else
					flag=0;
				if(j==i)
					flag=0;
			}
			cur=f[i]+sum;
			i=j;
			p++;
		}
		printf("Case #%d: %I64d\n",t,cur);
	}
	return 0;
}
