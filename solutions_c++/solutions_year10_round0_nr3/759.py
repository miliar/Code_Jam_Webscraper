#include <iostream>
#include <cstring>
using namespace std;
int T,t,r,k,n,i,a[1000],j,ri,ii,val[1001],app[1000];
long long ans,sum,temp;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		ans=0;
		memset(val,0,sizeof(val));
		memset(app,0,sizeof(app));
		i=0;app[i]=1;
		for(ri=1;ri<=1000;ri++)
		{
			ii=i;
			for(j=0,sum=0;j<n&&sum+a[ii]<=k;ii=(ii+1)%n,j++)
				sum+=a[ii];
			val[ri]=sum;
			i=ii;
			if (app[i]) break;
			app[i]=ri+1;
		}
		if (r<=ri)
			for(i=1;i<=r;i++)
				ans+=val[i];
		else
		{
			for(j=1;j<app[i];j++)
				ans+=val[j];
			r-=app[i]-1;
			temp=0;
			for(j=app[i];j<=ri;j++)
				temp+=val[j];
			ans+=temp*(r/(ri-app[i]+1));
			r%=ri-app[i]+1;
			for(ii=0,j=app[i];ii<r&&j<=ri;ii++,j++)
				ans+=val[j];
		}
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}