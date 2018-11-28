#include<iostream>

using namespace std;

int s[100],n,t,ans,maxc[100];
bool used[100];

void checker()
{
	for(int i=1;i<=n;++i)
		if(s[i]<maxc[i])
			return ;
	int d=0;
	for(int i=1;i<=n;++i)
		for(int j=i+1;j<=n;++j)
			if(s[i]>s[j])
				++d;
	ans=min(ans,d);
}

void search(int deep)
{
	if(deep>n)
	{
		checker();
		return ;
	}
	for(int i=1;i<=n;++i)
		if(!used[i])
		{
			used[i]=1;
			s[deep]=i;
			search(deep+1);
			used[i]=0;
		}
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt)
	{
		scanf("%d",&n);
		memset(maxc,0,sizeof(maxc));
		memset(used,0,sizeof(used));
		ans=1<<30;
		scanf("\n");
		for(int i=1;i<=n;++i)
		{
			for(int j=1;j<=n;++j)
			{
				char c;
				scanf("%c",&c);
				if(c=='1')
					maxc[i]=j;
			}
			scanf("\n");
		}
		search(1);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
