#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main()
{
	int i,t,n,r,cas = 1,cnt[2],res[2],ans,d,x;
	char a;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		cnt[0] = cnt[1] = 1;
		res[0] = res[1] = 0;
		ans = 0;
		getchar();
		for (i = 0;i < n;i++)
		{
			scanf("%c %d",&a,&r);
			getchar();
			if (a == 'O')
				x = 0;
			if (a == 'B')
				x = 1;
			d = abs(cnt[x] - r) + 1;
			if (res[x] >= d - 1)
			{
				res[x] = 0;
				ans++;
				res[1 - x]++;
			}
			else
			{
				ans += d - res[x];
				res[1 - x] += d - res[x];
				res[x] = 0;
			}
			cnt[x] = r;
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}