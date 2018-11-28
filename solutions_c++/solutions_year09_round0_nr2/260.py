#include <stdio.h>

#define SIZE_H	100
#define SIZE_W	100

int h, w, cnt;
int map[SIZE_H][SIZE_W];
int dir[SIZE_H][SIZE_W];
char ans[SIZE_H][SIZE_W];

const int dy[4] = {1, 0, 0, -1};
const int dx[4] = {0, 1, -1, 0};

void init()
{
	int i, j, k;
	int ni, nj, low;

	for(i = 0; i < h; i++)
		for(j = 0; j < w; j++)
			ans[i][j] = 0;
	for(i = 0; i < h; i++)
		for(j = 0; j < w; j++)
		{
			low = 999999;
			for(k = 3; k >= 0; k--)
			{
				ni = i + dy[k];
				nj = j + dx[k];
				if(!(0 <= ni && ni < h && 0 <= nj && nj < w)) continue;
				if(map[i][j] > map[ni][nj] && map[ni][nj] < low) low = map[ni][nj];
			}
			for(k = 3; k >= 0; k--)
			{
				ni = i + dy[k];
				nj = j + dx[k];
				if(!(0 <= ni && ni < h && 0 <= nj && nj < w)) continue;
				if(map[ni][nj] == low)
				{
					dir[i][j] = k;
					break;
				}
			}
			if(k < 0) dir[i][j] = k;
		}
}

void BFS(int i, int j)
{
	int k, ni, nj;
	int front, rear;
	int queue[SIZE_H*SIZE_W+100][2];

	ans[i][j] = 'a' + cnt;
	rear = 1;
	front = 0;
	queue[0][0] = i;
	queue[0][1] = j;
	while(front < rear)
	{
		i = queue[front][0];
		j = queue[front][1];
		front++;

		if(dir[i][j] >= 0) // there is a flow from this cell
		{
			ni = i + dy[dir[i][j]];
			nj = j + dx[dir[i][j]];
			if(ans[ni][nj] <= 0)
			{
				ans[ni][nj] = 'a' + cnt;
				queue[rear][0] = ni;
				queue[rear][1] = nj;
				rear++;
			}
		}

		for(k = 0; k < 4; k++)	// investigate the adjacent cells come into this cell
		{
			ni = i + dy[k];
			nj = j + dx[k];
			if(!(0 <= ni && ni < h && 0 <= nj && nj < w)) continue;
			if(ans[ni][nj] > 0 || dir[ni][nj] < 0) continue;
			if(k + dir[ni][nj] == 3)
			{
				ans[ni][nj] = 'a' + cnt;
				queue[rear][0] = ni;
				queue[rear][1] = nj;
				rear++;
			}
		}
	}
}

void process()
{
	int i, j;

	init();
	cnt = 0;
	for(i = 0; i < h; i++)
		for(j = 0; j < w; j++)
		{
			if(ans[i][j] == 0)
			{
				BFS(i, j);
				cnt++;
			}
		}
}

int main()
{
	int t, z, i, j;

	scanf("%d", &t);
	z = 1;
	while(t > 0)
	{
		scanf("%d %d", &h, &w);
		for(i = 0; i < h; i++)
			for(j = 0; j < w; j++)
				scanf("%d", &map[i][j]);
		process();
		printf("Case #%d:\n", z++);
		for(i = 0; i < h; i++)
		{
			for(j = 0; j < w-1; j++)
				printf("%c ", ans[i][j]);
			printf("%c\n", ans[i][j]);
		}
		t--;
	}

	return 0;
}
