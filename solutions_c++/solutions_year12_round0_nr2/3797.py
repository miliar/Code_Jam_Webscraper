#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, i, n, s, p, tmp, ans, cnt, cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d", &n, &s, &p);
		for(i = 0, cnt = 0, ans = 0; i < n; i++)
		{
			scanf("%d", &tmp);
			if(tmp == 0)
			{
				if(p == 0)
					ans++;
				continue;
			}
			if(tmp == 1)
			{
				if(p <= 1)
					ans++;
				continue;
			}
			if((tmp - 1) % 3 == 0)
			{
				if((tmp + 2) / 3 >= p)
					ans++;
			}
			else if(tmp % 3 == 0)
			{
				if(tmp / 3 >= p)
					ans++;
				else if((tmp + 3) / 3 >= p)
					cnt++;
			}
			else if((tmp - 2) % 3 == 0)
			{
				if((tmp + 1) / 3 >= p)
					ans++;
				else if((tmp + 4) / 3 >= p)
					cnt++;
			}
		}
		if(cnt >= s)
			ans += s;
		else
			ans += cnt;
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}
