#include <cstdio>

int i, n, k, t;
int p[31];
int main() {

	p[0] = 1;
	for(i=1;i<31;i++) p[i]=p[i-1]*2;

	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		scanf("%d %d",&n,&k);
		if ((k+1)%p[n]==0) printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	return 0;
}
