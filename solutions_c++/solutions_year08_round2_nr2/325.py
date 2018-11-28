#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");

int n;
int a,b,p;
int prime[2000];
int g[2000][2000];
bool vis[2000];

void init()
{
	n=0;
	for (int i=2; i<2000; ++i)
	{
		bool ok = 1;
		for (int j=2; j<i; ++j)
		    if (i%j ==0)
		    {
				ok = 0;
				break;
			}
		if (ok)
		    prime[n++] = i;
	}
}

void dfs(int x)
{
	vis[x]=1;
	for (int i=a; i<=b; ++i)
	    if (g[x][i] && !vis[i])
	        dfs(i);
}

bool ok(int x, int y)
{
	for (int i=n-1; i>=0 && prime[i]>=p; --i)
	    if (x%prime[i]==0 && y%prime[i]==0)
	        return 1;
	return 0;
}

void solve()
{
	memset(g,0,sizeof(g));
	fin >> a >> b >> p;
	for (int i=a; i<b; ++i)
	    for (int j=i+1; j<=b; ++j)
			if (ok(i,j))
			{
				g[i][j] = 1;
				g[j][i] = 1;
			}
			
	memset(vis,0,sizeof(vis));
	int ans=0;
	for (int i=a; i<=b; ++i)
		if (!vis[i])
		{
			++ans;
			dfs(i);
		}
	fout << ans << endl;
}

int main()
{
	init();
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
