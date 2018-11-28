#include <stdio.h>

inline int pow2(int n){
	int ret = 1;
	while(n--){
		ret <<= 1;
	}
	return ret;
}

int main(){
	int n,k;
	int ncas;
	scanf("%d",&ncas);
	for(int t=1;t<=ncas;t++){
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",
				t,(k%pow2(n)==(pow2(n)-1))?"ON":"OFF");
	}
	return 0;
}
