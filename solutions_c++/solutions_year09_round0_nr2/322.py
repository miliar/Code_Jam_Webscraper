#include <iostream>
#include <queue>
using namespace std;
#define ONLINEJUDGE
#define MAXN 110
#define NOTMARKED -1
#define NOTMARKED1 6
#define SINK 5

int map[MAXN][MAXN];
int Ret[MAXN][MAXN];
char La[MAXN * MAXN];
int L[MAXN][MAXN];
char hash[MAXN][MAXN];

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int H, W;
#define MAXALT 999999999

struct NodeType
{
	int x, y;
	int iVal;
}Buf1, Buf2;

queue<NodeType> Q;

bool sink(int x, int y)
{
	for(int i = 0; i < 4; i++)
	{
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if(nx < 0 || nx >= H || ny < 0 || ny >= W)
			continue;
		if(map[nx][ny] < map[x][y]) return false;
	}
	return true;
}

void Init()
{
	for(int i = 0; i < H; i++)
	{
		for(int j = 0; j < W; j++)
		{
			Ret[i][j] = NOTMARKED;
		}
	}
	for(int i = 0; i < MAXN * MAXN; i++)
		La[i] = NOTMARKED1;

	memset(hash, 0, sizeof(hash));
	while(!Q.empty())
	{
		Q.pop();
	}
}

void FindLabel(int x, int y)
{
	int iMinALT = MAXALT;
	char iT;
	for(int i = 0; i < 4; i++)
	{
		int nx = x + dir[i][0];
		int ny = y + dir[i][1];
		if(nx < 0 || nx >= H || ny < 0 || ny >= W)
			continue;

		if(iMinALT > map[nx][ny])
		{
			iT = i;
			iMinALT = map[nx][ny];
		}
	}
	if(iMinALT < map[x][y])
		Ret[x][y] = iT;
}

void Expand(NodeType Location)
{
	int i;
	int nx, ny;
	for(i = 0; i < 4; i++)
	{
		nx = Location.x + dir[i][0];
		ny = Location.y + dir[i][1];
		if(nx <0 || nx >= H || ny < 0 || ny >= W) 
			continue;
		if(hash[nx][ny]) continue;
		if(i == (3 - Ret[nx][ny]))
		{
			hash[nx][ny] = 1;
			Buf1.x = nx;
			Buf1.y = ny;
			Buf1.iVal = Location.iVal;
			L[nx][ny] = Location.iVal;
			Q.push(Buf1);
		}

	}

}
int main()
{
#ifdef ONLINEJUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif

	int iCaseTimes, inx, iny;
	int i, j, k;
	int iIndex;
	int iLabel;
	scanf("%d", &iCaseTimes);

	for(k = 0; k < iCaseTimes; k++)
	{
		scanf("%d%d", &H, &W);
		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
			{
				scanf("%d", &map[i][j]);
			}
		}
		Init();
		iLabel = 1;
		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
			{
				if(sink(i, j))
				{
					Buf1.x = i;
					Buf1.y = j;
					Buf1.iVal = iLabel;
					L[i][j] = iLabel++;
					Ret[i][j] = SINK;
					Q.push(Buf1);
				}
			}
		}

		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
			{
				if(Ret[i][j] == SINK) continue;
				else
				{
					FindLabel(i, j);
				}

			}
		}

		while(!Q.empty())
		{
			Buf2 = Q.front();
			Q.pop();
			Expand(Buf2);
	
		}

		char S = 'a';
		printf("Case #%d:\n", k + 1);
		for(i = 0; i < H; i++)
		{
			if(La[L[i][0]] == NOTMARKED1)
				La[L[i][0]] = S++;
			printf("%c", La[L[i][0]]);
			for(j = 1; j < W; j++)
			{
				if(La[L[i][j]] == NOTMARKED1)
					La[L[i][j]] = S++;
				printf(" %c", La[L[i][j]]);
			}
			printf("\n");
		}

	}
	return 0;
}