#include<stdio.h>
main(){
	int i,j,k;
	int T,TT;
	int n;
	char c[2],rc;
	int a,b,ta,tb;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		scanf("%d",&n);
		a=b=1;
		ta=tb=0;
		for(i=0;i<n;i++){
			rc=*c;
			scanf("%s%d",c,&k);
			if(*c=='O'){
				ta+=(k-a)>?(a-k);
				if(i&&rc=='B'){
					ta>?=tb;
				}
				ta++;
				a=k;
			} else {
				tb+=(k-b)>?(b-k);
				if(i&&rc=='O'){
					tb>?=ta;
				}
				tb++;
				b=k;
			}
			//printf("%d %d\n",ta,tb);
		}
		printf("Case #%d: %d\n",TT,ta>?tb);
	}
}
