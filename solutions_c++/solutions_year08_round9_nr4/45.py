#include <iostream>
#include <set>

using namespace std;

int	now, task;

const int	maxN = 40;
const int	maxT = 1000;
const int	INF = 1 << 29;

int		idx[maxN][maxN];
int		dis[maxN][maxN];
char		g[maxN][maxN];

pair<int, int>	queue[maxT];

int		cost[maxT][maxT];
int		node[maxT];
int		used[maxT];
int		tow[maxT];
int		hash[maxT];

int		N, M, T; 
int		op, cl;

void	refresh(int x0, int y0, int x, int y)
{
	if (idx[x0][y0] >= 0 || g[x0][y0] == '.') return;
	idx[x0][y0] = idx[x][y];
	dis[x0][y0] = dis[x][y] + 1;
	queue[cl++] = make_pair(x0, y0);
}

void	work(int u, int v, int x, int y)
{
	if (idx[u][v] < 0 || idx[u][v] == idx[x][y]) return;
	int c = - dis[u][v] * (dis[u][v] + 1) / 2;
	c += (dis[x][y] + 1 + dis[x][y] + dis[u][v] + 1) * (dis[u][v] + 1) / 2;
	cost[idx[x][y]][idx[u][v]] = min(cost[idx[x][y]][idx[u][v]], c);
}

int	main()
{
	freopen("input.txt", "r", stdin);
	scanf("%d", &task);
	for (int now = 1; now <= task; ++now)
	{
		scanf("%d%d\n", &N, &M);
		for (int i = 0; i < N; ++i) gets(g[i]);

		memset(idx, 255, sizeof(idx));
		memset(dis, 255, sizeof(dis));

		T = 0;
		for (int i = 0; i < N; ++i) for (int j = 0; j < M; ++j) if (g[i][j] == 'T')
		{
			queue[T] = make_pair(i, j);
			dis[i][j] = 0;
			idx[i][j] = T++;
		}

		for (op = 0, cl = T; op < cl; )
		{
			int x = queue[op].first, y = queue[op].second;
			++op;

			if (x) refresh(x - 1, y, x, y);
			if (y) refresh(x, y - 1, x, y);
			if (x < N - 1) refresh(x + 1, y, x, y);
			if (y < M - 1) refresh(x, y + 1, x, y);
		}

		for (int i = 0; i < T; ++i) for (int j = 0; j < T; ++j) cost[i][j] = INF;
		for (int i = 0; i < N; ++i) for (int j = 0; j < M; ++j) if (idx[i][j] >= 0)
		{
			int x = i, y = j;
			if (x) work(x - 1, y, x, y);
			if (y) work(x, y - 1, x, y);
			if (x < N - 1) work(x + 1, y, x, y);
			if (y < M - 1) work(x, y + 1, x, y);
		}

		for (int i = 0; i < T; ++i) cost[i][0] = INF;
		
		int minC = 0;
		memset(used, 0, sizeof(used));
/*		for (int i = 0; i < T; ++i)
		{
			for (int j = 0; j < T; ++j)
				cout << cost[i][j] << ' ';
			cout << endl;
		}
		cout << T << endl;
*/
		memset(hash, 0, sizeof(hash));
		int nowTime = 1;
		for (int rest = T; rest > 1; )
		{
			memset(tow, 255, sizeof(tow));
			for (int i = 0; i < T; ++i) if (!used[i])
				for (int j = 0; j < T; ++j) if (i != j && !used[j])
					if (tow[i] < 0 || cost[i][j] < cost[i][tow[i]]) tow[i] = j;

//			for (int i = 0; i < T; ++i) cout << tow[i] << ' '; cout << endl;

			++nowTime;
			for (int i = 0; i < T; ++i) if (!used[i] && hash[i] != nowTime)
			{
				int k = 0, j = i;
				int nowCost = 0, maxEdge = 0;

				while (!used[j])
				{
					hash[j] = nowTime;
					used[j] = 1;
					node[k++] = j;
					nowCost += cost[j][tow[j]];
					j = tow[j];
				}

				int head;
				for (int p = 0; p < k; ++p) if (node[p] == j)
				{
					head = p;
					break;
				}

				for (int j = head; j < k; ++j)
					maxEdge = max(maxEdge, cost[node[j]][tow[node[j]]]);
//				printf("head : %d, maxE : %d, cost : %d\n", head, maxEdge, nowCost);

				int u = node[head];
				used[u] = 0;

				for (int j = head + 1; j < k; ++j) for (int p = 0; p < T; ++p) if (!used[p] && p != u)
					cost[u][p] = min(cost[u][p], cost[node[j]][p]);

				for (int j = 0; j < k; ++j) for (int p = 0; p < T; ++p) if (!used[p] && p != u)
					cost[p][u] = min(cost[p][u], cost[p][node[j]]);

				minC += nowCost - maxEdge;
				rest -= (k - 1);
			}
		}
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j) if (idx[i][j] >= 0)
				minC += dis[i][j];
		printf("Case #%d: %d\n", now, minC);
	}
	return 0;
}
