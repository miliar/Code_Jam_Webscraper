#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

int flag[1005];
int tem[1005];

int main()
{
	int i,j;
	int cas=1;
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;scanf("%d",&t);
	while(t--)
	{
		memset(flag,0,sizeof(flag));
		int n;scanf("%d",&n);
		double ans=0;
		for(i=1;i<=n;++i)
			scanf("%d",tem+i);
		for(i=1;i<=n;++i)
		{
			if(!flag[i])
			{
				int p=i;
				int cnt=0;
				while(!flag[p])
				{
					cnt++;flag[p]=1;
					p=tem[p];
				}
				if(cnt!=1)
					ans+=cnt;
			}
		}
		printf("Case #%d: %.6f\n",cas++,ans);
	}
}