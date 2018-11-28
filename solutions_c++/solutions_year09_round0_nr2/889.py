#include <iostream>
#include <vector>
#include <string>
using namespace std;

int H, W;
int map[105][105];
bool was[105][105];
char ret[105][105];
char tl;

int getmin(int x, int y)
{
	int tec = map[x][y], ret = -1;
	if (x != 0 && map[x-1][y] < tec)
	{
		ret = 0;
		tec = map[x-1][y];
	}
	if (y != 0 && map[x][y-1] < tec)
	{
		ret = 1;
		tec = map[x][y-1];
	}
	if (y != W-1 && map[x][y+1] < tec)
	{
		ret = 3;
		tec = map[x][y+1];
	}
	if (x != H-1 && map[x+1][y] < tec)
	{
		ret = 2;
		tec = map[x+1][y];
	}

	return ret;
}

char DFS(int x, int y)
{
	if (was[x][y])
		return ret[x][y];
	int dir = getmin(x,y);
	if (dir == -1)
	{
		ret[x][y] = tl++;
		was[x][y] = 1;
		return ret[x][y];
	}
	else
		was[x][y] = 1; 
	if (dir == 0)
		ret[x][y] = DFS(x-1,y);
	else if (dir == 1)
		ret[x][y] = DFS(x,y-1);
	else if (dir == 2)
		ret[x][y] = DFS(x+1,y);
	else
		ret[x][y] = DFS(x,y+1);
	return ret[x][y];
}

void solve()
{
	for (int i=0; i<H; i++)
		for (int j=0; j<W; j++)
			if (!was[i][j])
			{
				ret[i][j] = DFS(i,j);
				was[i][j] = 1;
			}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int N;
	cin >> N;
	for (int I=0; I<N; I++)
	{
		memset(map,0,sizeof(map));
		memset(was,0,sizeof(was));
		memset(ret,0,sizeof(ret));
		tl = 'a';
		cin >> H >> W;
		for (int i=0; i<H; i++)
			for (int j=0; j<W; j++)
				cin >> map[i][j];
		solve();
		cout << "Case #" << I+1 << ":" << endl;
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<W; j++)
			{
				if (j != 0)
					cout << " ";
				cout << ret[i][j];
			}
			cout << endl;
		}
	}
}