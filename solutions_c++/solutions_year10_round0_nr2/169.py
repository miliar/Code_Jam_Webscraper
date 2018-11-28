#include<stdio.h>
#include<algorithm>
#define N 1000+10
using namespace std;
_int64 a[N];

_int64 gcd(_int64 a,_int64 b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}

int main()
{
	int t,i,j,n;
	_int64 ans,last;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d",&n);
		for(j=0;j<n;++j)
			scanf("%I64d",&a[j]);
		sort(a,a+n);
		last=a[0];              //最近一次发生的时间
		for(j=1;j<n;++j)
			a[j-1]=a[j]-a[j-1];
		--n;
		ans=a[0];
		for(j=1;j<n;++j)
			ans=gcd(ans,a[j]);
		_int64 temp=ans;
		ans=(last/temp+1)*ans-last;
		ans%=temp;
		printf("Case #%d: %I64d\n",i,ans); 
	}
	return 0;
}