#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct table {
	int s, f, r;
}Table;

int cmp(const void *a, const void *b) {
	Table *x = (Table*)a;
	Table *y = (Table*)b;
	if( x->s != y->s ) return x->f - y->f;
	return x->s - y->s;
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int nRound;
	scanf("%d", &nRound);
	for(int round = 1; round <= nRound; round++) {
		int T, nA, nB;
		Table S[200];
		int visit[200];
		int a, b, c, d;
		int res[2] = {0};
		scanf("%d %d %d", &T, &nA, &nB);
		for(int i = 0; i < nA; i++) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			S[i].s = a*60 + b;
			S[i].f = c*60 + d;
			S[i].r = 0;
			if( S[i].s > S[i].f ) S[i].f += 24*60;
		}
		for(int i = 0; i < nB; i++) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			S[nA + i].s = a*60 + b;
			S[nA + i].f = c*60 + d;
			S[nA + i].r = 1;
			if( S[nA + i].s > S[nA + i].f ) S[nA + i].f += 24*60;
		}
		memset(visit, 0, sizeof visit);
		qsort(S, nA + nB, sizeof S[0], cmp);
		
		for(int s = 0; s < nA + nB; s++) {
			if( visit[s] ) continue;
			int fl = 1;
			int last = s;
			res[ S[s].r ]++;
			visit[s] = 1;
			while( fl ) {
				fl = 0;
				int minTemp = 1<<30, d;
				for(int i = last + 1; i < nA + nB; i++) {
					if( visit[i] ) continue;
					if( S[i].r == (S[last].r + 1)%2 && S[i].s >= S[last].f + T && S[i].f < minTemp ) {
						minTemp = S[i].f;
						d = i;
						fl = 1;
					}
				}

				if( fl ) {
					visit[d] = 1;
					last = d;
				}
			}	
		}
		printf("Case #%d: %d %d\n", round, res[0], res[1]);
	}
	return 0;
}