#include<cstdio>
#include<cstring>

const int mx=110;

int n,k;
__int64 b,t;
__int64 x[mx],v[mx];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int i,tt,ca=1;
	scanf("%d",&tt);
	while(tt--)
	{
		scanf("%d%d%I64d%I64d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%I64d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%I64d",&v[i]);
		int cnt=0,can=0;
		int ans=0;
		for(i=n-1;i>=0;i--)
		{
			if(x[i]+v[i]*t>=b)
			{
				can++;
				ans+=cnt;
			}
			else
				cnt++;
			if(can==k)break;
		}
		if(can==k)
			printf("Case #%d: %d\n",ca++,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",ca++);
	}

	return 0;
}
