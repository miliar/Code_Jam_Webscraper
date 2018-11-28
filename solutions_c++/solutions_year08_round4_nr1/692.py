#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

const int maxn = 20000;
const int inf = 20000;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int m,v;
int gate[maxn];
int f[maxn][2];
int value[maxn];
int can[maxn];
bool vis[maxn][2];

void update(int &x, int y)
{
	if (y>=inf) y=inf;
	if (y<x) x=y;
}

inline bool leaf(int a)
{
	return a > (m-1)/2;
}

int dp(int a, int x)
{
	if (vis[a][x]) return f[a][x];
	if (leaf(a)) return x==value[a] ? 0 : inf;
	
	f[a][x]=inf;
	vis[a][x]=1;
	if (x==1 && gate[a]==1)
	{
		update(f[a][x], dp(a*2,1)+dp(a*2+1,1));
		if (can[a])
		{
			update(f[a][x], dp(a*2,0)+dp(a*2+1,1)+1);
			update(f[a][x], dp(a*2,1)+dp(a*2+1,0)+1);
			update(f[a][x], dp(a*2,1)+dp(a*2+1,1)+1);
		}
	}
	else if (x==1 && gate[a]==0)
	{
  		update(f[a][x], dp(a*2,1)+dp(a*2+1,1));
		update(f[a][x], dp(a*2,0)+dp(a*2+1,1));
		update(f[a][x], dp(a*2,1)+dp(a*2+1,0));
 		if (can[a])
			update(f[a][x], dp(a*2,1)+dp(a*2+1,1)+1);
	}
	else if (x==0 && gate[a]==1)
	{
		update(f[a][x], dp(a*2,1)+dp(a*2+1,0));
		update(f[a][x], dp(a*2,0)+dp(a*2+1,1));
		update(f[a][x], dp(a*2,0)+dp(a*2+1,0));
		if (can[a])
			update(f[a][x], dp(a*2,0)+dp(a*2+1,0)+1);
	}
	else if (x==0 && gate[a]==0)
	{
        update(f[a][x], dp(a*2,0)+dp(a*2+1,0));
		if (can[a])
		{
	        update(f[a][x], dp(a*2,0)+dp(a*2+1,1)+1);
	        update(f[a][x], dp(a*2,1)+dp(a*2+1,0)+1);
	        update(f[a][x], dp(a*2,0)+dp(a*2+1,0)+1);
		}
	}
	return f[a][x];
}

void solve()
{
	fin >> m >> v;
	for (int i=1; i<=(m-1)/2; ++i)
		fin >> gate[i] >> can[i];
	for (int i=(m-1)/2+1; i<=m; ++i)
		fin >> value[i];
	
	memset(vis, 0, sizeof(vis));
	if (dp(1,v) == inf)
	    fout << "IMPOSSIBLE" << endl;
	else
	    fout << dp(1,v) << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
