#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int n,tree[1005],a[1005];

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",cas);
		memset(tree,0,sizeof(tree));
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		int ans=0;
		for (int i=1;i<=n;i++)
		{
			if (a[i]==i) continue;
			else ans++;
		}
		printf("%d\n",ans);
	}
}