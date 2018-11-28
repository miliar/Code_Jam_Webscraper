#include<cstdio>
#include<iostream>
#include<cmath>
#include<climits>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int p,n;
		long long int ans,sum;
		int mini=INT_MAX;
		sum=ans=0;
		scanf("%d",&n);
		while(n--)
		{
			cin>>p;
			ans^=p;
			mini=min(mini,p);
			sum+=p;
		}
		if(ans==0)
			printf("Case #%d: %lld\n",tc,sum-mini);
		else
			printf("Case #%d: NO\n",tc);
	}
	return 0;
}
