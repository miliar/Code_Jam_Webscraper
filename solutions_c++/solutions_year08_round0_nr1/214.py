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


#define INF 1000000
using namespace std;
typedef vector<int> VI;
typedef vector<string>VS;

int T;
int S;
int Q;

char w[105][200];

int dp[1050][150];
int m[2000];
void init()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	RE("%d",&T);
}
bool eq(char * a, char * b)
{
	int i = 0;
	while (1)
	{
		if (a[i]!=b[i]) return false;
		if (a[i]==0) break;
		i++;
	}
	return true;
}
int main()
{
	init();
	int t, i, j, k;
	char s[10000];
	FOR(t,1,T)
	{
		RE("%d",&S);
		char ch = getchar();
		FOR(j,1,S) gets(w[j]);
		
		RE("%d",&Q);
		ch = getchar();
		FOR(j,1,Q)
		{
			gets(s);
			m[j] = 0;
			FOR(k,1,S) if (eq(s,w[k]))  {m[j] = k; break;}
		}
		
		FOR(i,1,S) dp[1][i] = 0;
		dp[1][m[1]] = INF;
		
		FOR(i,2,Q)
		{
			FOR(j,1,S) dp[i][j] = dp[i-1][j];
			int mi = INF;
			FOR(j,1,S) if (mi>dp[i-1][j]) mi = dp[i-1][j];
			mi++;
			FOR(j,1,S) if (dp[i][j]>mi) dp[i][j] = mi;
			dp[i][m[i]] = INF;
		}
		int mi = INF;
		FOR(i,1,S) if (dp[Q][i]<mi) mi = dp[Q][i];
		WR("Case #%d: %d",t,mi);
		if (t<T) WR("\n");
	}
	return 0;
}