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
#define DLINE   ;
#define DL(_form, ...) ;
#define D(...) ;
#endif

void solve()
{
	int n, m=INFI, x=0, a;
	LL s=0;
	scanf("%d", &n);
	REP(i, n) scanf("%d", &a), m=min(m,a),x^=a, s+=a;
	
	if(x)
		printf("NO\n");
	else
		printf("%lld\n", s-m);
}

int main()
{
	int __T;
	scanf("%d", &__T);
	FOR(i, 1, __T) printf("Case #%d: ", i), solve();
	return 0;
}
