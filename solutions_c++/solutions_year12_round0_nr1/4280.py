#include<stdio.h>
char c,*s="yhesocvxduiglbkrztnwjpfmaq";
main(){
	int i,j,k,T;
	scanf("%d",&T);
	getchar();
	for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		while((c=getchar())!='\n'){
			putchar(c==' '?' ':s[c-'a']);
		}
		puts("");
	}
	scanf(" ");
}
