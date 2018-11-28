#include <cstdio>
#include <cstring>

const int maxn = 45;

double C[maxn][maxn];
double opt[maxn][maxn][maxn];
bool used[maxn][maxn][maxn];

double Calc(int a, int b) {
	if (a < 0 || b < 0) return 0;
	if (a < b) return 0;
	return C[a][b];
}

double Search(int C, int N, int curr) {
//printf("%d %d %d\n", C, N, curr);
	if (curr == C) {
		used[C][N][curr] = 1;
		opt[C][N][curr] = 0;
		return 0;
	}
	if (used[C][N][curr]) return opt[C][N][curr];
	used[C][N][curr] = 1;
	double sum = 1;
	int i;
	for (i = 1; i <= N && curr + i <= C; i++) {
		double prob = Calc(curr, N - i) / Calc(C, N) * Calc(C - curr, i);
		sum += prob * Search(C, N, curr + i);
	}
	/*
	printf("C[C][N] = %lf\n", ::C[C][N]);
	printf("%lf ", Calc(C, N));
	printf("%lf\n", Calc(curr, N) / Calc(C, N));
	*/
	sum /= (1 - Calc(curr, N) / Calc(C, N));
	return opt[C][N][curr] = sum;
}

void Prefix() {
	C[0][0] = 1;
	int i, j;
	for (i = 1; i < maxn; i++) {
		C[i][0] = C[i][i] = 1;
		for (j = 1; j < i; j++)
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
	}
}

int main() {
	Prefix();
	int t, i;
	scanf("%d", &t);
	memset(used, 0, sizeof used);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		int C, N;
		scanf("%d %d", &C, &N);
		printf("%.10lf\n", Search(C, N, 0));
	}
	return 0;
}
