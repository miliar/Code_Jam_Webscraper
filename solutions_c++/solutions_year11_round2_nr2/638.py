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

const int MAXN = 209;
PII p[MAXN];
int D,n;

bool ok(LD v)
{
// 	printf("---\nTrying %Lf\n", v);
	LD last = -1e6;
	
	REP(i, n)
	{
		LD x = max(last + D, p[i].FS-v);
		last = x+ (p[i].SE-1) * D;
// 		printf("P[%d]=%d -> [%Lf, %Lf]\n", p[i].FS, p[i].SE, x, last-v);
		if(last - p[i].FS > v) return 0;
	}
	return 1;
}
void solve()
{
	scanf("%d%d", &n, &D);
	REP(i, n) scanf("%d%d", &p[i].FS, &p[i].SE);
	sort(p, p+n);
	
	LD s=0.0, e = 1.5e12;
// #	warningp E!!
	LD eps = 1e-9;
	int c =0;
	while( e-s > eps)
	{
		++c;
		LD m = (s+e)/2;
		if(ok(m))
			e = m;
		else
			s = m;
	}
	
// 	printf("%d\n", c);
	printf("%.8Lf", s);
}

int main()
{
	int __T;
	scanf("%d", &__T);
	REP(i, __T) printf("Case #%d: ", i+1), solve(), puts("");
	return 0;
}
	 