#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
using namespace std;
typedef long double LD;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL, LL> PLL;
typedef vector<int> VI;
typedef vector<PII> VPI;
typedef set<int> SI;
const LL INFLL=1000000000000000005LL;
const int INFI = 1000000005;
#define VAR(v,n) __typeof(n) v=(n)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define PER(i, n) for(int i=(n)-1;i>=0;--i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define FORE(i,c) for(VAR(i,(c).begin()); i!=(c).end(); ++i)
#define FORQ(i, a, b) for(int i=(a); (LL)i*i<=(b); ++i) 
#define FS first
#define SE second
#define MP make_pair
#define PB push_back
#define SIZE(x) ((int)(x).size())
//#define DEBUG
#ifdef DEBUG
#define DLINE             printf("Still alive to: %d\n", __LINE__);
#define DL(_form, ...)    fprintf(stderr, "%d: " _form, __LINE__, __VA_ARGS__);
#define D(...)             fprintf(stderr, __VA_ARGS__);
#else
#define DLINE   
#define DL(_form, ...) 
#define D(...) 
#endif

const int MAXN = 109;
int n;
int g[MAXN][MAXN];
int op[MAXN];
LD WP[MAXN],OWP[MAXN], OOWP[MAXN];
char a;
void solve()
{
	scanf("%d", &n);
	REP(iy, n)
		op[iy] = 0;
	
	REP(iy, n) REP(ix, n) 
	{
		scanf(" %c", &a);
		g[iy][ix]= ( a=='1'? 1 : (a=='0'?-1:0) );
		op[iy]+=g[iy][ix]!=0;
	}
	
	
	REP(iy, n) 
	{
		int w = 0;
		REP(ix, n) w += g[iy][ix]>0;
		WP[iy] = ((LD)w)/op[iy];
	}
	REP(iy, n)
	{
		LD owp=0.0;
		REP(ix, n) if(g[iy][ix]) owp += (WP[ix]*op[ix]-(g[ix][iy]==1))/(op[ix]-1);
		OWP[iy] = owp/op[iy];
	}
	REP(iy, n)
	{
		LD oowp=0.0;
		REP(ix, n) if(g[iy][ix]) oowp += OWP[ix];
		OOWP[iy] = oowp/op[iy];
	}
	REP(iy, n)
	{
		printf("%.9Lf\n", 0.25*WP[iy] + 0.5 * OWP[iy] + 0.25 * OOWP[iy]);
// 		printf("%c: WP: %.3Lf OWP: %.3Lf OOWP:%.3Lf\n", 'A'+iy, WP[iy], OWP[iy], OOWP[iy]);
	}
}

int main()
{
	int __T;
	scanf("%d", &__T);
	REP(i, __T) printf("Case #%d:\n", i+1), solve();
	return 0;
}
