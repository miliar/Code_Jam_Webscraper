#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 1002

int n;
__int64 na[maxn],nb[maxn];

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int cas,i,ii;
	scanf("%d",&cas);
	for(ii = 1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%I64d",&na[i]);
		for(i=0;i<n;i++)
			scanf("%I64d",&nb[i]);
		sort(na,na+n);
		sort(nb,nb+n);
		__int64 ans = 0 ;
		for(i=0;i<n;i++)
		{
			ans += na[i]*nb[n-i-1];
		}
		printf("Case #%d: %I64d\n",ii,ans);
	}
	return 0;
}