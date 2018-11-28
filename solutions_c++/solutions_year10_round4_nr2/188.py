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

const int N=1111;
int p,n;
int m[N], c[11][N];
ll a[11][N][11];

int main()
{
#ifdef LocalHost
freopen("b-large.in", "r", stdin);//-small-attempt
freopen("b-large.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
REP(it, T)
{
	scanf("%d", &p);
	n = 1<<p;
	REP(i, n) scanf("%d", &m[i]);
	REP(j, p) REP(i, 1<<(p-j-1))
		scanf("%d", &c[j][i]);
//	CL(a, -1);
	REP(i, n/2)
	{
		int x = min(m[2*i], m[2*i+1]);
		REP(u, x) a[0][i][u] = 0;
		a[0][i][x] = c[0][i];
		FOR(u, x+1, p+1) a[0][i][u] = -1;
	}
	FOR(j, 1, p) REP(i, 1<<(p-j-1))	REP(x, p+1)
	{
		a[j][i][x] = -1;
		if(a[j-1][2*i][x]!=-1 && a[j-1][2*i+1][x]!=-1)
			a[j][i][x] = a[j-1][2*i][x] + a[j-1][2*i+1][x] + c[j][i];
		if(x<p && a[j-1][2*i][x+1]!=-1 && a[j-1][2*i+1][x+1]!=-1)
		{
			ll t = a[j-1][2*i][x+1] + a[j-1][2*i+1][x+1];
			if(a[j][i][x]==-1) a[j][i][x] = t;
			else a[j][i][x] = min(a[j][i][x], t);
		}
	}
	ll ans = -1;
	REP(x, p+1) if(ans==-1 || a[p-1][0][x]!=-1 && a[p-1][0][x]<ans) ans = a[p-1][0][x];
	printf("Case #%d: %I64d\n", it+1, ans);
}
	return 0;
}
