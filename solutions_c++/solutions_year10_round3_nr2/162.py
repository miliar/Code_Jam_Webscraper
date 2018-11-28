#include <stdio.h>
#include <string.h>

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		long long l,p,c;
		scanf("%lld%lld%lld",&l,&p,&c);
		int k=0;
		while(p>l*c) {
			++k;
			c*=c;
		}
		printf("Case #%d: %d\n",test,k);
	}
	return 0;
}
