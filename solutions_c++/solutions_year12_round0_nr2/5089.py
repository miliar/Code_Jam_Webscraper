#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	int T,t,N,S,p,s,n;
	scanf("%d",&T);
	t=T;
	while(T--){
		printf("Case #%d: ",t-T);
		scanf("%d %d %d",&N,&S,&p);
		n=0;
		for(unsigned int i=0;i<N;i++){
			scanf("%d",&s);
			if(ceil(s/3.0)>=p||(s&&S&&ceil(s/3.0)+1>=p&&(S--||1))) n++;
		}
		printf("%d\n",n);
	}
}
