#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <functional>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

int a[1000100]; LL odl[1000100];

int main(void) {
	int T; scanf("%d", &T);
	FOR(te,1,T+1) {
		int L, n, C; LL t; scanf("%d%lld%d%d", &L, &t, &n, &C);
		REP(i,C)
			scanf("%d", &a[i]);
		FOR(i,C,n)
			a[i]=a[i-C];
		odl[0]=0;
		FOR(i,1,n+1) {
			odl[i]=odl[i-1]+a[i-1];
			//printf("%d -> %lld\n", i, odl[i]);
		}
		LL res=odl[n]*2LL; vector<LL> x;
		FOR(i,1,n+1) {
			if(odl[i]>t/2LL) {
				if(odl[i-1]>=t/2LL)
					x.PB(odl[i]-odl[i-1]);
				else
					x.PB(odl[i]-t/2LL);
			}
		}
		/*puts("--x ");
		REP(i,SZ(x))
			printf("%lld ", x[i]); puts("");
		printf("%lld\n", res);*/
		sort(ALL(x), greater<int>());
		REP(i,min(SZ(x),L))
			res-=x[i];
		printf("Case #%d: %lld\n", te, res);
	}
	return 0;
}
