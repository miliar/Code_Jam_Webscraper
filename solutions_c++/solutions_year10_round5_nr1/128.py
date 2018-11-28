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

int d,n,a,b, s[20];

int k, p[100000], mod;
vi x;

int mul (int x, int y) { return (ll(x)*y) % mod; }

int qpow (int x, int p)
{
	int res = 1;
	while(p)
	{
		if(p&1) res = mul(res, x);
		x = mul(x, x);
		p/=2;
	}
	return res;
}

int inv (int x)
{	return qpow(x, mod-2); }

int main()
{
#ifdef LocalHost
freopen("a-large.in", "r", stdin);//-small-attempt0
freopen("a-large.out", "w", stdout);//-large
#endif
	p[0]=2; p[1]=3; k=2;
	for(int i=5; i<1000000; i+=2)
	{
		int j;
		for(j=1; p[j]*p[j]<=i; j++)
			if(i%p[j]==0) break;
		if(p[j]*p[j]>i) p[k++]=i;
	}
	int T;
	scanf("%d", &T);
REP(it, T)
{
	scanf("%d%d", &d, &n);
	a=0;
	REP(i, n) scanf("%d", &s[i]), a=max(a, s[i]);
	b=1;
	REP(i, d) b*=10;
	
	int aa=-1, bb=-1;
	x.clear();
	if(n==1) goto no;
	
	REP(i, n-1) if(s[i]==0) bb=s[i+1];
	FOR(i, 2, n) if(s[i-2]!=s[i-1] && s[i-1]==s[i]) aa=0;
	
	if(n==2)
	{
		if(s[0]==s[1]) x.pb(s[0]);
		else if(bb!=-1 && (aa==0 || s[n-1]==0)) x.pb(bb);
		goto no;
	}
	
	REP(i, k) if(p[i]>a)
	{
		if(p[i]>b) break;
		mod = p[i];
		aa = -1;
		FOR(i, 1, n-1) if(s[i-1]!=s[i])
			aa = mul( s[i+1]-s[i]+mod , inv(s[i]-s[i-1]+mod) );
		if(aa==-1) aa=1, bb=0;
		else bb = (s[1] - mul(aa, s[0]) + mod) % mod;
		bool t=1;
		REP(i, n-1)
		{
			if(s[i+1] != (mul(aa, s[i]) + bb) % mod) t=0;
		}
		if(!t) continue;
		int v = (mul(aa, s[n-1]) + bb) % mod;
		if(x.empty()) x.pb(v);
		else
		{
			if(x[0]!=v) { x.pb(v); goto no; }
		}
	}
	no:;
	printf("Case #%d: ", it+1);
	if(sz(x)==1) printf("%d\n", x[0]);
	else printf("I don't know.\n");
}
	return 0;
}
