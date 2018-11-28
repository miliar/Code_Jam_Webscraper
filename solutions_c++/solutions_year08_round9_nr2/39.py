#include <cstdio>
#include <cstring>

int test;
int vis[200][200], q[50000];
void work()
{
	int r, c, dx[2], dy[2], sx, sy;
	scanf("%d%d", &r, &c);
	for (int i = 0; i < 2; ++i)
		scanf("%d%d", &dx[i], &dy[i]);
	scanf("%d%d", &sx, &sy);
	memset(vis, 0, sizeof(vis));
	vis[sx][sy] = 1;
	q[0] = sx << 16 | sy;
	int head = 0, tail = 0;
	while (head <= tail)
	{
		int cx = q[head] >> 16, cy = q[head] & 0xFFFF;
		++head;
		for (int d = 0; d < 2; ++d)
		{
			int nx = cx + dx[d], ny = cy + dy[d];
			if (nx < 0 || ny < 0 || nx >= r || ny >= c)
				continue;
			if (vis[nx][ny])
				continue;
			vis[nx][ny] = 1;
			q[++tail] = nx << 16 | ny;
		}
	}
	printf("Case #%d: %d\n", ++test, head);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
