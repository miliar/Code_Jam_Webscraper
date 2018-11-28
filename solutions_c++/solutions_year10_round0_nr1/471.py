#include <stdio.h>

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,k;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",i+1);
		if((k%(1<<n))==(1<<n)-1)
			printf("ON\n");
		else
			printf("OFF\n");

	}

	return 0;
}