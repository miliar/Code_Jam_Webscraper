#include<cstdio>
#define INF 0x7fffffff
int path[20],temp[20],t[100];
int ans,step;
struct
{
	int x,y;
} g[100][300];
int n,m,one;
int getone(int state)
{
	int one = 0;
	while (state)
	{
		state = state & (state - 1);
		++one;
	}
	return one;
}
bool check(int state)
{
	one = getone(state);
	for (int i = 0; i < n; ++i)
	{
		temp[i] = state & 1;
		state /= 2;
	}
	for (int i = 0; i < m; ++i)
	{
		bool ok = false;
		for (int j = 0; j < t[i]; ++j)
			if (temp[g[i][j].x] == g[i][j].y)
			{
				ok = true; break;
			}
		if (!ok) return false;
	}
	return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases,x,y;
	scanf("%d",&cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d",&n,&m);
		for (int i = 0; i < m; ++i)
		{
			scanf("%d",t + i);
			for (int j = 0; j < t[i]; ++j)
			{
				scanf("%d%d",&x,&y);
				--x;
				g[i][j].x = x;
				g[i][j].y = y;
			}
		}
		ans = INF;
		for (int state = 0; state < (1 << n); ++state)
			if (check(state))
				if (one < ans)
				{
					ans = one;
					for (int i = 0; i < n; ++i) path[i] = temp[i];
				}
		printf("Case #%d:",ca);
		if (ans == INF) puts(" IMPOSSIBLE"); 
		else { for (int i = 0; i < n ;++i) printf(" %d",path[i]); putchar('\n');}
	} 
}
