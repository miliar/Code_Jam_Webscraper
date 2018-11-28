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


const int MAX = 1000;
const int INF = 1000000001;

LL tab[MAX];
int next[MAX];
LL W[MAX];
bool vis[MAX];

int n, k, r;
LL sum;
bool zlo;

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		sum = 0;
		zlo = false;
		scanf("%d %d %d", &r, &k, &n);
		REP(i,n)
			scanf("%lld", tab+i), sum += tab[i], zlo |= tab[i] > k, vis[i] = false;
		if(sum <= k) {
			printf("%lld\n", (LL)sum*r);
			continue;
		}
		if(zlo) {
			LL w = 0;
			REP(i,r)
			{
				if(tab[i] > k)
					break;
				w += tab[i];
			}
			printf("%lld\n", w);
			continue;
		}
		REP(i,n)
		{
			LL tmp = 0;
			int now = i;
			while(tmp + tab[now] <= k)
				tmp += tab[now],
				now = (now+1) % n;
			next[i] = now;
			W[i] = tmp;
		}
		int tutaj = 0;
		for(;!vis[tutaj];tutaj=next[tutaj])
			vis[tutaj] = true;
		int len = 1;
		LL S = W[tutaj];
		for(int i=next[tutaj];i!=tutaj;i=next[i])
			++len,
			S += W[i];
		LL w = 0;
		int now = 0;
		while(r)
		{
			if(now == tutaj) {
				w += S*(r/len);
				r %= len;
				REP(i,r)
					w += W[now],
					now = next[now];
				break;
			}
			w += W[now];
			now = next[now];
			--r;
		}
		printf("%lld\n", w);
	}
	return 0;
}

