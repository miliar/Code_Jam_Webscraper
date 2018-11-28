#include <stdio.h>

int main() {

	int T;
	scanf("%d", &T);
	int pd, pg;
	long long N;
	for(int q=0;q<T;q++) {
		scanf("%lld %d %d", &N, &pd, &pg); 
		printf("Case #%d: ", q+1);
		if(pg == 100 && pd != 100) {
			printf("Broken\n");
			continue;
		}
		if(pg == 0 && pd != 0) {
			printf("Broken\n");
			continue;
		}
		if(N < 100LL) {
			bool flag = false;
			for(int i=1;i<=N;i++) {
				if((pd*i) % 100 == 0) {
					flag = true;
					break;
				}
			}
			if(!flag) {
				printf("Broken\n");
				continue;
			}
		}
		printf("Possible\n");
		

	}
	return 0;
}

