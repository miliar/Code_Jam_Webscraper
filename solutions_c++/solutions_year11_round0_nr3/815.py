#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int a[1005];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		int n;
		scanf("%d",&n);
		int tot=0;
		for (int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for (int i=1;i<=n;i++)
			tot=tot^a[i];
		if (tot!=0) printf("NO\n");
		else
		{
			int ans=0;
			sort(a+1,a+n+1);
			for (int i=2;i<=n;i++)
				ans+=a[i];
			printf("%d\n",ans);
		}
	}
}
