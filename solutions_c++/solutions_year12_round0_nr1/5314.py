#include <stdio.h>

char tr[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	int T,t;
	scanf("%d\n",&T);
	t=T;
	for(int i=0;i<T;i++){
		char buff[100] = {0};
		printf("Case #%d: ",i+1);
		gets(buff);
		for(int j=0;buff[j]!=0;j++)
			printf("%c",(buff[j]==32?32:tr[buff[j]-97]));
		printf("\n");
	}
	return 0;
}
