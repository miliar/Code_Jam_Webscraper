

#include <stdio.h>
#include <stdlib.h>

int main(void){
	int i,j,k,l,R;
	int T,N;
	int *g;
	int ret;
	int idx;
	scanf("%d\n",&T);
	for (i=0;i<T;i++){
		scanf("%d %d %d\n",&R,&k,&N);
		g=new int[N];ret=0;
		for (j=0;j<N;j++){scanf("%d ",&g[j]);}
		idx=0;
		for (j=0;j<R;j++){
			int rest=k;
			for (l=0;l<N;l++){
				if (rest<g[idx])break;
				ret+=g[idx];
				rest-=g[idx];
				idx++;idx=idx%N;
			}
		}
		printf("Case #%d: %d\n",i+1,ret);
		delete[] g;
	}
	return 0;
}
