#include <stdio.h>

int T,i,j,k,ans,p[20000],n,a,b,x[20],t,ma,p10[20],d,ima,imi,pans;

int obr(int x)
{
	int k=p[i]-2;
	__int64 k1=1,k2=x%p[i];
	while(k)
		if(k%2)
		{
			k1*=k2;
			k1%=p[i];
			k--;
		}
		else
		{
			k2*=k2;
			k2%=p[i];
			k/=2;
		}
	return k1;
}

int main()
{
	freopen("a.in","r",stdin);	freopen("a.out","w",stdout);
	for(i=2;i*i<=10000;i++)
		if(!p[i])
			for(j=i*i;j<=10000;j+=i)
				p[j]=1;
	for(i=2;i<10000;i++)
		if(!p[i])
			p[k++]=i;
	p10[0]=1;
	for(i=1;i<10;i++)
		p10[i]=p10[i-1]*10;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d",&d,&n);
		ma=0;
		ans=-1;
		for(i=0;i<n;i++)
		{
			scanf("%d",&x[i]);
			ma=ma>x[i]?ma:x[i];
		}
		for(i=0;i<n-1;i++)
			if(x[i]==x[n-1])
				break;
		if(i!=n-1)
		{
			printf("%d\n",x[i+1]);
			continue;
		}
		if(n<3)
		{
			printf("I don't know.\n");
			continue;
		}
		for(i=0;i<k;i++)
			if(p[i]>ma)
				break;
		imi=i;
		for(i=k-1;i>=0;i--)
			if(p[i]<=p10[d])
				break;
		ima=i;
		for(i=imi;i<=ima;i++)
		{
			if(p[i]<=ma)
				continue;
			if(p[i]>p10[d])
				break;
			a=(__int64)(x[2]-x[1]+p[i])%p[i]*obr(x[1]-x[0]+p[i])%p[i];
			b=(x[1]-x[0]*a%p[i]+p[i])%p[i];
			for(j=1;j<n;j++)
				if(x[j]!=(x[j-1]*a+b)%p[i])
					break;
			if(j==n)
			{
				pans=(x[n-1]*a+b)%p[i];
				if(ans==-1 || ans==pans)
					ans=pans;
				else
					break;
			}
		}
		if(ans==-1 || i<=ima)
			printf("I don't know.\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}