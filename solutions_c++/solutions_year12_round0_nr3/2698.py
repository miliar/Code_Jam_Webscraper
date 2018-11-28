#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>

using namespace std;

int t, a, b, i, tc, k, c ,ans, m;
map<pair<int,int>, int > vis;

int main()
{
	freopen("recycled.in","r",stdin); freopen("recycled.out", "w", stdout);
	scanf("%d", &t);
	for (tc = 1; tc <= t; tc++)
	{
		k = 1; ans = 0; vis.clear();
		scanf("%d %d", &a, &b);
		c = a;
		while (c/10 > 0) 
		{
			k *= 10;
			c /= 10;
		}
		for (i = a; i <= b; i++)
		{
			m = i; c = i;
			while (c/10 > 0)
			{
				m = m/10 + (m%10)*k;
				c /= 10;
				if ( m > i && m <= b && !vis[make_pair(i,m)]) 
				{
					vis[make_pair(i,m)] = 1;
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
}