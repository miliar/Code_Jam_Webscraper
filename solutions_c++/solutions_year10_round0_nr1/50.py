#include <stdio.h>

int main(){
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<cas;i++){
		int n ,k;
		scanf("%d%d",&n,&k);
		int aim = (1L<<n)-1;
		printf("Case #%d: ",i+1);
		if ((k&aim)==aim){
			printf("ON\n");
		}else{
			printf("OFF\n");
		}
	}
	return 0;
}