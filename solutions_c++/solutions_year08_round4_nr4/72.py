#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

const int L = 51200, S = 1<<16;
const int INF = 1<<20;

int main()
{
	char str[L];
	int T, K;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		scanf("%d %s", &K, str);
		int n = strlen(str), m = n/K;
		int w1[16][16] = { 0 }, w2[16][16] = { 0 };
		// i -> j
		FOR(i, 0, K) FOR(j, 0, K) FOR(k, 0, m)
			if(str[k*K+i] != str[k*K+j]) w1[i][j]++;
		
		FOR(i, 0, K) FOR(j, 0, K) FOR(k, 0, m-1)
			if(str[k*K+i] != str[k*K+K+j]) w2[i][j]++;
		FOR(i, 0, K) FOR(j, 0, K) w2[i][j]++;
		
		int dp[S][18], res = 1<<20;
		FOR(i, 0, K) {
			// i is the first char
			//fprintf(stderr, "%d\n", i);
			FOR(k, 0, 1<<K) FOR(l, 0, K) dp[k][l] = INF;
			dp[1<<i][i] = 0;
			FOR(k, 0, 1<<K) FOR(l, 0, K) FOR(x, 0, K) if(!(k&(1<<x)))
				dp[k|(1<<x)][x] <?= dp[k][l]+w1[l][x];
			FOR(k, 0, K) if(k != i) res <?= dp[(1<<K)-1][k]+w2[k][i];
		}
		printf("Case #%d: %d\n", t, res);
		//fprintf(stderr, "Case #%d: %d\n", t, res);
	}
	return 0;
}

