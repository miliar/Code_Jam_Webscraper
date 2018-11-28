#include <stdio.h>

int main(){
	int T,t;
	scanf("%d",&T);
	t=T;
	while(T--){
		int R,K,N,earn=0,gn=0;
		scanf("%d %d %d",&R,&K,&N);
		int g[N];
		for(int i=0;i<N;i++)
			scanf("%d",&g[i]);
			
		while(R--){
			int k=K,gns=gn,v=0;
			while(k>=g[gn]){ if(gn==gns and v) break;else if(gn==gns) v=1; k-=g[gn]; if(gn+1==N) gn=0; else gn++;}
			earn+=K-k;
		}
		printf("Case #%d: %d\n",t-T,earn);
	};
};
