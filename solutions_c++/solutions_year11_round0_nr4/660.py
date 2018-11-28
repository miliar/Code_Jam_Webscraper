#include <cstdio>
using namespace std;
int test,n,ans,x;

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		scanf("%d",&n);
		ans=0;
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&x);
			if (x!=i) ans++;
		}
		printf("Case #%d: %d.000000\n",kase,ans);
	}
	
	return 0;
}
