#include <iostream>

using namespace std;

int H,W;
char ch = 'a';
int Map[110][110];
char ans[110][110];
bool visit[110][110];
int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};
bool next(int x,int y,int &nx,int &ny)
{
	int tx,ty;
	int Min = Map[x][y];
	for(int i = 0; i< 4; ++i)
	{
		tx = x+dx[i];
		ty = y+dy[i];
		if(tx <= 0 || ty <= 0 || tx > H || ty > W) continue;
		if(visit[tx][ty] == false && Map[tx][ty] < Min)
		{
			Min = Map[tx][ty];
			nx = tx;
			ny = ty;
		}
	}
	if(Min == Map[x][y]) return false;
	else return true;
}
bool next2(int x,int y,int &nx,int &ny)
{
	int tx,ty;
	int Min = Map[x][y];
	for(int i = 0; i< 4; ++i)
	{
		tx = x+dx[i];
		ty = y+dy[i];
		if(tx <= 0 || ty <= 0 || tx > H || ty > W) continue;
		if( Map[tx][ty] < Min)
		{
			Min = Map[tx][ty];
			nx = tx;
			ny = ty;
		}
	}
	if(Min == Map[x][y]) return false;
	else return true;
}
void Dfs(int x,int y)
{
	//printf("-----  %d %d\n",x,y);
	ans[x][y] = ch;
	visit[x][y] = true;
	for(int i = 0; i< 4; ++i)
	{
		int tx = x + dx[i];
		int ty = y + dy[i];
		if(tx <= 0 || ty <= 0 || tx > H || ty > W) continue;
		if(visit[tx][ty] == false)
		{
			int nx =-1,ny=-1;
			if(next2(tx,ty,nx,ny) == true && ans[nx][ny] == ch && (nx == x && ny == y))
			{
				Dfs(tx,ty);
			}
		}
	}
}
void GetToLowest(int &x,int &y)
{
	int nx = -1;
	int ny = -1;
	while(next(x,y,nx,ny))
	{
		/*visit[x][y] = true;
		ans[x][y] = ch;*/
		x = nx;
		y = ny;
	}
}
void Print()
{
	for(int i = 1; i<= H; ++i)
	{
		for(int j = 1; j<= W; ++j)
		{
			printf("%c ",ans[i][j]);
		}
		printf("\n");
	}
}
void solve(int x,int y)
{
	GetToLowest(x,y);
	Dfs(x,y);
	//Print();
}
int main()
{
	int T;
	cin >> T;
	int TT = 1;
	while(T--)
	{
		cin >> H >> W;
		for(int i = 0; i< 110; ++i)
			for(int j = 0; j< 110; ++j) Map[i][j] = 1111111;
		memset(visit,0,sizeof(visit));
		for(int i = 1; i<= H; ++i)
		{
			for(int j = 1; j<= W; ++j)
			{
				scanf("%d",&Map[i][j]);
			}
		}
		ch = 'a'-1;
		for(int i = 1; i<= H; ++i)
		{
			for(int j = 1; j<= W; ++j)
			{
				if(visit[i][j]) continue;
				//visit[i][j] = true;
				//printf("(%d %d)\n",i,j);
				ch++;
				ans[i][j] = ch;
				solve(i,j);
				
			}
		}
		
		printf("Case #%d:\n",TT++);
		Print();
	}
	return 0;
}