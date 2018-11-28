#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
using namespace std;

int		n, m;
vector<int>		list	[500];

void init()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i <= n; i ++)
		list[i].clear();
	int a, b;
	for (int i = 0; i < m; i ++)
	{
		scanf("%d,%d", &a, &b);
		list[a].push_back(b);
		list[b].push_back(a);
	}
}

int		queue	[500];
int		head, tail;
int		dist	[500];

int		dp	[500][500];

int		cnt		[500];
int		node	[500][500];

int nodeAdd(int x, int a, int b)
{
	set<int> done;
	done.insert(a);
	done.insert(b);
	for (int i = 0; i < list[a].size(); i ++)
		done.insert(list[a][i]);
	for (int i = 0; i < list[b].size(); i ++)
		done.insert(list[b][i]);
	int v = 0;
	for (int i = 0; i < list[x].size(); i ++)
		if (! done.count(list[x][i]))
			v ++;
	return v;
}

void solve()
{
	memset(dist, 0xff, sizeof(dist));
	queue[ head = tail = 0 ] = 0;
	dist[0] = 0;

	memset(cnt, 0, sizeof(cnt));
	node[ 0 ][ 0 ] = 0;
	cnt[0] = 1;

	while (head <= tail)
	{
		int u = queue[head ++];
		for (int i = 0; i < list[u].size(); i ++)
		{
			int v = list[u][i];
			if (dist[v] < 0)
			{
				dist[v] = dist[u] + 1;
				queue[ ++ tail ] = v;
				node[ dist[v] ][ cnt[ dist[v] ] ++ ] = v;
			}
		}
	}

	if (dist[1] == 1)
	{
		printf("%d %d\n", 0, list[0].size());
		return;
	}

	int	L = dist[1];
	int ans = -1;

	memset(dp, 0xff, sizeof(dp));
	for (int i = 0; i < cnt[1]; i ++)
		dp[ 0 ][ node[1][i] ] = list[0].size() + nodeAdd(node[1][i], 0, n) - 1;

	for (int k = 1; k < L; k ++)
	{
		int a, b;
		for (int i = 0; i < cnt[k-1]; i ++)
		{
			a = node[k-1][i];
			for (int j = 0; j < cnt[k]; j ++)
			{
				b = node[k][j];
				if (dp[a][b] < 0) continue;

				if (k == L - 1)
				{
					bool yes = 0;
					for (int p = 0; p < list[b].size(); p ++)
						if (list[b][p] == 1) yes = 1;
					if (yes && dp[a][b] > ans) ans = dp[a][b];
				}
				else
				{
					for (int p = 0; p < list[b].size(); p ++)
					{
						int c = list[b][p];
						if (dist[c] == k + 1)
						{
							int tmp = dp[a][b] - 1 + nodeAdd(c, a, b);
							if (tmp > dp[b][c]) dp[b][c] = tmp;
						}
					}
				}
			}
		}
	}

	printf("%d %d\n", L - 1, ans);
}

int main()
{
//	freopen("D-small-attempt0.in", "r", stdin);
//	freopen("D-small.out", "w", stdout);

	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

//	freopen("in.txt", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t ++)
	{
		fprintf(stderr, "%d\n", t);
		init();
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
