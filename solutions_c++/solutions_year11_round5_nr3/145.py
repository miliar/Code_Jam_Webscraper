#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
const int mod=1000003;
	int n,m;
pair<int,int> dfs(vector<string> &q,int y,int x)
{
	int ty=y,tx=x;
	if(q[y][x]&1) tx--;
	if(q[y][x]&2) tx++;
	if(q[y][x]&4) ty--;
	if(q[y][x]&8) ty++;
	if(tx<0) tx=m-1;
	if(tx>=m) tx=0;
	if(ty<0) ty=n-1;
	if(ty>=n) ty=0;
	q[y][x]=0;
	if(q[ty][tx]==0) return make_pair(ty,tx);
	return dfs(q,ty,tx);
}
bool check(vector<string> &q)
{
	for(int y=0;y<n;y++)
		for(int x=0;x<m;x++)
		{
			if(q[y][x]==0) continue;
			pair<int,int> ret=dfs(q,y,x);
			if(ret.first!=y||ret.second!=x) return false;
		}
	return true;
}
int solve()
{
	scanf("%d%d",&n,&m);
	vector<string> p;
	vector<string> q;
	for(int i=0;i<n;i++)
	{
		char str[1024];
		scanf("%s",str);
		p.push_back(string(str));
		q.push_back(string(str));
	}
	int ans=0;
	for(int i=0;i<(1<<n*m);i++)
	{
		for(int j=0;j<n*m;j++)
		{
			int x=j%m,y=j/m;
			if(i&(1<<j))
			{
				switch(p[y][x])
				{
					case '-':
					q[y][x]=1;
					break;
					case '|':
					q[y][x]=4;
					break;
					case '/':
					q[y][x]=2+4;
					break;
					case '\\':
					q[y][x]=2+8;
					break;
				}
			}
			else
			{
				switch(p[y][x])
				{
					case '-':
					q[y][x]=2;
					break;
					case '|':
					q[y][x]=8;
					break;
					case '/':
					q[y][x]=1+8;
					break;
					case '\\':
					q[y][x]=1+4;
					break;
				}
			}
		}
		if(check(q)) ans++;
	}
	return ans%mod;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		printf("Case #%d: %d\n",cs,solve());
	}
	return 0;
}
