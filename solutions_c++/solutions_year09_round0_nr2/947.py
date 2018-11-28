#include <cstdio>
#include <climits>
#include <cstring>

const int MAX_SIZE = 100 + 5;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int T, H, W;
int in[MAX_SIZE][MAX_SIZE];
char out[MAX_SIZE][MAX_SIZE];
char cnt;

char dfs(int x, int y)
{
	if(out[x][y])	return out[x][y];
	int mn = INT_MAX, d = -1;
	for(int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx >= 0 && nx < H && ny >= 0 && ny < W && in[nx][ny] < mn)
		{
			mn = in[nx][ny];
			d = i;
		}
	}
	if(mn < in[x][y])
		return out[x][y] = dfs(x + dx[d], y + dy[d]);
	else
	{
		out[x][y] = cnt;
		cnt ++;
		return cnt - 1;
	}
}

int main()
{
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		scanf("%d %d", &H, &W);
		for(int i = 0; i < H; i ++)
			for(int j = 0; j < W; j ++)
				scanf("%d", &in[i][j]);
		memset(out, 0, sizeof(out));
		cnt = 'a';
		for(int i = 0; i < H; i ++)
			for(int j = 0; j < W; j ++)
				if(out[i][j] == 0)
					dfs(i, j);
		printf("Case #%d:\n", t + 1);
		for(int i = 0; i < H; i ++)
		{
			for(int j = 0; j + 1 < W; j ++)
				printf("%c ", out[i][j]);
			printf("%c\n", out[i][W - 1]);
		}
	}
    return 0;
}
