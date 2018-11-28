#include<stdio.h>
main(){
	int i,j,k;
	int T,TN;
	long long N;
	int D,G;
	scanf("%d",&T);
	for(TN=1;TN<=T;TN++){
		scanf("%I64d%d%d",&N,&D,&G);
		if(G==100&&D<100||G==0&&D>0){
			printf("Case #%d: Broken\n",TN);
			continue;
		}
		if(G==100&&D==G||G==0&&D==G){
			printf("Case #%d: Possible\n",TN);
			continue;
		}
		
		if(N>=100){
			printf("Case #%d: Possible\n",TN);
			continue;
		}
		if(D==0){
			printf("Case #%d: Possible\n",TN);
			continue;
		}
		
		for(i=1;i<=N;i++){
			for(j=1;j<=i;j++){
				if(j*100==i*D){
					printf("Case #%d: Possible\n",TN);
					break;
				}
			}
			if(j<=i)break;
		}
		if(i<=N)continue;
		printf("Case #%d: Broken\n",TN);
	}
		
}
