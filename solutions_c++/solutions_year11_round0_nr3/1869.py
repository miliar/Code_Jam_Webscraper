#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int T,n,mn,sum,a,ret;
	freopen("C-large.in","r",stdin);
	freopen("Clarge.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&n);
		sum=0;
		ret=0;
		mn=10000000;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a);
			sum+=a;
			ret^=a;
			if(mn>a)	mn=a;
		}
		if(ret)
			printf("Case #%d: NO\n",t);
		else
			printf("Case #%d: %d\n",t,sum-mn);
	}
}
