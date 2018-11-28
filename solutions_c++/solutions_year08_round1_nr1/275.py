#include <iostream>
#include <algorithm>
using namespace std;

long long a[805],b[805];
int main()
{
	int nca,i,n,ca;
	long long ans;
	freopen("A-large.in","r",stdin);
	freopen("11.out","w",stdout);
	scanf("%d",&nca);
	for(ca=1;ca<=nca;ca++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lld",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lld",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		ans = 0;
		for(i=0;i<n;i++)
			ans+=a[i]*b[n-1-i];
		printf("Case #%d: %lld\n",ca,ans);
	}
	return 0;
}