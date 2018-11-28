#include <cstdio>
#include <cmath>
#include <vector>

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int t, h, w;
int arr[5000][5000];
std::vector<int> adjList[20000];


void scan()
{
	scanf("%d%d", &h, &w);
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			scanf("%d", &arr[i][j]);
}

int code(int x, int y)
{
	return x*w + y;
}

void decode(int code, int &x, int &y)
{
	x = code / w;
	y = code % w;
}

int move[4][2];
int queue[20000];
bool mark[20000];
char answer[5000][5000];

void init()
{
	move[0][0] = -1;	move[0][1] =  0;
	move[1][0] =  0;	move[1][1] = -1;
	move[2][0] =  0;	move[2][1] = +1;
	move[3][0] = +1;	move[3][1] =  0;
	for (int i = 0; i < 20000; i++)
		adjList[i].clear();
	memset(mark, false, sizeof(mark));
}

void color(int u, char c)
{
	int x, y;
	decode(u, x, y);
	answer[x][y] = c;
}

void bfs(int v, char color)
{
	int l = 0, r = 0;

	::color(v, color);
	mark[v] = true;
	queue[0] = v;

	while (l <= r)
	{
		v = queue[l++];
		for (int i = 0; i < adjList[v].size(); i++)
		{
			int u = adjList[v][i];
			if (!mark[u])
			{
				mark[u] = true;
				queue[++r] = u;
				::color(u, color);
			}
		}
	}
}

void solve()
{
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			int minH = arr[i][j];
			int X = -1, Y = -1;
			for (int k = 0; k < 4; k++)
			{
				int x = i + move[k][0];
				int y = j + move[k][1];
				if (x >= 0 && x < h && y >= 0 && y < w)
					if (minH > arr[x][y])
					{
						minH = arr[x][y];
						X = x;
						Y = y;
					}
			}

			if (!(X == -1 && Y == -1))
			{
				int a = code(i, j);
				int b = code(X, Y);
				adjList[a].push_back(b);
				adjList[b].push_back(a);
			}
		}

	int curColor = 'a';
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			int v = code(i, j);
			if (!mark[v])
			{
				bfs(v, curColor);
				curColor++;
			}
		}
}

void print(int t)
{
	printf("Case #%d:\n", t);
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
			printf("%c ", answer[i][j]);
		printf("\n");
	}
}

int main()
{
	OpenFiles();
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		init();
		scan();
		solve();
		print(i+1);
	}
	

	return 0;
}