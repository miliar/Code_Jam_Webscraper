#include<stdio.h>

int nCase, N;

inline int abs(int x) { return x<0 ? -x : x; }

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		int to = 0, tb  = 0, po = 1, pb = 1;
		char c;
		int p;
		for(scanf("%d", &N); N > 0; --N) {
			scanf(" %c %d", &c, &p);
			if(c == 'O') {
				to = to + abs(po-p) + 1;
				if(to <= tb) to = tb + 1;
				po = p;
			} else {
				tb = tb + abs(pb-p) + 1;
				if(tb <= to) tb = to + 1;
				pb = p;
			}
		}
		printf("Case #%d: %d\n", cs, c=='O'?to:tb);
	}
}
