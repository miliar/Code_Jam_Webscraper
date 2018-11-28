#include<cstdio>

main(){
	int z,n,k; scanf("%d",&z);
	for(int t=1; t<=z; t++){
		scanf("%d %d",&n, &k);
		if( (((1<<n)-1) & k) == (1<<n)-1 )
			printf("Case #%d: ON\n",t);
		else printf("Case #%d: OFF\n",t);				
	}
	return 0;
}
