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

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

#define MOD 100003

long long bi[510][510], dp[510][510];

int main(void) {
	int n, m, i, j, k, T, t; long long res;
	bi[0][0]=1LL;
	FOR(i,1,502) {
		bi[i][0]=bi[i][i]=1LL;
		FOR(j,1,i)
			bi[i][j]=(bi[i-1][j-1]+bi[i-1][j])%MOD;
	}
	FOR(i,2,502)
		dp[1][i]=1LL;
	FOR(i,2,502) {
		FOR(j,i+1,502) {
			dp[i][j]=0LL;
			FOR(k,1,i) {
				if(j-i>=i-k) {
					dp[i][j]+=dp[k][i]*bi[j-i-1][i-k-1];
				}
			}
			dp[i][j]%=MOD;
		}
	}
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d", &n); res=0LL;
		FOR(i,1,n)
			res+=dp[i][n];
		res%=MOD;
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}

