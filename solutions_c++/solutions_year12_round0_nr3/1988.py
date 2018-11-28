#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>

#define FF(i, a, b) for (int i=a; i<=b; i++)
#define FI(i, a, b) for (int i=a; i>=b; i--)

using namespace std;

int q[100];

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	int a, b;
	FF(t, 1, tt)
	{
		scanf("%d%d", &a, &b);
		int ans = 0;
		if (a < 10) a = 10;
		int p = 1, w = 1;
		FF(i, a, b)
		{
			while (p * 10 <= i)
			{
				p = p * 10;
				w++;
			}
			int x = i;
			int r = 0;
			FF(j, 1, w - 1)
			{
				bool flag = true;
				if (x % 10 == 0) flag = false;
				x = (x % 10) * p + x / 10;
				FF(k, 1, r)
					if (x == q[k])
						flag = false;
				if (flag && i < x && x <= b)
				{
					ans++;
					q[++r] = x;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
