#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end()
typedef long long LL;

int p,T;
vector<LL> m;
vector< vector<LL> > dp;
vector< LL > cost;

LL DP(int pos, int k)
{
	if (pos >= m.size()/2)
		return 0;
	if (dp[pos][k] != -1)
		return dp[pos][k];
	LL res = 0;
	if (m[pos] > k)
		res = max(res,DP(pos*2,k+1)+DP(pos*2+1,k+1)+cost[pos]);
	res = max(res,DP(pos*2,k)+DP(pos*2+1,k));
	dp[pos][k] = res;
	return dp[pos][k];
}
LL solve()
{
	LL GS=0;
	scanf("%d",&p);
	m.clear();
	cost.clear();
	dp.clear();
	dp.resize((1<<p)+10,vector<LL>(15,-1));
	cost.resize((1<<p)+1);
	for (int i=0;i<(1<<p);i++)
	{
		LL t;
		scanf("%lld",&t);
		m.push_back(t);
	}
	reverse(m.begin(),m.end());
	m.resize(m.size()*2);
	for (int i=0;i<m.size()/2;i++)
	{
		m[i+m.size()/2]=m[i];
	}
	for (int i=m.size()/2-1;i;i--)
	{
		m[i] = min(m[i*2],m[i*2+1]);
	}
	for (int i=(1<<p)-1;i>0;i--)
	{
		scanf("%lld",&cost[i]);
		GS+=cost[i];
	}
	return GS-DP(1,0);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		printf("Case #%d: %lld\n",i+1,solve());
	}
	return 0;
}