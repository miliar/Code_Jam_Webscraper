#include <stdio.h>
#include <string.h>

#define Min(a,b) ((a)<(b)?(a):(b))

const int S = 105;
const int Q = 1010;
const int MAXINT = 1000000000;

char s[S][105];
char q[Q][105];
int c[Q][S];
int ns, nq;
int dp[Q][S];


void pre_calculate() {
	int i, j, k;
	for(i = 0; i < nq; ++i) {
		for(j = 0; j < ns; ++j) {
			for(k = i; k < nq && strcmp(q[k], s[j]) != 0; ++k);
			c[i][j] = k;
		}
	}
}

int go(int x, int y) {
	int k;
	int & ret = dp[x][y];
	if(x == nq) return -1;
	if(ret != -1) return ret;

	ret = MAXINT;
	for(k = 0; k < ns; ++k) if(k != y) {
		ret = Min(go(c[x][y], k)+1, ret);
	}
	// printf("dp[%d][%d] = %d\n", x, y,ret);
	return ret;
}

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("result.txt", "w", stdout);

	int ntc, i, tc = 0;
	scanf("%d", &ntc);
	while(ntc--) {
		scanf("%d\n", &ns);
		for(i = 0; i < ns; ++i) {
			gets(s[i]);
		}
		scanf("%d\n", &nq);
		for(i = 0; i < nq; ++i) {
			gets(q[i]);
		}

		if(nq == 0) {
			printf("Case #%d: 0\n", ++tc);
			continue;
		}
		pre_calculate();

		for(i = 0; i < nq; ++i)
			memset(dp[i], -1, ns*sizeof(dp[i][0]));

		int min = MAXINT;
		for(i = 0; i < ns; ++i) {
			int cand = go(0, i);
			min = Min(min, cand);
		}
		printf("Case #%d: %d\n", ++tc, min);
	}
	return 0;
}