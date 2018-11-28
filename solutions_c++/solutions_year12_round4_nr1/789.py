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


const int MAX = 10010;
const int INF = 1000000001;

int d[MAX];
int l[MAX];
int dp[MAX];

int n, k;

bool solve() {
	dp[1] = d[1];
	FOR(i,1,n)
	{
		int t = min(l[i], dp[i]);
		dp[i] = t;
		for(int j=i+1;j<=n && d[i]+t >= d[j];++j)
			dp[j] = max(dp[j], d[j]-d[i]);
	}
	FOR(i,1,n)
		if(d[i] + dp[i] >= k)
			return true;
	return false;
}

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d", &n);
		FOR(i,1,n)
		{
			dp[i] = 0;
			scanf("%d %d", d+i, l+i);
		}
		scanf("%d", &k);
		printf("%s\n", solve() ? "YES" : "NO");
	}
	return 0;
}

