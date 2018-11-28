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

const int mod = 1000000007;
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

ll n;
int b;
const int h=70;
int fac[h+1];
int k[h+1][h*h+h];

map<ll, int> m[h];

int cc[h+1][h+1];
int c (int n, int k)
{
	return cc[n][k];
//	return mul(fac[n], mul(faci[k], faci[n-k]));
}

int f (ll n, int l)
{
	if(n==0)
	{
		if(l==0) return 1;
		else return 0;
	}
	if(n<0 || l==0) return 0;
	if(m[l].count(n)) return m[l][n];
	int ans = 0;
	int r = n%b;
	REP(j, l+1)
	{
		REP(i, l+1)
			ans = (ans + mul(mul(c(l, i), fac[i]), mul(k[l][j*b + r], f((n/b)-j, i)))) % mod;
		FOR(i, 1, l+1)
		{
//			if(n==8 && i==1 && j==0) printf("%d %d %d %d\n", c(l-1, i-1), fac[i], k[l-1][j*b + r], f((n/b)-j, i));
			ans = (ans + mul(mul(c(l-1, i-1), fac[i]), mul(k[l-1][j*b + r], f((n/b)-j, i)))) % mod;
		}
	}
//	printf("%I64d %d: %d\n", n, l, ans);
	return m[l][n] = ans;
}

int main()
{
#ifdef LocalHost
freopen("d-small-attempt0.in", "r", stdin);//-small-attempt0
freopen("d-small-attempt0.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
	cc[0][0]=1;
	REP(i, h)
	{
		cc[i][0]=1;
		REP(j, h) cc[i+1][j+1] = (cc[i][j]+cc[i][j+1]) % mod;
	}
	fac[0]=1;
	REP(i, h) fac[i+1] = mul(fac[i], i+1);
REP(it, T)
{
	scanf("%I64d%d", &n, &b);
	CL(k, 0);
	k[0][0]=1;
	//y[1][0]=1;
	FOR(i, 1, b) for(int j=h-1; j>=0; --j)
		REP(u, h*h) k[j+1][u+i] += k[j][u];
//	REP(i, 10) { REP(j, 20) printf("%d", k[i][j]); printf("\n"); }
	REP(i, b+1) m[i].clear();
	int ans = 0;
	FOR(i, 1, b+1) ans = (ans + f(n, i)) % mod;
	printf("Case #%d: %d\n", it+1, ans);
}
	return 0;
}
