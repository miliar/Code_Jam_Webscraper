#include <cstdio>
#include <memory.h>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>


#define MAXN 1100
#define inf (long long)1e10
#define min(a, b) ((a) < (b) ? (a) : (b))

int T, P;

int M[MAXN];
int C[11][MAXN];
long long d[11][MAXN][11];

long long calc(int lev, int x, int del) {
 	if (d[lev][x][del] != -1) return d[lev][x][del];

 	if (lev == 0) {
 	 	if (del > M[2 * x] || del > M[2 * x + 1]) {
 	 	 	return d[lev][x][del] = inf;
 	 	} else 
 	 	if (del == M[2 * x] || del == M[2 * x + 1]) {
 	 	 	return d[lev][x][del] = C[lev][x];
 	 	} else {
 	 	 	return d[lev][x][del] = 0;
 	 	}
 	}
 	d[lev][x][del] = min(calc(lev - 1, 2 * x, del) + calc(lev - 1, 2 * x + 1, del) + C[lev][x],
 						calc(lev - 1, 2 * x, del + 1) + calc(lev - 1, 2 * x + 1, del + 1));
 	return d[lev][x][del];
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	scanf("%d", &T);
	for (int q = 1; q <= T; q++) {
	 	scanf("%d", &P);
	 	for (int i = 0; i < 1<<P; i++) {
	 	 	scanf("%d", &M[i]);
	 	}

	 	for (int j = 0; j < P; j++) {
	 	 	for (int i = 0; i < 1<<(P - j - 1); i++) {
	 	 	 	scanf("%d", &C[j][i]);
                
	 	 	}       
	 	}
	 	for (int i = 0; i < 11; i++) {
	 	 	for (int j = 0; j < MAXN; j++) {
	 	 	 	for (int k = 0; k < 11; k++) {
	 	 	 	 	d[i][j][k] = -1;
	 	 	 	}
	 	 	}
	 	}
		printf("Case #%d: %lld\n", q, calc(P - 1, 0, 0));
	}
	
 	return 0;
}
