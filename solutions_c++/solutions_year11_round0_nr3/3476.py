#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>

#define PB push_back
#define M 100
#define N 5010
#define LL long long


using namespace std;






int main()
{
	
	int tc,ti;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		int arr[N],i,j,k,n,ans,sum=0;
		scanf("%d",&n);
		ans=0;
		for(i=0;i<n;++i)
		{
			scanf("%d",&arr[i]);
			ans^=arr[i];
			sum+=arr[i];
		}
		if(ans!=0)
		{
			printf("Case #%d: NO\n",ti);
		} else {
			ans=arr[0];
			for(i=1;i<n;++i)
			if(arr[i]<ans)
			ans=arr[i];
			printf("Case #%d: %d\n",ti,sum-ans);
		}
		
		
	}
	
	
	return 0;
}
