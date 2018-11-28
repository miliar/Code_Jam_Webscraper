#include<iostream>
#include<algorithm>
using namespace std;
__int64 gcd(__int64 a,__int64 b)
{
	__int64 r;
	while(b)
	{
		r=a;
		a=b;
		b=r%b;
	}
	return a;
}
__int64 a[1001];
int main()
{
	__int64 d,d1,ans;
	int i,cas,ii,n;
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%I64d",&a[i]);
		sort(a,a+n);
		d=a[1]-a[0];
		for(i=2;i<n;i++)
		{
			d1=a[i]-a[i-1];
			d=gcd(d,d1);
		}
		ans=(d-a[0]%d)%d;
		printf("Case #%d: %I64d\n",ii,ans);
	}
	return 0;
}
