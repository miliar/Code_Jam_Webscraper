#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int n,D,tests,test,ok;
int d[100010],l[100010],f[100010];

int main()
{
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d%d",d+i,l+i);
		scanf("%d",&D);
		memset(f,0,sizeof f);
		f[1] = d[1];
		ok = 0;
		for (int i=1;i<=n;i++)
		{
			if (d[i]+f[i] >= D) ok = 1;
			for (int j=i+1;j<=n;j++)
			{
				if (d[i]+f[i]>=d[j])
				{
					f[j] = max(f[j], min(l[j],d[j]-d[i]));
				}
				else break;
			}
		}
		printf("Case #%d: ",test);
		if (ok) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
