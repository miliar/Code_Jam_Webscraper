#define _CRT_SECURE_NO_DEPRECATE
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define infL (1LL<<62)
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
int N, M, K;
#define MAXN 510
int a[MAXN][MAXN];
vi g[MAXN];
void dfs(int v, int p)
{
	FOR(i,0,N)
	{
		if (a[v][i] && i != p)
		{
			g[v].pb(i);
			dfs(i,v);
		}
	}
}
#define MOD 1000000009
ll rec(int v, int mn, int add)
{
	ll res=1;
	int sons = sz(g[v]);
	for (int i=0,n=sz(g[v]); i<n; ++i)
	{
		int p = g[v][i];
		ll tmp = max(K-mn-i, 0)*rec(p, sons+add, 1)%MOD;
		res = res*tmp%MOD; 
	}
	return res;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
//#define SHOW_TIME
#ifdef SHOW_TIME
	clock_t startTime = clock();
#endif

	int Q;
	scanf("%d", &Q);
	FOR(q,0,Q)
	{
		printf("Case #%d: ", q+1);
		fflush(stdout);

		FOR(i,0,MAXN) g[i].clear();
		fill(a,0);
		scanf("%d%d", &N, &K);
		FOR(i,0,N-1)
		{
			int p1, p2;
			scanf("%d%d", &p1, &p2);
			--p1, --p2;
			a[p1][p2] = 1;
			a[p2][p1] = 1;
		}
		dfs(0,-1);
		ll res = rec(0,0,0);
		printf("%lld\n", res%MOD);
	}

#ifdef SHOW_TIME
	clock_t endTime = clock();
	printf("\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
#endif
	return 0;
} 
