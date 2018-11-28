#include<cstdio>
#include<algorithm>
//            Last Change:  2011-05-07 08:41:26
using namespace std;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;++cas)
	{
		int n,a=1,b=1,ta=0,tb=0;
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
		{
			char c=' ';
			while(c!='O'&&c!='B')c=getchar();
			int x;scanf("%d",&x);
			if(c=='O')
			{
				ta+=abs(x-a)+1;
				ta=max(ta,tb+1);
				a=x;
			}
			else
			{
				tb+=abs(x-b)+1;
				tb=max(ta+1,tb);
				b=x;
			}
		}
		printf("Case #%d: %d\n",cas,max(ta,tb));
	}
	return 0;
}
