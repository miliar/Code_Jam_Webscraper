#include <stdio.h>
#include <string.h>


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		long long k;
		scanf("%d%lld",&n,&k);
		printf("Case #%d: %s\n",test,((k+1)%(1LL<<n)) ? "OFF" : "ON");
	}
	return 0;
}
