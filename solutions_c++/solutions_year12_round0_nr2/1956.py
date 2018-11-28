#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>

#define FF(i, a, b) for (int i=a; i<=b; i++)
#define FI(i, a, b) for (int i=a; i>=b; i--)

using namespace std;

int a[200];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	int n, s, p;
	FF(t, 1, tt)
	{
		scanf("%d%d%d", &n, &s, &p);
		FF(i, 1, n)
			scanf("%d", &a[i]);

		int ans = 0;
		FF(i, 1, n)
		{
			if (a[i] % 3 == 0)
			{
				if (a[i] / 3 >= p) 
					ans++;
				else if (a[i] / 3 + 1 >= p && s > 0 && a[i] / 3 != 0)
				{
					ans++;
					s--;
				}
			}
			else if (a[i] % 3 == 1)
			{
				if (a[i] / 3 + 1 >= p) ans++;
			}
			else
			{
				if (a[i] / 3 + 1 >= p)
					ans++;
				else if (a[i] / 3 + 2 >= p && s > 0)
				{
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
