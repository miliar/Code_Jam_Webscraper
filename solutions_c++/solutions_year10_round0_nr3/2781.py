/*
TASK: Themed Park
LANG: C

Programmed by
Nat Pavasant
*/

#include <stdio.h>

int g[1010];
int t;

int R,k,N;

int main() {
	int i,j,c;
	int r,n,d;
	scanf("%d",&t);
	for (i = 0; i < t; i++) {
		scanf("%d%d%d",&R,&k,&N);
		for (j = 0; j < N; j++) scanf("%d",&g[j]);
		r = c = n = 0;
		for (j = 0; j < R; j++) {
			n = d = 0;
			for (; n + g[c%N] <= k && d < N; n += g[c++%N], d++);
			//printf(": %d\n", n);
			r += n;
		}
		printf("Case #%d: %d\n", i+1, r);
		
	}
	//scanf(" ");
	return 0;
}
