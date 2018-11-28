#include <iostream>
#include <cstdio>


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int cs, n, s, p, x;
	scanf("%d", &cs);
	int now = 0;
	while (cs--)
	{
		scanf("%d%d%d", &n, &s, &p);
		int i, ans = 0;
		while (n--)
		{
			scanf("%d", &x);
			if (x==0)
			{
				if (x>=p) ans++;
			}
			else if (x%3==1)
			{
				if (x/3+1>=p) ans++;
			}
			else if (x%3==0)
			{
				if (x/3>=p) ans++;
				else if (x/3+1>=p && s>0) ans++,s--;
			}
			else if (x%3==2)
			{
				if (x/3+1>=p) ans++;
				else if (x/3+2>=p && s>0) ans++,s--;
			}
		}
		printf("Case #%d: %d\n", ++now, ans);
	}

	return 0;
}