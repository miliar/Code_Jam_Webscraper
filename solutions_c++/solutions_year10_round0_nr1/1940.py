#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int T,t,n,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(t = 0; t < T; t++){
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t+1);
		if(k%(1<<n) == (1<<n)-1) printf("ON\n");
		else{
			printf("OFF\n");
		}
	}
	return 0;
}