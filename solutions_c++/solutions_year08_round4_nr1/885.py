#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int>    VI;
typedef vector<string> VS;
typedef pair<int ,int> PAR;


int INF = 10000000;

int N, V, T;

int ch[30000], ty[30000];
int le[30000];

int dp[30000][2];
void init()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	RE("%d",&T);
}
void pp(int num, int lv, int rv,int typ,int ad)
{
	if (typ)
	{
		int h = lv && rv;
		dp[num][h] = min(dp[num][h],dp[num*2][lv] + dp[num*2 + 1][rv] + ad);
	}
	else
	{
		int h = lv || rv;
		dp[num][h] = min(dp[num][h],dp[num*2][lv] + dp[num*2 + 1][rv] + ad);
	}
}
void dfs(int num)
{
	if (num>(N-1)/2) //leaf
	{
		dp[num][le[num]] = 0;
		dp[num][!le[num]] = INF;
		return ;
	}
	dfs(num*2);
	dfs((num*2) + 1);
	
	dp[num][0] = INF;
	dp[num][1] = INF;
	
	pp(num,1,0,ty[num],0);
	pp(num,0,1,ty[num],0);
	pp(num,1,1,ty[num],0);
	pp(num,0,0,ty[num],0);
	
	if (ch[num])
	{
		pp(num,1,0,!ty[num],1);
		pp(num,0,1,!ty[num],1);
		pp(num,1,1,!ty[num],1);
		pp(num,0,0,!ty[num],1);
	}
}
int main()
{
	init();
	int i, j, t;
	CLR(dp);
	FOR(t,1,T)
	{
		RE("%d%d",&N,&V);
		FOR(i,1,(N-1)/2) RE("%d %d",&ty[i],&ch[i]);
		FOR(i,1,(N+1)/2) RE("%d",&le[i + (N-1)/2]);
		dfs(1);
		WR("Case #%d: ",t);
		if (dp[1][V]!=INF) WR("%d\n",dp[1][V]);
		else WR("IMPOSSIBLE\n");
	}
	return 0;
}