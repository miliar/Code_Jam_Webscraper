#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int n,T,Goal,d[101000],L[101000],f[101000],CASES;
bool ok;

int main()
{
	freopen("a.in","r",stdin);freopen("a.out","w",stdout);
	
	for (scanf("%d",&T);T;T--)
	{
		memset(f,0,sizeof(f));
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d%d",&d[i],&L[i]);
		scanf("%d",&Goal);
		f[1]=d[1];ok=false;
		for (int i=1;i<=n;i++)
		{
			for (int j=i-1;j>=1;j--)
			{
				if (f[j]+d[j]>=d[i])
				{
					f[i]=max(d[i]-d[j],f[i]);
				}
			}
			f[i]=min(f[i],L[i]);
			if (d[i]+f[i]>=Goal) { ok=true;break; }
		}
		if (ok) printf("Case #%d: YES\n",++CASES);else printf("Case #%d: NO\n",++CASES);
	}
	
	return 0;
}