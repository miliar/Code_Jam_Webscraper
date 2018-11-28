#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

inline int max(int x,int y)
{
	return x > y ? x : y;
}
int a[1200];
int main(void)
{
	int t, p, m, test = 0, i, j, k, s, ans;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d", &p);
		m = 1 << p;
		for(i = 0;i < m;i ++)
		{
			scanf("%d", &a[i]);
			a[i] = p - a[i];
			if(a[i] < 0)
				a[i] = 0;
		}
		for(i = 0;i < p;i ++)
		{
			k = 1 << (p - 1 - i);
			for(j = 0;j < k;j ++)
				scanf("%d", &s);
		}
		ans = 0;
		for(i = 0;i < p;i ++)
		{
			k = 1 << (p - 1 - i);
			for(j = 0;j < k;j ++)
			{
				s = max(a[j * 2], a[j * 2 + 1]);
				if(s >= p - i)
				{
					ans ++;
					a[j] = s - 1;
				}
				else
					a[j] = s;
			}
		}
		printf("Case #%d: %d\n", ++ test, ans);
	}


	return 0;
}
