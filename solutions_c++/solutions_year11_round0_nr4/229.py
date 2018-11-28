#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int a[1005];
bool vis[1005];

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;++i)
			scanf("%d",&a[i]);
		double ans=0;
		memset(vis,false,sizeof(vis));
		for (int i=1;i<=n;++i)
		if (a[i]!=i && !vis[i])
		{
			vis[i]=true;
			int len=0,x=i;
			do
			{
				x=a[x];
				vis[x]=true;
				++len;
			}while (x!=i);
			ans+=len;
		}
		printf("Case #%d: %.6f\n",test,ans);
	}
	return 0;
}
