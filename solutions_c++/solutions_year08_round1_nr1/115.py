#include <cstdio>
#include <algorithm>
using namespace std;

int x[801],y[801],T,n;

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int i = 1;i <= T;++i)
	{
		scanf("%d",&n);
		for(int j = 0;j < n;++j)
			scanf("%d",&x[j]);
		for(int k = 0;k < n;++k)
			scanf("%d",&y[k]);
		sort(x,x+n);
		sort(y,y+n);
		long long ans = 0;
		for(int j = 0;j < n;++j)
			ans += (long long)(x[j])*y[n-1-j];
		printf("Case #%d: %lld\n",i,ans);
	}
	return 0;
}