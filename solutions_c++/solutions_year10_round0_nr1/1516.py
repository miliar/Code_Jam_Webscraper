#include <stdio.h>

int main(){
	int n;
	int N,K;
	scanf("%d",&n);
	for(int i =1;i<=n;i++){
		scanf("%d %d",&N,&K);	
		if(!((K+1)%(1<<N))) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
