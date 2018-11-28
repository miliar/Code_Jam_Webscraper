#include <stdio.h>

int N,K;
int two[39];
int twosub[39];
int id;


void preSolve() {
	int i;
	two[0] = 1;
	for(i = 1; i <= 30; i++) {
		two[i] = two[i - 1] * 2;
		twosub[i] = two[i] - 1;
	}
}

void input() {
	scanf("%d%d",&N,&K);
}

void solve() {
	if(K % two[N] == twosub[N]) {
		printf("Case #%d: ON\n",++id);
	} else {
		printf("Case #%d: OFF\n",++id);
	}
}

int main() {
	int i,T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	preSolve();
	scanf("%d",&T);
	for(i = 0; i < T; i++) {
	input();
	solve();
	}
	return 0;
}