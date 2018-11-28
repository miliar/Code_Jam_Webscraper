#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
#include<map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int stmp;
#define scanf stmp=scanf


const int MAX = 100000;
const int INF = 1000000001;

int n, w, l;
LL R[MAX];

PII ans[MAX];

void solve(int y, VPII &C) {
	if(C.empty())
		return;
	int h = C.back().ST;
	for(int x=0;!C.empty() && x<=w;)
	{
		int lefth = h;
		int px = C.back().ST;
		int yh = -h+C.back().ST;
		if(y == 0) {
			yh = 0;
		}
		while(!C.empty() && yh + C.back().ST <= lefth)
		{
			ans[C.back().ND] = MP(x, y+yh);
			yh += C.back().ST;
			C.pop_back();
			if(!C.empty())
				yh += C.back().ST;
		}
		x += px;
		if(!C.empty())
			x += C.back().ST;
	}
	if(!C.empty())
		solve(y+h+C.back().ST, C);
}

LL sqr(LL x) { return x*x; }

void check() {
	int z = 0;
	REP(i,n)
	{
		if(ans[i].ST < 0 || ans[i].ST > w || ans[i].ND < 0 || ans[i].ND > l) debug("%d %d\n", ans[i].ST, ans[i].ND);
		REP(j,i)
		{
			if(sqr(ans[i].ST-ans[j].ST) + sqr(ans[i].ND-ans[j].ND) < sqr(R[i]+R[j]))
				++z;
		}
	}
	if(z)
		debug("%d\n", z);
}

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %d %d", &n, &w, &l);
		VPII C;
		REP(i,n)
		{
			int r;
			scanf("%d", &r);
			R[i] = r;
			C.PB(MP(r, i));
		}
		sort(ALL(C));
		solve(0, C);
		REP(i,n)
			printf("%d %d ", ans[i].ST, ans[i].ND);
		printf("\n");
		check();
	}
	return 0;
}

