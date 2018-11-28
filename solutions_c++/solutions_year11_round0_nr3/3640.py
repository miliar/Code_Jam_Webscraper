#include<stdio.h>
#include<string.h>
long long a[1003];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,n,i,j,k,ans,cas=0,min;
	long long sum;
	scanf("%d",&t);
	while(t--)
	{
		memset(a,0,sizeof(a));
		cas++;
		sum=0; ans=1;
		min=1000002;
		scanf("%d",&n);
		for(i=1;i<=n;i++) 
		{
			scanf("%lld",&a[i]);
			sum+=a[i];
			if(min>a[i]) min=a[i];
		}
		ans=a[1];
		for(i=2;i<=n;i++) 
		{
			ans^=a[i];	
		}
		if(ans) printf("Case #%d: NO\n",cas);
		else printf("Case #%d: %lld\n",cas,sum-min);
	}
	return 0;	
}