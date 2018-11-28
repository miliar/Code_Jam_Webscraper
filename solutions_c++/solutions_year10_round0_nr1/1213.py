#include <cstdio>

int main(){
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		int n,k;
		scanf("%d%d",&n,&k);
		if((((1<<n)-1)&k)==(1<<n)-1) printf("Case #%d: ON\n",ic);
		else printf("Case #%d: OFF\n",ic);
	}
	return 0;
}
