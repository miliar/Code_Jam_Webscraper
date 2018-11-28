#include <cstdio>
#include <cstring>

int N, S, P;
int inp[128];
int memo[128][128];
#define INF 0x3f3f3f3f

int dp(int n, int s) {
	if (s < 0) return -INF;
	if (n == N) {
		return 0;
	}
	int tr;

	if (memo[n][s] != -1) return memo[n][s];

	int p = inp[n] / 3;
	if (P == 1 && inp[n] == 0 || inp[n] < P || inp[n] - P - (P-2) < (P-2)) { // no chance
		tr = dp(n+1, s);
	} else if(inp[n] - P - (P-1) >= (P-1)) {
		tr = dp(n+1, s) + 1;
	} else {
		tr = dp(n+1, s);
		int t = dp(n+1, s-1)+1;
		if (t > tr) tr = t;
	}

	memo[n][s] = tr;
	return tr;
}


int main() {
	int T;
	scanf(" %d", &T);
	for (int i=0;i<T;++i) {
		printf("Case #%d: ", (i+1));
		
		scanf(" %d%d%d", &N, &S, &P);
		for (int i=0;i<N;++i) {
			scanf(" %d", &inp[i]);
		}
		memset(memo, -1, sizeof memo);
		printf("%d\n", dp(0, S));
	}
	return 0;
}