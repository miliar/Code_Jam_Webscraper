#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int pd[600][600];
int M = 100003;

int pascal[600][600];
int comb(int n, int p) {
	if (pascal[n][p] == -1) {
		if (n == p || p == 0) {
			pascal[n][p] = 1;
		} else {
			pascal[n][p] = comb(n-1,p) + comb(n-1,p-1);
			if (pascal[n][p] >= M) pascal[n][p] %= M;
		}
	}
	return pascal[n][p];
}
int N;
long long temp;
int calc(int n, int r) {
	if (pd[n][r] == -1) {
		if (r == 1) {
			pd[n][r] = 1;
		} else {
			
			// n eh o r-esimo element, entao tem que inserir r
			//if (n == N) printf("  Calculando pd %d %d..\n", n,r);
			pd[n][r] = calc(r,r-1); // coloca r na posicao r-1
			//if (n == N) printf("    Chamou pd %d %d..\n", r,r-1);
			for (int i = 2 ; i <= n-r && r-i >= 1 ; i++) {
				// coloca r na posicao r-i
				temp = (long long)comb(n-r-1,i-1);
				temp *= (long long) calc(r, r-i);
				//if (n == N) printf("    Chamou pd %d %d..\n", r,r-i);
				if (temp >= M) temp%=M;
				pd[n][r] += (int) temp;
				if (pd[n][r] >= M) pd[n][r]%=M;
			}
		}
		//printf("calc (%d %d) = %d\n", n,r, pd[n][r]);
	}
	return pd[n][r];
}

int process() {
	int total = 0;
	
	scanf("%d", &N);
	for (int i = 1 ; i < N ; i++) {
		total += calc(N,i);
		if (total >= M) total %=M;
	}
	return total;
}

int main() {
	
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	memset(pd,-1,sizeof(pd));
	memset(pascal,-1,sizeof(pascal));
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %d\n", i+1, process());
	}
	
	return 0;
}
