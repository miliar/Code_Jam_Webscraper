#include <stdio.h>

int main(){
	int i,t,n,k,c;
	scanf("%d",&t);
	for (i=1;i<=t;i++){
		scanf("%d %d",&n, &k);
		c = (1<<n)-1;
		printf("Case #%d: %s\n",i,(k&c)==c?"ON":"OFF");
	}
	return 0;
}

