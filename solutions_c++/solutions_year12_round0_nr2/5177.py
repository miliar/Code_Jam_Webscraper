#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

int T,n,s,P,ans,t[1010],j;

int main()
{
	freopen("bb.in","r",stdin);
	freopen("bb.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d%d",&n,&s,&P);
		for(j=1;j<=n;j++)
			scanf("%d",&t[j]);
		sort(t+1,t+1+n);
		ans=0;
		for(j=n;j;j--)
		{
			if(P>=2)
			{
				if(!s&&t[j]<3*P-2)
					break;
				if(t[j]>=3*P-2)
					ans++;
				else if(t[j]>=3*P-4&&s)
				{
					ans++;
					s--;
				}
			}
			else
			{
				if(t[j])
					ans++;
				else if(!t[j]&&!P)
					ans++;
				else if(!t[j]&&P)
					break;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
