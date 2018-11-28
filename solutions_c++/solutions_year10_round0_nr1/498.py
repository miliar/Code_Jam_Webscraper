#include <stdio.h>

main(){
	int testcase;
	scanf("%d",&testcase);
	for(int t=1;t<=testcase;t++){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t);
		if((k&((1<<n)-1))==((1<<n)-1))printf("ON\n");
		else printf("OFF\n");
	}
}