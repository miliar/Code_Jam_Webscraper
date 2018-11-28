#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <string.h>
using namespace std;

int C[1005];

//const int N = 11;
//double f[N], comb[N][N], D[N], A[N];
//
//void calc() {
//	memset(comb, 0, sizeof(comb));
//	int i, j;
//	for(comb[0][0] = 1, i = 1; i < N; ++i)
//		for(comb[i][0] = 1, j = 1; j <= i; ++j)
//			comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
//
//	A[0] = 1;
//	for(i = 1; i < N; ++i) A[i] = A[i - 1] * i;
//
//	D[0] = 1;
//	D[1] = 0;
//	for(i = 2; i < N; ++i) D[i] = (i - 1) * (D[i - 1] + D[i - 2]);
//
//	memset(f, 0, sizeof(f));
//	for(i = 2; i < N; ++i){
//		double t = A[i] / (A[i] - D[i]);
//		for(j = 1; j <= i; ++j){
//			f[i] += comb[i][j] * D[i - j] / A[i] * (f[i - j] + t) * t;
//		}
//	}
//
//}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("op.out", "w", stdout);
//	calc();
	int testCase;
	scanf("%d", &testCase);
	for(int tc = 1; tc <= testCase; ++tc){
		int n;
		double res = 0;
		cin >> n;
		for(int i = 1; i <= n; ++i){
			scanf("%d", &C[i]);
		}
		for(int i = 1; i <= n; ++i){
			if(!C[i] || C[i] == i) continue;
			int cnt = 1;
			for(int j = i, Cj = C[j]; Cj != i; ++cnt){
				j = Cj;
				Cj = C[j];
				C[j] = 0;
			}
			C[i] = 0;
//			res += f[cnt];
			res += cnt == 2 ? 2 : cnt;
		}
		printf("Case #%d: %.6lf\n", tc, res);
	}
	return 0;
}
