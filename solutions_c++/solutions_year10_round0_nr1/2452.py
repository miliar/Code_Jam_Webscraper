#include <stdio.h>

int main(){
	
	int t;
	
	int n,k;
	
	int max;
	
	int teste=1;
	
	scanf("%d",&t);
	
	while(t--){
		
		scanf("%d %d",&n,&k);
	
		max = 1<<n;
	
		k = k % max;
		
		printf("Case #%d: ",teste++);
		if(k==max-1){
			printf("ON\n");
		}else{
			printf("OFF\n");
		}
		
		
	}
	
	
	
	
}
