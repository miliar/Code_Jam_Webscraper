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

int r,k,n, g[1111];
int u[1111];
vi p;
ll s[1111], t;

int main()
{
#ifdef LocalHost
freopen("c-large.in", "r", stdin);//-small-attempt
freopen("c-large.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
REP(it, T)
{
	scanf("%d%d%d", &r, &k, &n);
	REP(i, n) scanf("%d", &g[i]);
	p.clear();
	CL(u, -1);
	s[0]=0;
	int j=0;
	while(u[j]==-1)
	{
		u[j] = sz(p);
		p.pb(j);
		int i=j;
		t=g[j];
		while(t<=k)
		{
			++i; if(i==n) i=0;
			t+=g[i];
			if(i==j) break;
		}
		s[sz(p)] = s[sz(p)-1] + t-g[i];
		j=i;
	}
	int l = sz(p)-u[j];
	ll ans = 0, t=s[u[j]];
	if(r<u[j]) ans = s[r];
	else
	{
		ans = t;
		r -= u[j];
		ans += (r/l) * (s[sz(p)] - t);
		ans += s[u[j] + (r%l)] - t;
	}
	printf("Case #%d: %I64d\n", it+1, ans);
}
	return 0;
}
