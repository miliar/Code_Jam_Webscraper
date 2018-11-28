#include<functional>
#include<cstdio>
#include<algorithm>
using namespace std;
#define MAXN 800
int v1[MAXN],v2[MAXN];
int main()
{
	int t;
	int n;
	int sum;
	scanf("%d",&t);
	for (int k=1;k<=t;++k)
	{
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d",v1+i);
		for (int i=0;i<n;++i)
			scanf("%d",v2+i);
		sort(v1,v1+n);
		sort(v2,v2+n,greater<int>());
		sum=0;
		for (int i=0;i<n;++i)
			sum+=v1[i]*v2[i];
		printf("Case #%d: %d\n",k,sum);
	}
	return 0;
}