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

long arr[10005];

int main()
{
	long t,cas=0,l,h,n,i,j,cnt,ans;
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("c.out","w",stdout);
	scanf("%ld",&t);
	while(t--)
	{
		scanf("%ld%ld%ld",&n,&l,&h);
		for(i=0;i<n;i++){scanf("%ld",&arr[i]);}
		for(i=l;i<=h;i++)
		{
			cnt=0;
			for(j=0;j<n;j++)
			{
				if(i%arr[j]==0||arr[j]%i==0){ans=i;cnt++;}
				else{break;}
			}
			if(cnt==n){break;}
		}
		if(cnt!=n){printf("Case #%ld: NO\n",++cas);}
		else{printf("Case #%ld: %ld\n",++cas,ans);}
	}
	return 0;
}