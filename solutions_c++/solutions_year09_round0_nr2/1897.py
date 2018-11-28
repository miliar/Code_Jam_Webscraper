#include <cstdio>
#include <memory.h>
#include <vector>
#include <queue>
using namespace std;

int T, H, W;

int HeightMap[110][110];
int BasinMap[110][110];
int DirMap[110][110];

int GetDirection(int x, int y)
{
	int MinHeight = 1000000;
	int CurHeight = HeightMap[x][y];
	int CurDir = 0;
	if(y > 0)
	{
		if(HeightMap[x][y-1] < MinHeight &&
			HeightMap[x][y-1] < CurHeight)
		{
			CurDir = 1;
			MinHeight = HeightMap[x][y-1];
		}
	}
	if(x > 0)
	{
		if(HeightMap[x-1][y] < MinHeight &&
			HeightMap[x-1][y] < CurHeight)
		{
			CurDir = 2;
			MinHeight = HeightMap[x-1][y];
		}
	}
	if(x < W-1)
	{
		if(HeightMap[x+1][y] < MinHeight &&
			HeightMap[x+1][y] < CurHeight)
		{
			CurDir = 3;
			MinHeight = HeightMap[x+1][y];
		}
	}
	if(y < H-1)
	{
		if(HeightMap[x][y+1] < MinHeight &&
			HeightMap[x][y+1] < CurHeight)
		{
			CurDir = 4;
			MinHeight = HeightMap[x][y+1];
		}
	}
	return CurDir;
}

int main(void)
{
	//freopen("TaskB.in", "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("TaskB.out", "wt", stdout);
	scanf("%d", &T);
	for(int Test = 0; Test < T; Test++)
	{
		memset(BasinMap, 0, sizeof(BasinMap));

		scanf("%d %d", &H, &W);
		for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				scanf("%d", &HeightMap[x][y]);
			}
		}


		for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				DirMap[x][y] = GetDirection(x,y);
			}
		}

		int CurBasin = 0;

		for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				if(DirMap[x][y] == 0)
				{
					CurBasin ++;
					queue<pair<int, int>> wave;
					wave.push(make_pair(x, y));
					while(!wave.empty())
					{
						pair<int, int> CurCoord = wave.front();
						int X, Y;
						X = CurCoord.first;
						Y = CurCoord.second;
						BasinMap[X][Y] = CurBasin;
						wave.pop();
						if(X > 0   && DirMap[X-1][Y] == 3)	wave.push(make_pair(X-1, Y));
						if(X < W-1 && DirMap[X+1][Y] == 2)	wave.push(make_pair(X+1, Y));
						if(Y > 0   && DirMap[X][Y-1] == 4)	wave.push(make_pair(X, Y-1));
						if(Y < H-1 && DirMap[X][Y+1] == 1)	wave.push(make_pair(X, Y+1));
					}
				}
			}
		}
		printf("Case #%d:\n", Test+1);
		vector<char> Mapping(30, ' ');
		char CurrentLetter = 'a';
		/*for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				
				printf("%d\t", DirMap[x][y]);
			}
			printf("\n");
		}*/
		for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				if(Mapping[BasinMap[x][y]] == ' ')
				{
					Mapping[BasinMap[x][y]] = CurrentLetter ++;
					if(CurrentLetter > 'c')
					{
						int a = 0;
					}
				}
				printf("%c ", Mapping[BasinMap[x][y]]);
			}
			printf("\n");
		}
	}
	
	return 0;
}