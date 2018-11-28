#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)
#define SZ(AA) ((int)(AA.size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP(AA,BB) make_pair((AA), (BB))

#define INF 100000000000000LL

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

int BASE, c[10100], x[10100];
long long dp[10010][15];

long long rec(int a, int k) {
	if(a>=BASE) {
		if(k>x[a-BASE])
			return INF;
		return 0;
	}
	if(dp[a][k]!=-1)
		return dp[a][k];
	return dp[a][k]=min(rec(2*a,k)+rec(2*a+1,k)+c[a], rec(2*a,k+1)+rec(2*a+1,k+1));
}

int main(void) {
	int t, T, n, m, i, j, k;
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d", &n); BASE=(1<<n);
		REP(i,BASE)
			scanf("%d", &x[i]);
		for(i=n-1, j=BASE/2; i>=0; --i, j/=2) {
			REP(k,j)
				scanf("%d", &c[j+k]);
		}
		memset(dp, -1, sizeof dp);
		printf("Case #%d: %lld\n", t, rec(1, 0));
	}
	return 0;
}
