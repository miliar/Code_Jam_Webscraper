#include <stdio.h>
#include <algorithm>
using namespace std;
long long gcd(long long a,long long b)
{
	return !b?a:gcd(b,a%b);
}
long long f(long long a,long long b)
{
	return a*b/gcd(a,b);
}
long long a[200];
long long l,h,n;
long long solve()
{
	long long i;
	long long tmp=1;
	for(i=0;i<n-1;i++)
	{
		tmp=f(tmp,a[i]);
		if(tmp>1000000)
			return -1;
	}
	for(i=l;i<=h;i++)
	{
		if(a[n-1]%f(tmp,i)==0)
			return i;
	}
	tmp=f(tmp,a[n-1]);
	for(i=l;i<=h;i++)
	{
		if(i%tmp==0)
			return i;
	}
	return -1;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	long long T;
	scanf("%lld",&T);
	for(long long _=1;_<=T;_++)
	{
		scanf("%lld%lld%lld",&n,&l,&h);
		long long i;
		for(i=0;i<n;i++)
			scanf("%lld",&a[i]);
		printf("Case #%lld: ",_);
		sort(a,a+n);
		long long ans=solve();
		if(ans==-1)
			printf("NO\n");
		else
			printf("%lld\n",ans);
	}
	return 0;
}