#include <iostream>
#include <cstdio>
using namespace std;

int ans,n,S,p,T,t[150],cnt;

int main()
{
	freopen("b.in","r",stdin);freopen("b.out","w",stdout);
	
	for (scanf("%d",&T);T;T--)
	{
		ans=0;
		scanf("%d%d%d",&n,&S,&p);
		for (int i=1;i<=n;i++) scanf("%d",&t[i]);
		for (int i=1;i<=n;i++)
		{
			if ((t[i]+2)/3>=p) ans++;
			else if ((t[i]%3==2 || t[i]%3==0) && (t[i]+2)/3==p-1 && S && t[i]>=p) {S--;ans++;} 
		}
		printf("Case #%d: %d\n",++cnt,ans);
	}

	return 0;
}
