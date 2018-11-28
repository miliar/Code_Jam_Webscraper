#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int n, k, Test;
int vis[110], match[110];
int price[110][110];
int map[110][110];

int find(int x)
{
	for (int i = 0; i < n; ++i)
	{
		if (map[x][i] && !vis[i])
		{
			vis[i] = 1;
			if (match[i] == -1 || find(match[i]))
			{
				match[i] = x;
				return 1;
			}
		}
	}
	return 0;
}

int cmp(int a, int b)
{
	for (int i = 0; i < k; ++i)
	{
		if (price[a][i] >= price[b][i])
			return false;
	}
	return true;
}

void work()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < k; ++j)
			scanf("%d", &price[i][j]);
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
			map[i][j] = cmp(i, j);
	}
	
	memset(match, -1, sizeof(match));
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		memset(vis, 0, sizeof(vis));
		ans += find(i);
	}
	
	printf("Case #%d: %d\n", ++Test, n - ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
