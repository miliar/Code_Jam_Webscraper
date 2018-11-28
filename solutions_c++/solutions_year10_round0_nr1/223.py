#include <stdio.h>

int main(int argc, char *argv[])
{
	int Case,N,T,K;
	scanf("%d",&T);
	Case = 0;
	while(T--) {
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",++Case);
		//if((1<<N)-1 == K) puts("ON");
//		else puts("OFF");
		if((K+1)%(1<<N) == 0) puts("ON");
		else puts("OFF");
	}
	return 0;
}
