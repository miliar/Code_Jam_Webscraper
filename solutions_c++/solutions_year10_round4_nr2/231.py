#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1222333444555LL
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "B-large"

int n;
int miss[1024];
int cost[16][1024];
LL d[12][1024][10];

LL dfs(int s, int x, int missed)
{
	if (d[s][x][missed] != -1)
		return d[s][x][missed];
	if (s==0) return 0;
	LL res = dfs(s-1,2*x,missed)+dfs(s-1,2*x+1,missed)+cost[s][x];
	bool can=true;
	REP(i,1<<s)
		if (miss[x*(1<<s)+i] <= missed)
			can=false;
	if (can)
		res=min(res,dfs(s-1,2*x,missed+1)+dfs(s-1,2*x+1,missed+1));
	return d[s][x][missed] = res;
}

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);
		scanf("%d",&n);
		REP(i,1<<n)
			scanf("%d",&miss[i]);
		FOR(i,1,n)
			REP(j,1<<(n-i))
				scanf("%d",&cost[i][j]);
		FILL(d,-1);
		LL res = dfs(n,0,0);
		printf("Case #%d: %lld\n",tst+1,res);
	}
	return 0;
}