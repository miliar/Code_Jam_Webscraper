#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

int T,N,S,P,ans,t[1010];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d%d",&N,&S,&P);
		for(int j=1;j<=N;j++)
			scanf("%d",&t[j]);
		sort(t+1,t+1+N);
		ans=0;
		for(int j=N;j;j--)
		{
			if(P>=2)
			{
				if(!S&&t[j]<3*P-2)
					break;
				if(t[j]>=3*P-2)
					ans++;
				else if(t[j]>=3*P-4&&S)
				{
					ans++;
					S--;
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
