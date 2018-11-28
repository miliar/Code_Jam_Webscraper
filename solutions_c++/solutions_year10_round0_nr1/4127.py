#include <cstdio>

int main() {
	int ntc;
	scanf("%d",&ntc);
	for(int tc=1; tc<=ntc; ++tc) {
		printf("Case #%d: ",tc);
		int n,k;
		scanf("%d%d",&n,&k);
		if(k%(1<<n)==(1<<n)-1) printf("ON\n"); else printf("OFF\n");
	}
	return 0;
}
