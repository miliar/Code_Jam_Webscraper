#include <cstdio>

int t,n,k,p,i;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d", &t);
	for(i=0;i<t;i++) {
		scanf("%d%d", &n, &k);
		p = 1 << n;
		if((k + 1) % p == 0)
			printf("Case #%d: ON\n", i+1);
		else
			printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}