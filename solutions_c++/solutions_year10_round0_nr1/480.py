#include <cstdio>
int ii,t,k,n;
int main() {
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",ii);
		if ((k+1)%(1<<n)) printf("OFF\n"); else printf("ON\n");
	}
	return 0;
}