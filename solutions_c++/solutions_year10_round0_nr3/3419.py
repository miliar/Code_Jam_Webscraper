#include<iostream>

#define N 1005

int a[N<<1],b[N];
__int64 c[N],w[N],f[N];

int main()
{
	int cas=1,t,r,m,n,i,j,k,u,v;
	__int64 sum;
	freopen("in.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&m,&n);
		for(sum=i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		printf("Case #%d: ",cas++);
		if(m>=sum)
		{
			printf("%I64d\n",sum*r);
			continue;
		}
		for(i=0;i<n;i++)
			a[i+n]=a[i];
		for(i=0;i<n;i++)
		{
			for(sum=0,j=i;;j++)
			{
				sum+=a[j];
				if(sum>m)
					break;
			}
			c[i]=j%n;
			w[i]=sum-a[j];
		}
		memset(b,-1,sizeof(b));
		for(k=i=0;;i=c[i])
		{
			if(b[i]>=0)
			{
				u=b[i];
				break;
			}
			f[++k]=w[i];
			b[i]=k;
		}
		f[0]=0;
		for(i=1;i<=k;i++)
			f[i]+=f[i-1];
		if(r<u)
			printf("%I64d\n",f[r]);
		else
		{
			sum=(r-u+1)/(k-u+1);
			v=(r-u+1)%(k-u+1);
			sum*=(f[k]-f[u-1]);
			sum+=f[u-1+v];
			printf("%I64d\n",sum);
		}
	}
	return 0;
}
