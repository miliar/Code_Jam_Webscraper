#include <stdio.h>

int main()
{
	int T, i, c;
	int in, aux;
	int pi[10];
	int pi2[10];
	
	scanf("%d\n",&T);
	c=1;
	while(T--){
		scanf("%d",&in);
		for(i=0;i<10;i++) pi[i]=0;
		aux=in;
		while(aux){
			pi[aux%10]++;
			aux/=10;
		}
		while(1){
			in++;
			for(i=1;i<10;i++) pi2[i]=0;
			aux=in;
			while(aux){
				pi2[aux%10]++;
				aux/=10;
			}
			for(i=1;i<10;i++) if(pi[i]!=pi2[i]) break;
			if(i==10){
				printf("Case #%d: %d\n",c,in);
				break;
			}
		}
		c++;
	}
	return 0;
}

