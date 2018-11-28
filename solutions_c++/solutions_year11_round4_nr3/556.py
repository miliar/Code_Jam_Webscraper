#include<stdio.h>
#include<algorithm>
main(){
	int TT,TN;
	long long N,i,j,k;
	bool f;
	scanf("%d",&TT);
	for(TN=1;TN<=TT;TN++){
		printf("Case #%d: ",TN);
		scanf("%I64d",&N);
		if(N==1||N==2){
			printf("0\n");
			continue;
		}
		k=0;
		for(i=2;i*i<=N;i++){
			f=0;
			for(j=2;j*j<=i;j++){
				if(i%j==0){
					f=1;
					break;
				}
			}
			if(f)continue;
			for(j=i*i;j<=N;j=j*i){
				
				//printf("%I64d^%I64d\n",i,j);
				
				k++;
			}
		}
		printf("%I64d\n",k+1);
				
		
		
	}
}

