#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define INF 0x3F3F3F3F

using namespace std;

int pd[10010][2];
char folha[10010], muda[10010], no[10010];

void go(int a, int x) {
	if (pd[a][x] < INF) return;
	if (folha[a]) {
		if (x == no[a]) {
			pd[a][x] = 0;
		}
		return;
	}
	int esq, dir;
	esq = 2*a;
	dir = 2*a+1;
	go(2*a, 0);
	go(2*a, 1);
	go(2*a+1, 0);
	go(2*a+1, 1);
	if (x == 0) {
		// or
		if (no[a] == 0) {
			pd[a][x] = min(pd[a][x], pd[esq][0] + pd[dir][0]);
		}
		// and
		else {
			pd[a][x] = min(pd[a][x], min(pd[esq][0]+pd[dir][0], min(pd[esq][0]+pd[dir][1], pd[esq][1] + pd[dir][0])));
		}
		// se pode mudar soma 1
		if (muda[a]) {
			if (no[a] == 0) {
				pd[a][x] = min(pd[a][x],1+ min(pd[esq][0]+pd[dir][0], min(pd[esq][0]+pd[dir][1], pd[esq][1] + pd[dir][0])));
			}
			else {
				pd[a][x] = min(pd[a][x],1+ pd[esq][0] + pd[dir][0]);
			}
		}
	}
	else {
		if (no[a] == 0) {
			// or
			pd[a][x] = min(pd[a][x], min(pd[esq][0] + pd[dir][1], min(pd[esq][1]+pd[dir][0], pd[esq][1]+pd[dir][1])));
		}
		else {
			// and
			pd[a][x] = min(pd[a][x], pd[esq][1] + pd[dir][1]);
		}
		// se pode mudar soma 1
		if (muda[a]) {
			if (no[a] == 0) {
				pd[a][x] = min(pd[a][x], 1+pd[esq][1] + pd[dir][1]);
			}
			else {
				pd[a][x] = min(pd[a][x],1+min(pd[esq][0] + pd[dir][1], min(pd[esq][1]+pd[dir][0], pd[esq][1]+pd[dir][1])));
			}
		}
	}
}

int main() {
	int teste=1, N, M, V, G, C, i, I;
	scanf("%d", &N);
	while (N--) {
		scanf("%d %d", &M, &V);
		memset(folha, 0, sizeof(folha));
		memset(muda, 0, sizeof(muda));
		for (i=1;i<=(M-1)/2;i++) {
			scanf("%d %d", &G, &C);
			no[i] = G;
			if (C==1) muda[i] = 1;
		}
		for (;i<=M;i++) {
			scanf("%d", &I);
			no[i] = I;
			folha[i] = 1;
		}
		memset(pd, INF, sizeof(pd));
		go(1, V);
		printf("Case #%d: ", teste++);
		if (pd[1][V] == INF) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("%d\n", pd[1][V]);
		}
	}
	return 0;
}
