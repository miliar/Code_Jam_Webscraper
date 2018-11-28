#include<cstdio>
#include<algorithm>
//                                      Last Change:  2011-05-07 19:51:00
using namespace std;
int n,a[1001];
double solve()
{
	double ret=0;
	for(int i=1;i<=n;++i)
	{
		int cnt=1;
		while(a[i]!=i)
		{
			++cnt;
			swap(a[i],a[a[i]]);
		}
		if(cnt>1)ret+=cnt;
	}
	return ret;
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int _;scanf("%d",&_);
	for(int cas=1;cas<=_;++cas)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;++i)scanf("%d",a+i);
		printf("Case #%d: %.6lf\n",cas,solve());
	}
	return 0;
}
