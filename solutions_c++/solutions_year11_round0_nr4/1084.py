#include <cstdio>

int perm[1000];
double f[1001][1001];
double fact[1001];

double dp[1001];

const int MAXN = 1000;

int main() {

	f[0][0] = 1;
	fact[0] = 1;
	for (int N = 1; N<=MAXN; N++) {
		fact[N] = fact[N-1] * N;
		f[N][N] = 1.0 / fact[N];
		f[N][N-1] = 0;
		double sum = 1.0 / fact[N];
		for(int k = N-2; k>0; k--) {
			f[N][k] = f[N-k][0] / fact[k];
			sum+=f[N][k];
		}
		f[N][0] = 1 - sum;
	}
	
	dp[0] = dp[1] = 0;
	for(int N = 2; N<=MAXN; N++) {
		dp[N] = 1e1000;
		for(int hold = 0; hold<N-1; hold++) {
			if(hold == 1) {
				continue;
			}
			double curres = 0;
			for(int correct = 1; correct<=N-hold; correct++) {
				curres += f[N-hold][correct] * (dp[N-correct] + 1);
			}
			curres = (curres + f[N-hold][0]) / (1 - f[N-hold][0]);
			if(curres < dp[N]) {
				dp[N] = curres;
			}
		}
	}
	
	int TESTS;
	scanf("%d", &TESTS);
	for(int test = 1; test<=TESTS; test++) {
		int N;
		scanf("%d", &N);
		int incorrect = 0;
		for(int i = 0; i<N; i++) {
			scanf("%d", perm+i);
			if(perm[i] != i+1) {
				incorrect++;
			}
		}
		printf("Case #%d: %0.6lf\n", test, dp[incorrect]);
	}
	return 0;
}
