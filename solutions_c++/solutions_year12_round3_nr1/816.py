#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cassert>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d ",n)
#define outln(n) printf("%d\n",n)
#define outl(n) printf("%lld ",n)
#define outlln(n) printf("%lld\n",n)
#define LL long long 
#define pb push_back
#define f first
#define s second
using namespace std;
int n;
vector<int> g[1024];
int vis[1024];

int fl;
int ctr;
void dfs(int v)
{
	vis[v]=ctr;
	rep(i,0,g[v].size())
	{
		if(vis[g[v][i]]==ctr)
		{
			fl = 1;
			continue;
		}
		dfs(g[v][i]);
	}
}
int main()
{
	int kases;
	in(kases);
	for(int kase=1;kase<=kases;kase++)
	{
		fl=0;
		memset(vis,-1,sizeof(vis));
		printf("Case #%d: ",kase);
		in(n);
		rep(i,0,n)
		{
			g[i].clear();
			int t;
			in(t);
			rep(j,0,t)
			{
				int x;
				in(x);
				x--;
				g[i].pb(x);

			}
		}
		ctr=0;
		rep(i,0,n)
		{
			if(vis[i]==-1)
			{
				dfs(i);
				ctr++;
			}
		}
		puts(fl?"Yes":"No");

	}
	return 0;
}
