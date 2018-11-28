#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
LL d[10001],l[10001],f[10001];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,t,n,i,j;
	LL D;
	scanf("%d",&T);
	for (t=1; t<=T; ++t)
	{
		scanf("%d",&n);
		for (i=1; i<=n; ++i) scanf("%I64d%I64d",d+i,l+i);
		scanf("%I64d",&D);
		memset(f,0,sizeof f);
		f[1]=d[1]*2;
		for (i=1; i<n; ++i)
			for (j=i+1; j<=n && d[j]<=f[i]; ++j)
				f[j]=max(f[j],d[j]*2-max(d[i],d[j]-l[j]));
		for (i=1; i<=n && f[i]<D; ++i);
		printf("Case #%d: ",t);
		if (i<=n) puts("YES"); else puts("NO");
	}
	return 0;
}
