#include <cstdio>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

const int N = 10240;
const int INF = 1<<20;

int dp[2][N];
int gate[N], val[N], changeable[N];

int op(int o, int a, int b) { return o == 0 ? (a|b) : (a&b); }

int main()
{
	int T;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		int n, v; scanf("%d %d", &n, &v);
		int n1 = (n-1)/2, n2 = n-n1;
		FOR(i, 0, n1) scanf("%d %d", &gate[i], &changeable[i]);
		FOR(i, 0, n2) scanf("%d", &val[i]);
		FOR(i, 0, n) dp[0][i] = dp[1][i] = INF;
		for(int i = n-1; i >= 0; i--)
			if(i >= n1) {
				// the leaf
				dp[val[i-n1]][i] = 0;
			} else {
				// the gate
				int lc = 2*i+1, rc = 2*i+2;
				FOR(a, 0, 2) FOR(b, 0, 2) dp[op(gate[i], a, b)][i] <?= dp[a][lc]+dp[b][rc];
				if(!changeable[i]) continue;
				FOR(a, 0, 2) FOR(b, 0, 2) dp[op(1^gate[i], a, b)][i] <?= dp[a][lc]+dp[b][rc]+1;
			}
		//printf("%d %d\n", dp[0][3], dp[1][3]);
		printf("Case #%d: ", t);
		if(dp[v][0] >= INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", dp[v][0]);
	}
	return 0;
}

