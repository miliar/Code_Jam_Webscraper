#include <stdio.h>

int main(){
	int i;
	scanf("%d",&i);
	for(int ii=1;ii<=i;++ii){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n", ii, (k+1)%(1<<n)==0?"ON":"OFF");
	}
	return 0;
}

