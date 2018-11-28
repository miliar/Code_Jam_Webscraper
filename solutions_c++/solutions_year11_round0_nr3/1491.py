#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int _,n,cas=0,v;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d",&n);
		int yihuo=0,minn=(1<<30),sum=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&v);
			sum+=v;
			yihuo^=v;
			minn=min(minn,v);
		}
		printf("Case #%d: ",++cas);
		if(yihuo!=0) printf("NO\n");
		else printf("%d\n",sum-minn);
	}
}
