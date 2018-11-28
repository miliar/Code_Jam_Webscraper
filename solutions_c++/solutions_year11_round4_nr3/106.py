#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

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

int c[2000100]; VI pri;

int main(void) {
	int T; scanf("%d", &T);
	for(int i=2; i<=1500; ) {
		for(int j=i+i; j<=2000000; j+=i)
			c[j]=1;
		while(c[++i]);
	}
	FOR(i,2,2000000) {
		if(!c[i])
			pri.PB(i);
	}
	
	FOR(t,1,T+1) {
		LL N; scanf("%lld", &N);
		LL mx=(N==1?0:1), mn=0;
		for(int i=0; (LL)pri[i]*pri[i]<=N; ++i) {
			int k=0; LL x=1LL;
			while(x<=N) {
				x*=pri[i];
				++k;
			}
			--k;
			//printf("%d -> %d\n", pri[i], k);
			mx+=k; ++mn;
		}
		printf("Case #%d: %lld\n", t, mx-mn);
	}
	return 0;
}
	
