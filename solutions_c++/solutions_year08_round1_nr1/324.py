#include<iostream>
#include<algorithm>
using namespace std;
long long v1[814],v2[814];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas,n;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		long long sum=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lld",&v1[i]);
		for(int i=0;i<n;i++)
			scanf("%lld",&v2[i]);
		sort(v1,v1+n);
		sort(v2,v2+n);
		for(int i=0;i<n;i++)
			sum+=v1[i]*v2[n-i-1];
		printf("Case #%d: %lld\n",ca,sum);
	}
}