#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,T;
	int i,j,a[809],b[809],n;
	__int64 sum=0;
	scanf("%d",&T);
	for(t=0;t<T;t++)
	{
		sum=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a,a+n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&b[i]);
		}
		sort(b,b+n);
		for(i=0,j=n-1;i<n;i++,j--)
			sum+=(__int64)a[i]*(__int64)b[j];
		printf("Case #%d: %I64d\n",t+1,sum);
	}
	return 0;
}