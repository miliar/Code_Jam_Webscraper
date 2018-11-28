#include <stdio.h>

int main(){
	int T;
	scanf("%d",&T);
	int testcase = 0;
	while(T-- > 0){
		testcase++;
		int n,k;
		scanf("%d%d",&n,&k);
		long long tot = (1<<(n));
		printf("Case #%d: ",testcase);
		long long K=k+1;
		if(K%tot == 0){
			printf("ON");
		}else{
			printf("OFF");
		}
		printf("\n");
	}
	return 0;
}
