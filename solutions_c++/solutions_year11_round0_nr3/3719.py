#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<vector>
#include<sstream>
#include<utility>
#include<string>
using namespace std;

int main()
{
	__int64 t,cas=0,n,i,arr[1005],ans,sum;
//	freopen("C-large.in","r",stdin);
//	freopen("big.out","w",stdout);
	scanf("%I64d",&t);
	while(t--)
	{
		scanf("%I64d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&arr[i]);
		}
		sort(arr,arr+n);
		ans=0;
		sum=0;
		for(i=0;i<n;i++)
		{
			ans^=arr[i];
			sum+=arr[i];
		}
		if(ans==0){printf("Case #%I64d: %I64d\n",++cas,sum-arr[0]);}
		else{printf("Case #%I64d: NO\n",++cas);}
	}
	return 0;
}