#include <stdio.h>

int main(){
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<cas;i++){
		int n ,k;
		scanf("%d%d",&n,&k);
		int test = (1L<<n)-1;
		
		if ((k&test)==test){
			printf("Case #%d: ON\n",i+1);
		}else{
			printf("Case #%d: OFF\n",i+1);
		}
	}
	return 0;
}