#include <cstdio>
#include <cstring>

int test;

int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
int from[50][50], vis[50][50], step[50][50], q[50*50];
char map[50][50];
void work()
{
	int n, m, tx = -1, ty, ans = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
	{
		scanf("%s", map[i]);
		for (int j = 0; j < m; ++j)
		{
			if (map[i][j] == 'T' && i + j > 0)
			{
				tx = i; ty = j;
			}
		}
	}
	memset(vis, 0, sizeof(vis));
	if (tx != -1)
	{
		q[0] = 0;
		int head = 0, tail = 0;
		memset(from, -1, sizeof(from));
		from[0][0] = 0;
		step[0][0] = 0;
		int ok = 0;
		while (head <= tail && !ok)
		{
			int cx = q[head] >> 16, cy = q[head] & 0xFFFF;
			++head;
			for (int d = 0; d < 4; ++d)
			{
				int nx = cx + dx[d], ny = cy + dy[d];
				if (nx < 0 || ny < 0 || nx >= n || ny >= m)
					continue;
				if (from[nx][ny] != -1 || map[nx][ny] == '.')
					continue;
				from[nx][ny] = cx << 16 | cy;
				step[nx][ny] = step[cx][cy] + 1;
				q[++tail] = nx << 16 | ny;
				if (map[nx][ny] == 'T')
					ok = 1;
			}
		}
		ans = step[tx][ty];
		ans = ans * (ans + 1) / 2;
		int cx = tx, cy = ty;
		while (cx + cy)
		{
			vis[cx][cy] = 1;
			int t = from[cx][cy];
			cx = t >> 16, cy = t & 0xFFFF;
		}
	}
	q[0] = 0;
	int head = 0, tail = 0;
	if (tx != -1)
		q[++tail] = tx << 16 | ty;
	memset(step, -1, sizeof(step));
	step[0][0] = 0;
	if (tx != -1)
		step[tx][ty] = 0;
	while (head <= tail)
	{
		int cx = q[head] >> 16, cy = q[head] & 0xFFFF;
		++head;
		if (!vis[cx][cy])
			ans += step[cx][cy];
		for (int d = 0; d < 4; ++d)
		{
			int nx = cx + dx[d], ny = cy + dy[d];
			if (nx < 0 || ny < 0 || nx >= n || ny >= m)
				continue;
			if (step[nx][ny] != -1 || map[nx][ny] == '.')
				continue;
			step[nx][ny] = step[cx][cy] + 1;
			q[++tail] = nx << 16 | ny;
		}
	}
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
