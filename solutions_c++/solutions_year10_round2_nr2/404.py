#include<iostream>
#include<algorithm>
struct W
{
	int x,v;
	bool operator<(W b)
	{
		return x>b.x;
	}
}d[50];
int main()
{
	int T,cs,i,j,n,k,b,t,ct,ans;
	freopen("B-Large.in","r",stdin);
	freopen("B-Large.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%d",&d[i].x);
		for(i=0;i<n;i++)
			scanf("%d",&d[i].v);
		std::sort(d,d+n);
		for(ans=ct=i=0;i<n;i++)
			if(d[i].x+d[i].v*t>=b)
			{
				for(j=0;j<i;j++)
					if(d[j].x+d[j].v*t<b)ans++;
				ct++;
				if(ct==k)break;
			}
		if(ct<k)
		{
			printf("Case #%d: IMPOSSIBLE\n",cs);
			continue;
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}