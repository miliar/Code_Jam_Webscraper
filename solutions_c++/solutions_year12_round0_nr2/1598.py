#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int tests,n,s,p,cnt,ans,x;

int main()
{
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d%d%d",&n,&s,&p);
		cnt = ans = 0;
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&x);
			if (x>(p-1)*3) ans++;
			else if (x>(p-1)*3-2 && x>0) cnt++;
		}
		ans += min(s,cnt);
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
