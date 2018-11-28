#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<cstring>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;

int d[110][110];
int n, m;
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int vis[110][110];
int cnt = 0;
int foo(int x, int y)
{
	if(vis[x][y] != -1)
	{
		return vis[x][y];
	}
	int i, j, k;
	int mval = d[x][y];
	for(i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;
		mval = min(mval, d[nx][ny]);
	}
	if(mval == d[x][y])
	{
		cnt++;
		vis[x][y] = cnt;
		return cnt;
	}
	for(i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;
		if(d[nx][ny] == mval)
		{
			vis[x][y] = foo(nx, ny);
			return vis[x][y];
		}
	}
	return -1;
}
void solve()
{
	CLRM(vis);
	cnt = 0;
	int i, j, k;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < m; j++)
		{
			if(vis[i][j] != -1)
				continue;
			vis[i][j] = foo(i, j);
		}
	}
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < m; j++)
		{
			assert(vis[i][j] > 0 && vis[i][j] <= 26);
			printf("%c ",(char)(vis[i][j] - 1 + 'a'));
		}
		printf("\n");
	}
}
int main()
{
	int tes;
	scanf("%d", &tes);
	int tot = 0;
	while(tes--)
	{
		tot++;
		scanf("%d%d", &n, &m);
		int i, j, k;
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m; j++)
			{
				scanf("%d", &k);
				d[i][j] = k;
			}
		}
		printf("Case #%d:\n", tot);
		solve();
	}
	return 0;
}
