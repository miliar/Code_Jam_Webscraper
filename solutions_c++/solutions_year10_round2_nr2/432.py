#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#define inf 214748364
#define maxn 51
using namespace std;
long long tim,n,k,b,t;
bool bo[maxn];
long long x[maxn],v[maxn];
long long con[maxn];
int  main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&tim);
	for(int tt=1;tt<=tim;tt++)
	{
		printf("Case #%d: ",tt);
		cin>>n>>k>>b>>t;
		memset(bo,0,sizeof(bo));
		for(long long i=1;i<=n;i++)
			cin>>x[i];
		long long cnt=0;
		for(long long i=1;i<=n;i++)
		{
			cin>>v[i];
			if(x[i]+v[i]*t>=b)
				bo[i]=1,cnt++,con[i]=0;
				else
				con[i]=inf;
		}
		if(cnt<k)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(long long i=1;i<=n;i++)
		if(bo[i])
		for(long long j=1;j<=n;j++)
		if(i!=j&&x[j]>x[i]&&!bo[j])
		{
			if(con[i]>inf)
				con[i]=0;
			con[i]++;
		}
		for(long long i=1;i<n;i++)
		for(long long j=1;j<n;j++)
		if(con[j]>con[j+1])
			swap(con[j],con[j+1]);
		long long res=0;
		for(long long i=1;i<=k;i++)
			res+=con[i];
		cout<<res<<'\n';
	}
	return 0;
}
