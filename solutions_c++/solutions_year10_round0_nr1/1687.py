#include <stdio.h>
int T,n,k;

int main(void) {
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		scanf("%d%d",&k,&n);
		printf("Case #%d: ",_);
		if ((n & (1<<k)-1) == (1<<k)-1) puts("ON");
		else puts("OFF");
	}
	
	return 0;
}
