#include <cstdio>
#include <cstring>

using namespace std;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int T, H, W;
int height[100][100];
int anc[11000];
char lab[11000];

void init()
{
	scanf("%d%d", &H, &W);
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			scanf("%d", &height[i][j]);
}

int find(int u)
{
	if (anc[u] == -1) return u; else return anc[u] = find(anc[u]);
}

void uni(int u, int v)
{
	int i = find(u), j = find(v);
	if (i != j) anc[i] = j;
}

void work()
{
	memset(anc, 0xff, sizeof(anc));
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
		{
			int dir, minh = 100000;
			for (int k = 0; k < 4; k++)
			{
				if (i+dx[k] >= 0 && i+dx[k] < H && j+dy[k] >= 0 && j+dy[k] < W && minh > height[i+dx[k]][j+dy[k]])
				{
					minh = height[i+dx[k]][j+dy[k]];
					dir = k;
				}
			}
			if (minh < height[i][j])
				uni(i*W+j, (i+dx[dir])*W+j+dy[dir]);
		}
	char now = 'a';
	for (int i = 0; i < H*W; i++)
		lab[i] = '#';
	for (int i = 0; i < H*W; i++)
	{
		if (lab[find(i)] == '#')
		{
			lab[find(i)] = now;
			lab[i] = now;
			now++;
		}
		else
			lab[i] = lab[find(i)];
	}
	printf("Case #%d:\n", T);
	for (int i = 0; i < H; i++)
	{
		printf("%c", lab[i*W]);
		for (int j = 1; j < W; j++)
			printf(" %c", lab[i*W+j]);
		printf("\n");
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; T++)
	{
		init();
		work();
	}
}