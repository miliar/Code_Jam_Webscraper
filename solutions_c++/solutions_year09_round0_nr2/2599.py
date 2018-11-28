#include <iostream>
using namespace std;

const int maxh = 100, maxw = 100;
const int dx[4] = {-1,0,0,1}, dy[4] = {0,-1,1,0};
int t,h,w;
int map[maxh][maxw];
int ans[maxh][maxw];

bool inrange(int x, int y, int i)
{
	if (x + dx[i] >=0 && x + dx[i] < h && y +dy[i] >= 0 && y+dy[i] < w)
		return true;
	else return false;
}

void dfs(int x, int y,int& now,int& aans)
{
	int sink = -1,lowest = map[x][y];
	for (int i = 0; i < 4; ++i)
	{
		if (inrange(x,y,i))
		{
			if (map[x+dx[i]][y+dy[i]] < lowest)
			{
				sink = i;
				lowest = map[x+dx[i]][y+dy[i]];
			}
		}
	}
	if (sink == -1)
	{
		++now;
		ans[x][y] = now;
		aans = now;
	}
	else if (ans[x+dx[sink]][y+dy[sink]] == -1)
	{
		dfs(x+dx[sink],y+dy[sink],now,aans);
		ans[x][y] = aans;
	}
	else
	{
		ans[x][y] = ans[x+dx[sink]][y+dy[sink]];
		aans = ans[x][y];
	}
}

void solve()
{
	int now = -1,aans = -1;
	for (int i = 0; i < h; ++i)
	for (int j = 0; j < w; ++j)
		if (ans[i][j] == -1)
		{
			dfs(i,j,now,aans);
		}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	
	cin >> t;
	for (int tt = 0; tt < t; ++tt)
	{
		cin >> h >> w;
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				cin >> map[i][j];
				ans[i][j] = -1;
			}
		}
		solve();
		printf("Case #%.d:\n",tt+1);
		for (int i = 0; i < h; ++i)
		{
			printf("%.c",ans[i][0]+'a');
			for (int j = 1; j < w; ++j)
			{
				printf(" %.c",ans[i][j]+'a');
			}
			printf("\n");
		}
	}
	
	return 0;
}
