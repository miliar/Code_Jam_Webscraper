#include<iostream>

using namespace std;

int main()
{
	
	int tt,cas;
	int n,k,b,t;
	int p[55],v[55];
	int i,j;

	freopen("B-large.in","r",stdin);
	freopen("out","w",stdout);

	cas=0;
	scanf("%d",&tt);
	for (cas=1;cas<=tt;cas++)
	{
		cin>>n>>k>>b>>t;
		for (i=0;i<n;i++)
			cin>>p[i];
		for (i=0;i<n;i++)
			cin>>v[i];

	int ans=0;
	int good=0;
	int bad=0;

	for (i=n-1;i>=0;i--)
	{
		if (p[i]+(long long )v[i]*t<(long long )b) //bad
			bad++;
		else
		{
			good++;
			ans+=bad;
			if (good==k) break;
		}
	}

	//printf("good=%d,bad=%d\n",good,bad);
	
	printf("Case #%d: ",cas);
	if (good<k)
			puts("IMPOSSIBLE");
	else
		printf("%d\n",ans);
	}
	return 0;
}
