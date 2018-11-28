#include<algorithm>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof(Z.begin()) x=Z.begin();x!=Z.end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) X.begin(),X.end()

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif


const int MAX = 100;
const int INF = 1000000001;

pair<char,int> tab[MAX];
VI C[256];

int n;

void go() {
	int o = 0, b = 0;
	int po = 1, pb = 1;
	int button = 0;
	int ans = 0;
	for(;button<n;++ans)
	{
		if(tab[button].ST == 'O' && po == tab[button].ND) {
			++button;
			++o;
			if(b < C['B'].size()) {
				if(pb < C['B'][b])
					++pb;
				else if(pb > C['B'][b])
					--pb;
			}
		}
		else if(tab[button].ST == 'B' && pb == tab[button].ND) {
			++button;
			++b;
			if(o < C['O'].size()) {
				if(po < C['O'][o])
					++po;
				else if(po > C['O'][o])
					--po;
			}
		}
		else {
			if(b < C['B'].size()) {
				if(pb < C['B'][b])
					++pb;
				else if(pb > C['B'][b])
					--pb;
			}
			if(o < C['O'].size()) {
				if(po < C['O'][o])
					++po;
				else if(po > C['O'][o])
					--po;
			}
		}
	}
	printf("%d\n", ans);
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		C['O'].clear();
		C['B'].clear();
		scanf("%d", &n);
		REP(i,n)
		{
			char c;
			int p;
			scanf("\n%c %d", &c, &p);
			tab[i] = MP(c, p);
			C[c].PB(p);
		}
		go();
	}
	return 0;
}

