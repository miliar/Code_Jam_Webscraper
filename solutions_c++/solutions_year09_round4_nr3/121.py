#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int h=200;
int t,n,k, p[h][h];

bool used[h], usedm[h];
int mt[h];
vi g[h];

bool match (int v)
{
	if(used[v]) return false;
	used[v]=true;
	REP(i, sz(g[v]))
	{
		int to=g[v][i];
		if(mt[to]==-1 || match(mt[to]))
		{
			mt[to]=v;
			return true;
		}
	}
	return false;
}

int main()
{
freopen("c-large.in", "r", stdin);
freopen("c-large.out", "w", stdout);
	scanf("%d", &t);
REP(it, t)
{
	scanf("%d%d", &n, &k);
	REP(i, n) REP(j, k)
		scanf("%d", &p[i][j]);
	REP(i, n) g[i].clear();
	REP(i, n) REP(j, n)
	{
		bool t=1;
		REP(c, k) if(p[i][c]>=p[j][c]) { t=0; break; }
		if(t) g[i].pb(j);
	}
	CL(usedm, 0);
	CL(mt, -1);
	int ans=0;
	REP(i, n) REP(j, sz(g[i]))
		if(mt[g[i][j]]==-1)
		{
			mt[g[i][j]]=i;
			usedm[i]=true;
			++ans;
			break;
		}
	REP(i, n) if(!usedm[i])
	{
		CL(used, 0);
		if(match(i)) ++ans;
	}
	printf("Case #%d: %d\n", it+1, n-ans);
}	
	return 0;
}
