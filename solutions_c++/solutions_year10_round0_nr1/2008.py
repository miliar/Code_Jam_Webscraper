#include<stdio.h>
main(){
	int i,j,k;
	int T,n;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d%d",&n,&k);
		if(k%(1<<n)==(1<<n)-1){
			printf("Case #%d: ON\n",i);
		} else {
			printf("Case #%d: OFF\n",i);
		}
	}
	//scanf(" ");
}
